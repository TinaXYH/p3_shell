from abc import ABC, abstractmethod


class ArgumentContent(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
