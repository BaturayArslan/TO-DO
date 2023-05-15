from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class AddItemRequest:
    content: str
    status: int
    list_id: int
    deletion_date_str: str = None
    deletion_date: date = field(init=False, repr=False,default=None)

    def __post_init__(self):
        self.__validate_content()
        self.__validate_deletion_date()
        self.__validate_status()
    
    def __validate_deletion_date(self):
        if self.deletion_date_str and type(self.deletion_date_str) != str:
            raise ValueError("deletion date must be string")
        
        if (self.deletion_date_str):
            try:
                self.deletion_date = datetime.strptime(self.deletion_date_str, "%d/%m/%Y").date()
            except Exception:
                raise ValueError("Invalid value for deletion_date data. Please provide valid data with day/month/year format.")
            
    
    def __validate_content(self):
        if type(self.content) != str:
            raise ValueError("content data must be string.")
        
        if (len(self.content) > 100):
            raise ValueError("Cotent Length must be less than 100.")

    def __validate_status(self):
        if type(self.status) != int:
            raise ValueError("status data must be integer")
        
        if(self.status < 1 or self.status > 3):
            raise ValueError("Status data must be in between 1 and 3. 1=TODO, 2=DOING, 3= DONE")