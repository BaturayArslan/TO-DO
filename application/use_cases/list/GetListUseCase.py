
from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.GetListRequest import GetListRequest
from application.repositories.ListRepository import ListRepository

class GetListUseCase(BaseUseCase):

    def __init__(self, repo: ListRepository):
        self.repo = repo

    def process(self, get_list_req: GetListRequest):
        todo_list = self.repo.get(get_list_req)
        return todo_list