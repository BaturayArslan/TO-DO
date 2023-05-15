from sqlalchemy import select
from typing import List

from application.repositories.BaseRepository import BaseRepository
from application.dto.request.GetUserRequest import GetUserRequest
from application.dto.request.AddUserRequest import AddUserRequest
from application.entities.BaseUser import BaseUser
from application.entities.NormalUser import NormalUser
from application.entities.PrivilegedUser import PrivilegedUser
from application.utils.utils import list_model_to_entity

from application.providers.orm.models import UserModel
from application.entities.TodoList import TodoList

class UserRepository(BaseRepository):

    def get(self, get_user_req: GetUserRequest) -> BaseUser:
        stmt = select(UserModel).where(UserModel.name == get_user_req.username and UserModel.password == get_user_req.password)
        user_model = self.session.scalars(stmt).one()
        if(user_model.privileged):
            return PrivilegedUser(id= user_model.id, name=user_model.name,password=user_model.password)
        
        return NormalUser(id= user_model.id, name=user_model.name, password=user_model.password)

    def insert(self, add_user_req: AddUserRequest) -> BaseUser:
        model = UserModel(
            name = add_user_req.name,
            password = add_user_req.password,
            privileged = add_user_req.privileged
        )

        self.session.add(model)
        self.session.commit()
        self.session.flush()
        self.session.refresh(model)
        
        if(add_user_req.privileged):
            return PrivilegedUser(id=model.id ,name=model.name,password=model.password)
        
        return NormalUser(id=model.id, name=model.name, password=model.password)
        
    def get_lists(self, user_id) -> List[TodoList]:
        stmt = select(UserModel).where(UserModel.id == user_id)
        user_model = self.session.scalars(stmt).one()

        return [list_model_to_entity(todo_model) for todo_model in user_model.lists]

