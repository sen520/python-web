from sqlalchemy import create_engine

from models.mysql_model import User, db
from settings import Config


class MainSqlUtil():
    """自定义连接执行sql，主要避免通过db.session.execute使用的是从库数据库"""
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=Config.SQLALCHEMY_ECHO)

    @classmethod
    def execute_query(cls, sql, params=None):
        with cls.engine.connect() as conn:
            result = conn.execute(sql, params).fetchall()
        return [row._asdict() for row in result]

    @classmethod
    def execute(cls, sql, params=None):
        with cls.engine.connect() as conn:
            conn.execute(sql, params)


class UserDAO:

    @classmethod
    def get_all(cls):
        # 从库
        return [u.__json__() for u in User.query.all()]

    @classmethod
    def get_by_id(cls, id):
        # 从库
        user = User.query.filter_by(id=id).first()
        return user.__json__() if user else None

    @classmethod
    def add(cls, **kwargs):
        # 主库
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update(cls, id, **kwargs):
        # 主库
        user = User.query.filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return 'success'

    @classmethod
    def delete(cls, id):
        # 主库
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return 'success'
