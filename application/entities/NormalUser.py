from application.entities.BaseUser import BaseUser

class NormalUser(BaseUser):
    def __init__(self, name: str, password: str,id=0):
        super().__init__(id,name, password)