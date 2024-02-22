from . import OutputInterface
from .File import File
from sys import stdin


class InputInterface:
    def __init__(self, mode: str = 'stdin', filepath=None):
        """
        possible modes:
            'stdin': read from stdin
            'from_output': pipe redirected output
            'file': input redirection
        """
        self.__mode = mode
        self.__file = None
        self.__raw_content: list[str] = []
        if filepath:
            self.__file = File(filepath)

    def from_output(self, oi: OutputInterface):
        self.__raw_content = oi.capture_content()
        self.__mode = 'from_output'

    def read(self):
        match self.__mode:
            case 'stdin':
                return stdin.read()
            case 'file':
                return self.__file.read()
            case 'from_output':
                return "".join(self.__raw_content)

    def readlines(self):
        match self.__mode:
            case 'stdin':
                return stdin.readlines()
            case 'file':
                return self.__file.readlines()
            case 'from_output':
                return self.__raw_content
