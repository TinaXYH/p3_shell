from .ArgumentContent import ArgumentContent


class Argument:
    def __init__(self):
        self.contents: list[ArgumentContent] = []

    def add_content(self, content: ArgumentContent):
        self.contents.append(content)

    def accept(self, visitor):
        return visitor.visit_argument(self)
