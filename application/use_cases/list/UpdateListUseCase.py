

from application.repositories.ListRepository import ListRepository
from application.use_cases.BaseUseCase import BaseUseCase
from application.dto.request.UpdateRoomRequest import UpdateRoomRequest


class UpdateListUseCase(BaseUseCase):
    def __init__(self, repo: ListRepository):
        ...
    
    def process(self, update_list_req:UpdateRoomRequest):
        ... 
