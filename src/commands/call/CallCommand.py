from src.commands.call.argument.Argument import Argument
from src.commands.Command import Command


class CallCommand(Command):
    def __init__(self, appname: str, arg: Argument):
        self.appname = appname
        self.arg = arg  # arg may have nothing inside

    def accept(self, visitor):
        return visitor.visit_call(self)
