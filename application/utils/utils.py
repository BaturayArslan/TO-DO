from dataclasses import asdict

from application.entities.TodoItem import TodoItem
from application.entities.TodoList import TodoList
from application.providers.orm.models import ListModel, ItemModel
from application.entities.ItemStatus import ItemStatus
from application.dto.response.GetListResponse import GetListResponse
from application.dto.response.GetItemResponse import GetItemResponse


def list_model_to_entity(model: ListModel) -> TodoList:
    todo_list = TodoList(
        id = model.id,
        name = model.name,
        creation_date= model.creation_date,
        deletion_time=model.deletion_date,
        update_date=model.update_date,
        comp_perc=model.completion_percentage
    )
    
    if (len(model.item_list) == 0):
        todo_list.item_list = []
    else:
        todo_list.item_list = [_item_model_to_entity(item_model) for item_model in model.item_list]
    
    for item in todo_list.item_list:
        item.set_list(todo_list)

    return todo_list



def _item_model_to_entity(model: ItemModel) -> TodoItem:
    todo_item = TodoItem(
        id=model.id,
        creation_date=model.creation_date,
        status=ItemStatus[model.status].value,
        content=model.content,
        deletion_time=model.deletion_date,
        update_date=model.update_date
    )
    return todo_item

def item_model_to_entity(model: ItemModel) -> TodoItem:
    todo_list = list_model_to_entity(model.list)
    for item in todo_list.item_list:
        if(item.ID == model.id):
            return item

def list_entity_to_model(list_entity:TodoList) -> ListModel:
    list_model = ListModel(
        name=list_entity.name,
        creation_date=list_entity.creation_date,
        deletion_date=list_entity.deletion_time,
        completion_percentage=list_entity.completion_percentage,
        update_date=list_entity.update_date,
        item_list = [item_entity_to_model(item_entity) for item_entity in list_entity.item_list]
    )

    return list_model

def item_entity_to_model(item_entity: TodoItem) -> ItemModel:
    model = ItemModel(
        creation_date=item_entity.creation_date,
        deletion_date=item_entity.deletion_time,
        update_date=item_entity.update_date,
        status=item_entity.status.name,
        content=item_entity.content
    )
    return model

def item_copy_to_model(item: TodoItem, model: ItemModel):
    model.update_date = item.update_date
    model.status = item.status.name
    model.content = item.content
    model.deletion_date = item.deletion_time
    model.creation_date = item.creation_date

def list_copy_to_model(list: TodoList, model: ListModel):
    model.update_date = list.update_date
    model.deletion_date = list.deletion_time
    model.completion_percentage = list.completion_percentage
    model.name = list.name
    model.creation_date = list.creation_date
    
    for item in list.item_list:
        for item_model in model.item_list:
            if (item.ID == item_model.id):
                item_copy_to_model(item, item_model)

def list_to_response(list: TodoList) -> GetListResponse:
    return GetListResponse(
        id=list.ID,
        creation_date= list.creation_date.strftime("%d/%m/%Y"),
        update_date=list.update_date.strftime("%d/%m/%Y"),
        deletion_date= list.deletion_time.strftime("%d/%m/%Y"),
        completion_percentage= list.completion_percentage,
        item_list= [ asdict(item_to_response(item)) for item in list.item_list ]
    )

def item_to_response(item: TodoItem) -> GetItemResponse:
    return GetItemResponse(
        id= item.ID,
        creation_date= item.creation_date.strftime("%d/%m/%Y"),
        update_date= item.update_date.strftime("%d/%m/%Y"),
        deletion_date= item.deletion_time.strftime("%d/%m/%Y"),
        content = item.content,
        status = item.status.value,
        list_id = item.list.ID,
    )