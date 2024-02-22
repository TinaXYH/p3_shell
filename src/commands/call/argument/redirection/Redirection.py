from abc import ABC
from src.commands.call.argument.Atom import Atom
from ..ArgumentContent import ArgumentContent


class Redirection(ArgumentContent, ABC):
    def __init__(self, filepath: Atom):
        self.filepath = filepath
