from abc import ABC, abstractmethod


class Quoted(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass
