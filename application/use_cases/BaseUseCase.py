from abc import ABC, abstractmethod

class BaseUseCase(ABC):

    @abstractmethod
    def process(self, dto):
        ...

    