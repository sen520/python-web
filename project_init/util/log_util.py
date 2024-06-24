import os
import logging
from concurrent_log_handler import ConcurrentRotatingFileHandler


# 获取当前绝对路径
def get_cwd():
    return os.path.dirname(os.path.abspath(__file__))


def log_config(file_path=get_cwd(), file_name='flask.log', maxBytes=1024 * 1024 * 100, backupCount=100,
               LOG_LEVEL=logging.DEBUG):
    # 设置日志的的登记
    # print(LOG_LEVEL, maxBytes, backupCount)
    logging.basicConfig(level=LOG_LEVEL)
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # 日志输出目录
    log_path = os.path.join(file_path, file_name)
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    file_log_handler = ConcurrentRotatingFileHandler(log_path, encoding='UTF-8', maxBytes=maxBytes, backupCount=backupCount)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(filename)s]: %(lineno)s - %(funcName)s - %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().handlers.clear()
    logging.getLogger().addHandler(file_log_handler)

    console = logging.StreamHandler()
    console.setLevel(LOG_LEVEL)
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
