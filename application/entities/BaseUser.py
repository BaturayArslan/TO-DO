from abc import ABC, abstractmethod

class BaseUser(ABC):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password