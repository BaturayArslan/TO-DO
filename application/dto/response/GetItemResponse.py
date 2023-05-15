from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Dict,Any,List

@dataclass
class GetItemResponse:
    id: int
    creation_date: str
    update_date: str
    deletion_date: str
    content: str
    status: int
    list_id: int
