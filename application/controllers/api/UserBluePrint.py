from flask import Blueprint,request,jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required,get_jwt
from dataclasses import asdict

from application.dto.request.AddUserRequest import AddUserRequest
from application.dto.request.GetUserRequest import GetUserRequest
from application.repositories.UserRepository import UserRepository
from application.repositories.ListRepository import ListRepository
from application.use_cases.user.GetUserUseCase import GetUserUseCase
from application.use_cases.user.AddUserUseCase import AddUserUseCase
from application.use_cases.user.GetListsUseCase import GetListsUseCase
from application.use_cases.list.GetAllListsUseCase import GetAllListsUseCase
from application.utils.utils import list_to_response
from application.entities.NormalUser import NormalUser
from application.entities.PrivilegedUser import PrivilegedUser

user_blueprint = Blueprint("user_blueprint", __name__, url_prefix="/user")


@user_blueprint.route("/get_token",methods=["POST"])
def get_token():
    try:
        get_user_req = GetUserRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    user_repo = UserRepository()
    get_user_usecase = GetUserUseCase(user_repo)
    user = get_user_usecase.process(get_user_req)

    access_token = None
    if(isinstance(user,PrivilegedUser)):
        access_token = create_access_token(identity=user.id,additional_claims={"user_type": "privileged"})
        return jsonify(access_token=access_token)
    
    access_token = create_access_token(identity=user.id, additional_claims={"user_type": "normal"})
    return jsonify(access_token=access_token)


@user_blueprint.route("/create", methods=["POST"])
def create_user():
    try:
        add_user_req = AddUserRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    user_repo = UserRepository()
    add_user_usecase = AddUserUseCase(user_repo)
    user = add_user_usecase.process(add_user_req)

    return jsonify(asdict(user))

@user_blueprint.route("/get_lists",methods=["POST"])
@jwt_required()
def get_lists():
    id = get_jwt_identity()
    user_repo = UserRepository()
    get_lists_usecase = GetListsUseCase(user_repo)
    todo_lists = get_lists_usecase.process(id)

    todo_lists_response = [list_to_response(todo_list) for todo_list in todo_lists]

    return jsonify([asdict(response_obj) for response_obj in todo_lists_response])


@user_blueprint.route("/get_all_lists",methods=["POST"])
@jwt_required
def get_all_lists():
    is_privileged = True if get_jwt()["type"] == "privileged" else False
    if(not is_privileged):
        return "Access Denied,", 402

    list_repo = ListRepository()
    get_all_list_usecase = GetAllListsUseCase()
    todo_lists = get_all_list_usecase.process()

    todo_lists_response = [list_to_response(todo_list) for todo_list in todo_lists]

    return jsonify([asdict(response_obj) for response_obj in todo_lists_response])