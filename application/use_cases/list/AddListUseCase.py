from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.AddListRequest import AddListRequest
from application.repositories.ListRepository import ListRepository

class AddListUseCase(BaseUseCase):

    def __init__(self, repo: ListRepository):
        self.repo = repo

    def process(self, add_list_req: AddListRequest):
        todo_list = self.repo.insert(add_list_req)
        return todo_list