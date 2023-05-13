from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

from application.providers.orm.models import Base

class SqlOrm:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.engine = create_engine("sqlite:///test.db", echo=True)
        self.session = Session(self.engine)
        Base.metadata.create_all(self.engine)
        
    
    def get_session(self) -> Session:
        return self.session