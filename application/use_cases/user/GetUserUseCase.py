from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.GetUserRequest import GetUserRequest
from application.repositories.UserRepository import UserRepository

class GetUserUseCase(BaseUseCase):

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def process(self, get_user_req: GetUserRequest):
        user = self.repo.get(get_user_req)
        return user