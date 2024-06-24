from apps import app
from .resource import UserRegisterView

package_url = '/user/'


def get_app_url(path):
    return package_url + path


app.add_url_rule(get_app_url('register'), view_func=UserRegisterView.as_view('register'))
