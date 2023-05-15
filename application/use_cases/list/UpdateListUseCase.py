from application.repositories.ListRepository import ListRepository
from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.UpdateListRequest import UpdateListRequest


class UpdateListUseCase(BaseUseCase):
    def __init__(self, repo: ListRepository):
        self.repo = repo
    
    def process(self, update_list_req: UpdateListRequest):
        todo_list = self.repo.update(update_list_req)
        return todo_list
