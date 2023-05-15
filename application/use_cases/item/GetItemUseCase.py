from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.GetItemRequest import GetItemRequest
from application.repositories.ItemRepository import ItemRepository

class GetItemUseCase(BaseUseCase):

    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def process(self, get_item_req: GetItemRequest):
        todo_item = self.repo.get(get_item_req)
        return todo_item