from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class AddUserRequest:
    name: str
    password: str
    privileged: bool = False
