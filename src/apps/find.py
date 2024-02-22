from glob import glob
from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import Directory, InputInterface, OutputInterface


class Find(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.contents = []
        self.pattern = None

    @staticmethod
    def is_legal_option(arg1, arg2):
        return arg1 == '-name' and Find.is_legal_path(arg2)

    @staticmethod
    def is_legal_path(arg):
        return len(arg) > 0 and arg[0] != '-'

    def is_legal_args(self):
        if len(self.args) not in [2, 3]:
            return False
        if len(self.args) == 2:
            return self.is_legal_option(self.args[0], self.args[1])
        else:
            return self.is_legal_option(self.args[1], self.args[2]) and self.is_legal_path(self.args[0])

    def eval(self) -> OutputInterface:
        if not self.is_legal_args():
            raise InvalidArgumentError(f"illegal arguments: {self.args}")
        if len(self.args) == 2:
            self.pattern = self.args[1]
            self.find(Directory('./'))
        else:
            self.pattern = self.args[2]
            self.find(Directory(self.args[0]))
        self.output_interface.set_content(self.contents)
        return self.output_interface

    def find(self, directory: Directory):
        for d in directory.get_directories():
            globbing = glob(self.pattern, root_dir=d.get_path())
            globbing.sort()
            self.contents.extend(globbing)
            self.find(d)
        f_globbing = glob(self.pattern, root_dir=directory.get_path())
        f_globbing.sort()
        self.contents.extend(f_globbing)
