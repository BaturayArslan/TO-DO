from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.AddItemRequest import AddItemRequest
from application.repositories.ItemRepository import ItemRepository

class AddItemUseCase(BaseUseCase):

    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def process(self, add_item_req: AddItemRequest):
        todo_list = self.repo.insert(add_item_req)
        return todo_list
