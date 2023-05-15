from flask import Blueprint,request,jsonify
from dataclasses import asdict

from application.dto.request.AddItemRequest import AddItemRequest
from application.dto.request.GetItemRequest import GetItemRequest
from application.dto.request.AddItemRequest import AddItemRequest
from application.dto.request.UpdateItemRequest import UpdateItemRequest
from application.repositories.ItemRepository import ItemRepository
from application.use_cases.item.GetItemUseCase import GetItemUseCase
from application.use_cases.item.AddItemUseCase import AddItemUseCase
from application.use_cases.item.UpdateItemUseCase import UpdateItemUseCase
from application.utils.utils import list_to_response, item_to_response

item_blueprint = Blueprint("item_blueprint", __name__,url_defaults="/item")


@item_blueprint.route("/get",methods=["POST"])
def get_item():
    try:
        get_item_req = GetItemRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    item_repo = ItemRepository()
    get_item_usecase = GetItemUseCase(item_repo)
    todo_Item = get_item_usecase.process(get_item_req)
    get_item_response = item_to_response(todo_Item)

    return jsonify(asdict(get_item_response))

@item_blueprint.route("/create", methods=["POST"])
def create_item():
    try:
        add_item_req = AddItemRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    item_repo = ItemRepository()
    add_item_usecase = AddItemUseCase(item_repo)
    todo_list = add_item_usecase.process(add_item_req)
    list_response = list_to_response(todo_list)

    return jsonify(asdict(list_response))

@item_blueprint.route("/update", methods=["POST"])
def update_item():
    try:
        update_item_req = UpdateItemRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")

    item_repo = ItemRepository()
    update_item_usecase = UpdateItemUseCase(item_repo)
    todo_list = update_item_usecase.process(update_item_req)

    list_response = list_to_response(todo_list)

    return jsonify(asdict(list_response))
