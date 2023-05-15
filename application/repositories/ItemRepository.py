from sqlalchemy import select
from datetime import date
from dataclasses import asdict

from application.dto.request.GetItemRequest import GetItemRequest
from application.dto.request.AddItemRequest import AddItemRequest
from application.dto.request.UpdateItemRequest import UpdateItemRequest
from application.repositories.BaseRepository import BaseRepository
from application.entities.TodoItem import TodoItem
from application.entities.TodoList import TodoList
from application.providers.orm.models import ItemModel,ListModel
from application.entities.ItemStatus import ItemStatus
from application.utils.utils import (
    item_model_to_entity, 
    list_model_to_entity,
    item_entity_to_model,
    list_entity_to_model,
    list_copy_to_model,
    item_copy_to_model
)

class ItemRepository(BaseRepository):
    def get(self, get_item_request: GetItemRequest) -> TodoItem:
        id = get_item_request.id
        stmt = select(ItemModel).where(ItemModel.id.in_([id]))
        item_model = self.session.scalars(stmt).one()
        return item_model_to_entity(item_model)
    
    def insert(self, add_item_request: AddItemRequest) -> TodoList:

        stmt = select(ListModel).where(ListModel.id == add_item_request.list_id )
        model = self.session.scalars(stmt).one()
        todo_list = list_model_to_entity(model)

        todo_item = TodoItem(
            creation_date = date.today(),
            content = add_item_request.content,
            status = ItemStatus(add_item_request.status),
            deletion_time = add_item_request.deletion_date,
            list=todo_list,          
        )

        todo_list.add_item(todo_item)
        list_copy_to_model(todo_list, model)
        item_model = item_entity_to_model(todo_item)
        model.item_list.append(item_model)

        self.session.commit()
        self.session.flush()
        self.session.refresh(model)

        return list_model_to_entity(model)

    def update(self, update_item_req: UpdateItemRequest) -> TodoItem:

        stmt = select(ItemModel).where(ItemModel.id == update_item_req.id )
        model = self.session.scalars(stmt).one()
        todo_list = list_model_to_entity(model.list)
        todo_list.update_item(model.id,  asdict(update_item_req))

        list_copy_to_model(todo_list, model.list)
        
        self.session.commit()