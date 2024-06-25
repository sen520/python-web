class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/mytest'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 处理告警
    SQLALCHEMY_ECHO = True  # 用于sql调试
    SQLALCHEMY_BINDS = {
        'master': 'mysql+pymysql://root:123456@localhost:3306/mytest',
        'slave1': 'mysql+pymysql://root:123456@localhost:3306/mytest',
        'slave2': 'mysql+pymysql://root:123456@localhost:3306/mytest',
    }

    DB_DIR = 'db'
    DEBUG = True

    LOG_PATH = 'log'
    LOG_NAME = 'flask.log'
    LOG_SIZE = 10  # 单位MB
    LOG_COUNT = 10
    LOG_LEVEL = 'DEBUG'

    HOST = '0.0.0.0'
    PORT = 8000

    GPT_API_KEY = ''
    GPT_MODEL = 'gpt-3.5-turbo'

    AES_SALT = '12345678123456781234567812345678'
    JWT_SALT = '12345678123456781234567812345678'
