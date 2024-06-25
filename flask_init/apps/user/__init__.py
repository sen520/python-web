from apps import api
from apps.user.resource import ns as user_ns
# from .resource import UserRegisterView

# package_url = '/user/'
#
#
# def get_app_url(path):
#     return package_url + path
#
#
# app.add_url_rule(get_app_url('register'), view_func=UserRegisterView.as_view('register'))


api.add_namespace(user_ns)