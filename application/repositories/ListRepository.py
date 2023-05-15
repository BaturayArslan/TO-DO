from sqlalchemy import select
from dataclasses import fields, asdict
from datetime import date

from application.repositories.BaseRepository import BaseRepository
from application.providers.orm.models import ListModel, ItemModel
from application.dto.request.UpdateListRequest import UpdateListRequest
from application.entities.TodoList import TodoList
from application.dto.request.GetListRequest import GetListRequest
from application.dto.request.AddListRequest import AddListRequest
from application.utils.utils import (
    item_model_to_entity, 
    list_model_to_entity,
    item_entity_to_model,
    list_entity_to_model
)

class ListRepository(BaseRepository):

    def get(self, get_list_req: GetListRequest) -> TodoList:
        id = get_list_req.id
        stmt = select(ListModel).where(ListModel.id.in_([id]))
        list_model = self.session.scalars(stmt).one()
        return list_model_to_entity(list_model)
    
    def insert(self,add_list_request: AddListRequest) -> TodoList:
        model = ListModel(
            name=add_list_request.name,
            deletion_date=add_list_request.deletion_date,
            creation_date=date.today(),
            completion_percentage=0,
        )
        self.session.add(model)
        self.session.commit()
        self.session.flush()
        self.session.refresh(model)
        
        return list_model_to_entity(model)
    
    def update(self, id, update_list_req: UpdateListRequest) -> TodoList:
        stmt = select(ListModel).where(ListModel.id == update_list_req.id )
        model = self.session.scalars(stmt).one()
        todo_list = list_model_to_entity(model)

        values = {key: value for key, value in asdict(update_list_req).items() if value is not None}
        todo_list.update_list(values)

        model.name = todo_list.name
        model.deletion_date = todo_list.delete_item
        model.update_date = todo_list.update_date

        self.session.commit()

        return todo_list
    
    def delete(self, id):
        raise NotImplementedError()