from flask import Blueprint,request,jsonify
from dataclasses import asdict

from application.dto.request.AddListRequest import AddListRequest
from application.dto.request.GetListRequest import GetListRequest
from application.dto.request.AddListRequest import AddListRequest
from application.dto.request.UpdateListRequest import UpdateListRequest
from application.repositories.ListRepository import ListRepository
from application.use_cases.list.GetListUseCase import GetListUseCase
from application.use_cases.list.AddListUseCase import AddListUseCase
from application.use_cases.list.UpdateListUseCase import UpdateListUseCase
from application.utils.utils import list_to_response

list_blueprint = Blueprint("list_blueprint", __name__,url_defaults="/list")


@list_blueprint.route("/get",methods=["POST"])
def get_list():
    try:
        get_list_req = GetListRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    list_repo = ListRepository()
    get_list_usecase = GetListUseCase(list_repo)
    todo_list = get_list_usecase.process(get_list_req)
    get_list_response = list_to_response(todo_list)

    return jsonify(asdict(get_list_response))

@list_blueprint.route("/create", methods=["POST"])
def create_list():
    try:
        add_list_req = AddListRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    list_repo = ListRepository()
    add_list_usecase = AddListUseCase(list_repo)
    todo_list = add_list_usecase.process(add_list_req)
    list_response = list_to_response(todo_list)

    return jsonify(asdict(list_response))

@list_blueprint.route("/update", methods=["POST"])
def update_list():
    try:
        update_list_req = UpdateListUseCase(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")

    list_repo = ListRepository()
    update_list_usecase = UpdateListUseCase(list_repo)
    todo_list = update_list_usecase.process(update_list_req)

    list_response = list_to_response(todo_list)

    return jsonify(asdict(list_response))
