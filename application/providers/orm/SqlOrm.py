from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from application.providers.orm.models import Base

class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            print("Database initialized ...")
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class SqlOrm(Singleton):
    def __init__(self):
        self.engine = create_engine("sqlite:///test.db")
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)
        
    
    def get_session(self) -> Session:
        return self.session