from abc import ABC, abstractmethod

from src.utils import *


class Application(ABC):
    """Application interface

    Attributes
    ----------
    args : list[str]
        List of arguments passed to the application

    Methods
    -------
    eval() -> OutputInterface
        Evaluates the application
        The output of the application is returned as a string
    """
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        """Constructor

        Parameters
        ----------
        args: list[str]
            List of arguments
        """
        self.args = args
        self.input_interface = input_interface
        self.output_interface = output_interface

    @abstractmethod
    def eval(self) -> OutputInterface:
        """Evaluates the application. The output of the application is returned as a string.
        If the arguments are invalid, an InvalidArgumentError is raised.
        Returns
        -------
        OutputInterface
            Output of the application
        """
        pass
