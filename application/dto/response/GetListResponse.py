from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict,Any,List

@dataclass
class GetListResponse:
    id: int
    name: str
    creation_date: str
    update_date: str
    deletion_date: str
    completion_percentage: int
    item_list: List[Any]

        
    
    