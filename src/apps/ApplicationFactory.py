from . import *
from src.exceptions import CommandNotFoundError
from src.utils import *
from ..UnsafeDecorator import UnsafeDecorator

apps = {
    'cat': Cat,
    "cd": Cd,
    "cut": Cut,
    "echo": Echo,
    "find": Find,
    "grep": Grep,
    "head": Head,
    "ls": Ls,
    "pwd": Pwd,
    "sort": Sort,
    "tail": Tail,
    "uniq": Uniq
}


class ApplicationFactory:

    @staticmethod
    def get_application(name: str, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        is_unsafe = False
        if len(name) > 1 and name[0] == '_':
            name = name[1:]
            is_unsafe = True
        app = apps[name]
        if app is None:
            raise CommandNotFoundError
        app_object = app(args, input_interface, output_interface)
        if is_unsafe:
            app_object = UnsafeDecorator(app_object)
        return app_object
