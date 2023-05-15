from application.app import create_app 


# Temizlenecek Importlar
from datetime import date
from application.entities.TodoList import TodoList
from application.providers.orm.models import ListModel, ItemModel

from application.dto.request.UpdateListRequest import UpdateListRequest
from application.dto.request.GetListRequest import GetListRequest
from application.dto.request.AddListRequest import AddListRequest

from application.dto.request.UpdateItemRequest import UpdateItemRequest
from application.dto.request.GetItemRequest import GetItemRequest
from application.dto.request.AddItemRequest import AddItemRequest

from application.dto.request.GetUserRequest import GetUserRequest
from application.dto.request.AddUserRequest import AddUserRequest

from application.repositories.ListRepository import ListRepository
from application.repositories.ItemRepository import ItemRepository
from application.repositories.UserRepository import UserRepository

from application.use_cases.item.AddItemUseCase import AddItemUseCase
from application.use_cases.item.GetItemUseCase import GetItemUseCase
from application.use_cases.item.UpdateItemUseCase import UpdateItemUseCase

from application.use_cases.list.AddListUseCase import AddListUseCase
from application.use_cases.list.GetListUseCase import GetListUseCase
from application.use_cases.list.UpdateListUseCase import UpdateListUseCase

from application.use_cases.user.GetUserUseCase import GetUserUseCase
from application.use_cases.user.AddUserUseCase import AddUserUseCase

from application.entities.PrivilegedUser import PrivilegedUser
from application.entities.NormalUser import NormalUser

if __name__ == "__main__":
    app = create_app(True)

    # list_repo = ListRepository()
    # item_repo = ItemRepository()
    # user_repo = UserRepository()

    # add_item_usecase = AddItemUseCase(item_repo)
    # get_item_usecase = GetItemUseCase(item_repo)
    # update_item_usecase = UpdateItemUseCase(item_repo)

    # add_list_usecase = AddListUseCase(list_repo)
    # get_list_usecase = GetListUseCase(list_repo)
    # update_list_usecase = UpdateListUseCase(list_repo)

    # add_user_usecase = AddUserUseCase(user_repo)
    # get_user_usecase = GetUserUseCase(user_repo)

    # # Successfully add new list
    # add_list_req = AddListRequest(name= "My new List", deletion_date_str="12/02/1998")
    # todo_list = add_list_usecase.process(add_list_req)
    # print(todo_list)

    # # Successfully add new item to list
    # add_item_req = AddItemRequest(content="Make dinner", status=3, list_id=1)
    # todo_list = add_item_usecase.process(add_item_req)
    # print(todo_list)

    
    # get_item_req = GetItemRequest(1)
    # todo_item = get_item_usecase.process(get_item_req)
    # print(todo_item)

    # get_list_req = GetListRequest(1)
    # todo_list = get_list_usecase.process(get_list_req)
    # print(todo_list)


    # update_list_req = UpdateListRequest(id=1,name="My new new List",deletion_date_str="26/08/2023")
    # todo_list = update_list_usecase.process(update_list_req)
    # print(todo_list)
    
    # update_item_req = UpdateItemRequest(2,status=2,content="make cook and go shopping",deletion_date_str="16/05/2023")
    # todo = update_item_usecase.process(update_item_req)
    # print(todo)

    # add_user_req = AddUserRequest("baturay","hello world",True)
    # user = add_user_usecase.process(add_user_req)
    # print(isinstance(user, PrivilegedUser))
    # print(user.id)

    # get_user_req = GetUserRequest(id=1)
    # user = get_user_usecase.process(get_user_req)
    # print(user.name, user.password, user.id)


    app.run()