from application.repositories.ItemRepository import ItemRepository
from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.UpdateItemRequest import UpdateItemRequest


class UpdateItemUseCase(BaseUseCase):
    def __init__(self, repo: ItemRepository):
        self.repo = repo
    
    def process(self, update_item_req: UpdateItemRequest):
        todo_item = self.repo.update(update_item_req)
        return todo_item
