from application.entities.TodoItem import TodoItem
from application.entities.TodoList import TodoList
from application.providers.orm.models import ListModel, ItemModel
from application.entities.ItemStatus import ItemStatus


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
        deletion_date=model.deletion_date,
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