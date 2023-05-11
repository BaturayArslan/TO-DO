from application.entities.BaseUser import BaseUser

class PrivilegedUser(BaseUser):
    def __init__(self, name: str, password: str):
        super().__init__(name, password)