from src.commands.call.argument.quoted.Quoted import Quoted


class SingleQuoted(Quoted):
    def __init__(self, content: str):
        self.content = content

    def accept(self, visitor):
        return visitor.visit_single_quoted(self)
