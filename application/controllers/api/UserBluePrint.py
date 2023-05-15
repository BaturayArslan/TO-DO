from flask import Blueprint,request,jsonify
from dataclasses import asdict

from application.dto.request.AddUserRequest import AddUserRequest
from application.dto.request.GetUserRequest import GetUserRequest
from application.repositories.UserRepository import UserRepository
from application.use_cases.user.GetUserUseCase import GetUserUseCase
from application.use_cases.user.AddUserUseCase import AddUserUseCase

user_blueprint = Blueprint("user_blueprint", __name__,url_defaults="/user")


@user_blueprint.route("/get",methods=["POST"])
def get_user():
    try:
        get_user_req = GetUserRequest(**request.json)
    except Exception as e:
        raise ValueError("Invalid Input")
    
    user_repo = UserRepository()
    get_user_usecase = GetUserUseCase(user_repo)
    user = get_user_usecase.process(get_user_req)

    return jsonify(asdict(user))

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