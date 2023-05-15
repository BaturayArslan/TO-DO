from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.GetListRequest import GetListRequest
from application.repositories.ListRepository import ListRepository

class GetAllListsUseCase(BaseUseCase):

    def __init__(self, repo: ListRepository):
        self.repo = repo

    def process(self):
        todo_lists = self.repo.get_all()
        return todo_lists