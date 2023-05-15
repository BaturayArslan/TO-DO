from flask import Flask,jsonify
from flask_jwt_extended import JWTManager

from application.controllers.api.ItemBluePrint import item_blueprint
from application.controllers.api.ListBluePrint import list_blueprint
from application.controllers.api.UserBluePrint import user_blueprint
from application.dto.request.AddUserRequest import AddUserRequest
from application.repositories.UserRepository import UserRepository
from application.use_cases.user.AddUserUseCase import AddUserUseCase
from application.providers.orm.SqlOrm import SqlOrm


def init():
	SqlOrm()

	user_repo = UserRepository()
	add_user_usecase = AddUserUseCase(user_repo)

	add_user_req = AddUserRequest("NormalTestUser","NormalTestUser",False)
	normal_user = add_user_usecase.process(add_user_req)


	add_user_req = AddUserRequest("PrivilegedTestUser","PrivilegedTestUser",True)
	privileged_user = add_user_usecase.process(add_user_req)

	print("Test Users Initialized...")
	print(f"NormalUser(id={normal_user.id}, username={normal_user.name}, password={normal_user.password})")
	print(f"PrivilegedUser(id={privileged_user.id}, username={privileged_user.name}, password={privileged_user.password})")


def create_app(test_config=None):
	app = Flask(__name__)
	
	if test_config:
		app.config.from_object("application.config.TestConfig")
	else:
		app.config.from_object("application.config.DevConfig")
	
	jwt = JWTManager(app)

	@jwt.expired_token_loader
	def my_expired_token_callback(jwt_token):
		return jsonify({"status": "error", "message": "Expired Token.","type":jwt_token['type']}), 402

	@jwt.invalid_token_loader
	def my_invalid_token_callback(message):
		return jsonify({"status": "error", "message": "Invalid Token."}), 402

	@jwt.unauthorized_loader
	def my_missing_token_callback(messge):
		return jsonify({"status": "error", "message": "Missing Token."}), 402

	app.register_blueprint(item_blueprint)
	app.register_blueprint(list_blueprint)
	app.register_blueprint(user_blueprint)

	init()

	return app	