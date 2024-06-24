import os.path

from tinydb import TinyDB, Query
from settings import Config

from models.model import User, Id, Message


class IDController:
    def __init__(self):
        self.db = TinyDB(os.path.join(Config.DB_DIR, 'id.json'))
        self.DB_QUERY = Query()

    def get(self, table_name):
        result = self.db.search(self.DB_QUERY.name == table_name)
        if result:
            self.inc(table_name, result[0]['id'])
            return result[0]['id'] + 1
        id_obj = Id(table_name)
        self.db.insert(id_obj.__json__())
        return 1

    def inc(self, table_name, line_id):
        self.db.update({'id': line_id + 1}, self.DB_QUERY.name == table_name)


class UserController:
    db = TinyDB(os.path.join(Config.DB_DIR, 'users.json'))
    UserQuery = Query()
    table_name = 'users'

    @classmethod
    def get(cls, username):
        return cls.db.search(cls.UserQuery.username == username)

    @classmethod
    def get_one(cls, username):
        users = cls.db.search(cls.UserQuery.username == username)
        return User(**users[0]) if users else None

    @classmethod
    def insert(cls, **user_dict):
        user = User(**user_dict)
        if cls.db.search(cls.UserQuery.username == user.username):
            return False
        Id = IDController()
        user_id = Id.get(cls.table_name)
        user.id = user_id
        cls.db.insert(user.__json__())
        return user_id

    @classmethod
    def delete(cls, user_id):
        cls.db.remove(cls.UserQuery.id == user_id)
        return True


class MessageController:
    db = TinyDB(os.path.join(Config.DB_DIR, 'messages.json'))
    MessageQuery = Query()
    table_name = 'messages'

    @classmethod
    def get(cls, user_id):
        return cls.db.search(cls.MessageQuery.user_id == user_id)

    @classmethod
    def update(cls, user_id, message_id, message):
         return cls.db.update({'message': message}, cls.MessageQuery.user_id == user_id and cls.MessageQuery.message_id ==message_id)

    @classmethod
    def add(cls, user_id, message):
        Id = IDController()
        message_id = Id.get(cls.table_name)
        Mes = Message(**{'id': message_id, 'messages': message, 'user_id': user_id})
        cls.db.insert(Mes.__json__())
        return message_id


if __name__ == '__main__':
    u = UserController.get_one('张森')
    # UserController.delete(9)
    # UserController.insert(**{'username': '张森'})
    # u = UserController.get('张森')
    # print(u.id)
    # MessageController.add(u.id, [{'role': 'system', 'content': '你是一个聊天机器人'}, {'role': 'user', 'content': '你是谁'}])
    # print(MessageController.get(u.id))
