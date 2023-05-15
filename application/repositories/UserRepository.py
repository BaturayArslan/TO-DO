from sqlalchemy import select

from application.repositories.BaseRepository import BaseRepository
from application.dto.request.GetUserRequest import GetUserRequest
from application.dto.request.AddUserRequest import AddUserRequest
from application.entities.BaseUser import BaseUser
from application.entities.NormalUser import NormalUser
from application.entities.PrivilegedUser import PrivilegedUser
from application.providers.orm.models import UserModel


class UserRepository(BaseRepository):

    def get(self, get_user_req: GetUserRequest) -> BaseUser:
        id = get_user_req.id
        stmt = select(UserModel).where(UserModel.id == get_user_req.id)
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
        
        