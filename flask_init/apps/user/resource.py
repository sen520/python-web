from flask import current_app, request
from flask.views import MethodView
from util.gpt_util import Chat
from controllers.db import *

class UserRegisterView(MethodView):
    methods = ["GET", "POST", 'PUT', 'DELETE']

    def __init__(self, *args, **kwargs):
        self.logger = current_app.logger
        self.chat = current_app.chat
        super().__init__(*args, **kwargs)

    def get(self):
        self.logger.error('error')
        self.logger.debug('debug')
        self.logger.info('info')
        message = request.args.get('message')
        user = UserController.get_one('张森')
        if not user:
            user_id = UserController.insert(**{'username': '张森', 'age': 18})
        else:
            user_id = user.id
        return {'user_id': user_id, 'message': message}

        # self.chat.set_message({'role': 'system', 'content': '你是一个聊天机器人'})

        # print('GPT TEST')
        # self.chat.set_message({'role': 'user', 'content': message})
        # try:
        #     response = self.chat.get_response()
        # except:
        #     return 'time out'
        # self.chat.set_message({'role': response.message.role, 'content': response.message.content})
        # message = self.chat.get_all_message()
        # MessageController.add(user_id, message)
        # return response.message.content



    def post(self):
        # self.user_ctl.add(username='test')
        result = {"code": 0, "msg": "注册成功"}
        return result

    def put(self):
        # self.user_ctl.update(id=4, username='test1')
        return 'put'

    def delete(self):
        self.chat.clear()
        # self.user_ctl.delete(id=1)
        return 'delete'
