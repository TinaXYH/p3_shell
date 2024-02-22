from src.commands.call.argument.quoted.Quoted import Quoted
from src.commands.call.argument.quoted.BackQuoted import BackQuoted


class DoubleQuoted(Quoted):
    def __init__(self, content: list[BackQuoted | str]):
        self.content = content

    def accept(self, visitor):
        return visitor.visit_double_quoted(self)
