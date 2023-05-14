from sqlalchemy import select
from dataclasses import fields, asdict

from application.repositories.BaseRepository import BaseRepository
from application.providers.orm.models import ListModel, ItemModel
from application.dto.request.UpdateListRequest import UpdateListRequest
from application.entities.TodoList import TodoList
from application.utils.utils import (
    item_model_to_entity, 
    list_model_to_entity,
    item_entity_to_model,
    list_entity_to_model
)

class ListRepository(BaseRepository):

    def get(self, id: int) -> TodoList:
        stmt = select(ListModel).where(ListModel.id.in_([id]))
        list_model = self.session.scalars(stmt).one()
        return list_model_to_entity(list_model)
    
    def insert(self,list_entity: TodoList) -> None:
        model = list_entity_to_model(list_entity=list_entity)
        with self.session:
            self.session.add_all([model])
            self.session.commit()
    
    def update(self, id, update_room_req: UpdateListRequest) -> None:
        model = self.get(id=id)
        for field, value in asdict(update_room_req).items():
            if(value):
                setattr(model, field, value)
        self.session.commit()
    
    def delete(self, id):
        raise NotImplementedError()