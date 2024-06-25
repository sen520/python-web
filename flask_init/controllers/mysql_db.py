from models.mysql_model import User, db


class UserDAO:

    @classmethod
    def get_all(cls):
        return User.query.all()

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()

    @classmethod
    def add(cls, **kwargs):
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def update(cls, id, **kwargs):
        user = User.query.filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return 'success'

    @classmethod
    def delete(cls, id):
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return 'success'


