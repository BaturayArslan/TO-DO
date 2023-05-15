from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.GetUserRequest import GetUserRequest
from application.repositories.UserRepository import UserRepository

class GetListsUseCase(BaseUseCase):

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def process(self, user_id: int):
        todo_lists = self.repo.get_lists(user_id)
        return todo_lists