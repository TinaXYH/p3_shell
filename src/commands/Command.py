from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
