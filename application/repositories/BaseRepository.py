from abc import ABC, abstractmethod

from application.providers.orm.SqlOrm import SqlOrm
from application.dto.request.GetListRequest import GetListRequest
from application.dto.request.AddListRequest import AddListRequest
from application.dto.request.UpdateListRequest import UpdateListRequest


class BaseRepository:
    def __init__(self):
        self.session = SqlOrm().get_session()
    
    @abstractmethod
    def get(self, get_req):
        ...
    
    @abstractmethod
    def insert(self, add_req ):
        ...

    @abstractmethod
    def update(self, update_req):
        ...
    
    @abstractmethod
    def delete(self, id):
        ...