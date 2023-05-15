from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.AddUserRequest import AddUserRequest
from application.repositories.UserRepository import UserRepository

class AddUserUseCase(BaseUseCase):

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def process(self, add_user_req: AddUserRequest):
        user = self.repo.insert(add_user_req)
        return user