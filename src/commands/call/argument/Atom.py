from src.commands.call.argument.quoted.Quoted import Quoted
from .ArgumentContent import ArgumentContent


class Atom(ArgumentContent):
    def __init__(self, content: Quoted | str):
        self.content = content

    def accept(self, visitor):
        return visitor.visit_atom(self)
