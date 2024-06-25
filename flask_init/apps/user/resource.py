from flask import request
from flask import current_app
from flask_restx import Api, Resource, fields, reqparse

from apps.user import api
from controllers.db import *
from controllers.mysql_db import UserDAO

ns = api.namespace('user', description='user operations')


@ns.route('/register')
class UserRegister(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = current_app.logger
        self.chat = current_app.chat
        super().__init__(*args, **kwargs)

    @ns.doc(params={
        'message': {'description': 'Name to greet', 'type': 'string', 'required': True},
        'age': {'description': 'Age of the person', 'type': 'integer', 'required': False}
    })
    def get(self):
        """ get method """
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

    # @ns.expect(ns.model('HelloModel', { # json
    #     'name': fields.String(required=True, description='Name to greet'),
    #     'age': fields.Integer(required=False, description='Age of the person')
    # }))
    @ns.expect(reqparse.RequestParser()  # form-data
                .add_argument('name', type=str, required=True, help='Name to greet', location='form')
                .add_argument('age', type=int, required=False, help='Age of the person', location='form'))
    @ns.response(200, 'success')
    @ns.response(404, 'not found')
    def post(self):
        """ post method """
        u = UserDAO.get_all()
        print(u, '22222')
        u = UserDAO.get_by_id(9)
        print(u, '22222')
        UserDAO.update(8, username='zs')

        UserDAO.delete(7)
        # self.user_ctl.add(username='test')
        result = {"code": 0, "msg": "注册成功"}
        return result

    def put(self):
        """ put method """
        # self.user_ctl.update(id=4, username='test1')
        return 'put'

    def delete(self):
        """ delete method """
        self.chat.clear()
        # self.user_ctl.delete(id=1)
        return 'delete'


# class UserRegisterView(MethodView):
#     methods = ["GET", "POST", 'PUT', 'DELETE']
#
#     def __init__(self, *args, **kwargs):
#         self.logger = current_app.logger
#         self.chat = current_app.chat
#         super().__init__(*args, **kwargs)
#
#     def get(self):
#         self.logger.error('error')
#         self.logger.debug('debug')
#         self.logger.info('info')
#         message = request.args.get('message')
#         user = UserController.get_one('张森')
#         if not user:
#             user_id = UserController.insert(**{'username': '张森', 'age': 18})
#         else:
#             user_id = user.id
#         return {'user_id': user_id, 'message': message}
#
#         # self.chat.set_message({'role': 'system', 'content': '你是一个聊天机器人'})
#
#         # print('GPT TEST')
#         # self.chat.set_message({'role': 'user', 'content': message})
#         # try:
#         #     response = self.chat.get_response()
#         # except:
#         #     return 'time out'
#         # self.chat.set_message({'role': response.message.role, 'content': response.message.content})
#         # message = self.chat.get_all_message()
#         # MessageController.add(user_id, message)
#         # return response.message.content
#
#
#
#     def post(self):
#         # self.user_ctl.add(username='test')
#         result = {"code": 0, "msg": "注册成功"}
#         return result
#
#     def put(self):
#         # self.user_ctl.update(id=4, username='test1')
#         return 'put'
#
#     def delete(self):
#         self.chat.clear()
#         # self.user_ctl.delete(id=1)
#         return 'delete'
