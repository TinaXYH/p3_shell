from src.apps.Application import Application
from src.exceptions import *
from src.utils import *
import re
from glob import glob


class Grep(Application):
    """
    Searches for lines containing a match to the specified pattern.
    The output of the command is the list of lines.
    Each line is printed followed by a newline.
    """

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.contents = []

    def search_content(self, content, filename: str = None):
        prefix = f"{filename}:" if filename else ""
        for line in content:
            if re.search(self.args[0], line):
                self.contents.append(f"{prefix}{line}")

    def eval(self):
        no_file_name = False
        match len(self.args):
            case 0:
                raise InvalidArgumentError("missing pattern")
            case 1:
                content = self.input_interface.readlines()
                self.search_content(content)
            case _:
                args = self.args[1:]
                for arg in args:
                    globbing = glob(arg)
                    if len(globbing) == 0:
                        raise InvalidArgumentError("FileNotFound")
                    globbing.sort()
                    files = list(map(lambda fn: File(fn), globbing))
                    if len(args) == 1 and len(files) == 1:
                        no_file_name = True
                    for file in files:
                        content = file.readlines()
                        if no_file_name:
                            self.search_content(content)
                        else:
                            self.search_content(content, file.get_filepath())
        self.output_interface.set_content(self.contents)
        return self.output_interface
