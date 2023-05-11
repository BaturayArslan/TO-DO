from abc import ABC, abstractmethod

class BaseUser(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password