from src.commands.call.argument.quoted.Quoted import Quoted


class BackQuoted(Quoted):
    def __init__(self, content: str):
        self.content = content

    def accept(self, visitor):
        return visitor.visit_back_quoted(self)
