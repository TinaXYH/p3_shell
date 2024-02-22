from src.apps.Application import Application
from src.utils import InputInterface, OutputInterface


class Echo(Application):
    """
    Prints its arguments separated by spaces and followed by a newline to stdout
    """

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.content = " "
        
    def eval(self) -> OutputInterface:
        self.output_interface.set_content([self.content.join(self.args) + '\n'])
        return self.output_interface
