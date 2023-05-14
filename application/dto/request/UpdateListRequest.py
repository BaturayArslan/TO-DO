from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class UpdateListRequest:
    name: str = None
    deletion_date_str: str = None
    deletion_date: date = field(init=False, repr=False)

    def __post_init__(self):
        self.__validate_name()
        self.__validate_deletion_date()
    
    def __validate_deletion_date(self):
        if self.deletion_date_str and type(self.deletion_date_str) != str:
            raise ValueError("deletion date must be string")
        
        if (self.deletion_date_str):
            try:
                self.deletion_date = datetime.strptime(self.deletion_date_str, "%d/%m/%Y").date()
            except Exception:
                raise ValueError("deletion_date data invalid format.Please provide with day/month/year format.")
            
    
    def __validate_name(self):
        if self.name and type(self.name) != str:
            raise ValueError("name data must be string.")
        
        if(len(self.name) > 30):
            raise ValueError("name data length must be less than 30.")
    
    