from application.entities.BaseUser import BaseUser

class PrivilegedUser(BaseUser):
    def __init__(self, name: str, password: str,id=0):
        super().__init__(id,name, password)