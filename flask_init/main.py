from middleware import *
from settings import Config


if __name__ == '__main__':
    app.wsgi_app = middle(app.wsgi_app)
    app.run(port=Config.PORT, host=Config.HOST)

