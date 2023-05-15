from dataclasses import dataclass, field
from datetime import date, datetime

@dataclass
class UpdateItemRequest:
    id: int
    content: str = None
    status: int = None
    deletion_date_str: str = None
    deletion_date: date = field(init=False, repr=False)

    def __post_init__(self):
        self.__validate_content()
        self.__validate_deletion_date()
        self.__validate_id()
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
        if self.content and type(self.content) != str:
            raise ValueError("content data must be string.")
        
        if(self.content and len(self.content) > 100):
            raise ValueError("content data length must be less than 100.")


    def __validate_status(self):
        if type(self.id) != int:
            raise ValueError("status data must be integer")

        if(self.status < 1 or self.status > 3):
            raise ValueError("status code must be in between 1 and 3. 1=TODO, 2=DOING, 3=DONE.")
        
    def __validate_id(self):
        if type(self.id) != int:
            raise ValueError("id data must be integer")