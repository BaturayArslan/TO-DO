from abc import ABC, abstractmethod

from application.providers.orm.SqlOrm import SqlOrm


class BaseRepository:
    def __init__(self):
        self.session = SqlOrm().get_session()
    
    @abstractmethod
    def get(self, id: int):
        ...
    
    @abstractmethod
    def insert(self, model):
        ...

    @abstractmethod
    def update(self, id, info):
        ...
    
    @abstractmethod
    def delete(self, id):
        ...