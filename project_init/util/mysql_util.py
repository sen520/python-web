import random
from flask_sqlalchemy import SQLAlchemy, SignallingSession, get_state
from sqlalchemy.sql.dml import UpdateBase
from sqlalchemy import orm
import logging


class RoutingSession(SignallingSession):
    def __init__(self, *args, **kwargs):
        self.logger = logging.Logger('flask')
        self.logger.setLevel(logging.DEBUG)
        super(RoutingSession, self).__init__(*args, **kwargs)

    def get_bind(self, mapper=None, clause=None):
        state = get_state(self.app)
        if mapper is not None:
            try:
                persist_selectable = mapper.persist_selectable
            except AttributeError:
                persist_selectable = mapper.mapped_table
            info = getattr(persist_selectable, 'info', {})
            bind_key = info.get('bind_key')
            if bind_key is not None:
                return state.db.get_engine(self.app, bind=bind_key)

        if self._flushing or isinstance(clause, UpdateBase):
            self.logger.warning('写更新删除, 访问主库')
            return state.db.get_engine(self.app, bind='master')
        else:
            slave_key = random.choice(['slave1', 'slave2'])
            self.logger.warning('访问从库: {}'.format(slave_key))
            return state.db.get_engine(self.app, bind=slave_key)


class RoutingSQLAlchemy(SQLAlchemy):
    def create_session(self, options):
        return orm.sessionmaker(class_=RoutingSession, db=self, **options)
