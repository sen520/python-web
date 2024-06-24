class User(object):
    def __init__(self, **user_dict):
        self.id = user_dict.get('id')
        self.username = user_dict['username']
        self.age = user_dict.get('age')

    def __json__(self):
        return {
            "id": self.id,
            "username": self.username,
            "age": self.age
        }


class Id:
    def __init__(self, table_name):
        self.name = table_name
        self.id = 1

    def __json__(self):
        return {
            "name": self.name,
            'id': self.id
        }


class Message:
    def __init__(self, **message_dict):
        self.id = message_dict.get('id')
        self.messages = message_dict['messages']
        self.user_id = message_dict['user_id']

    def __json__(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'messages': self.messages
        }