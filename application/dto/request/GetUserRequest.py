from dataclasses import dataclass


@dataclass
class GetUserRequest:
    id: int

    def __post_init__(self):
        self.__validate_id()

    def __validate_id(self):
        if type(self.id) != int:
            raise ValueError("id data must be integer")
        
  