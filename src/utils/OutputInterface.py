from src.utils.File import File


class OutputInterface:
    def __init__(self, mode='stdout', filepath=None):
        """
        possible modes:
            'stdout': normal output
            'file_overwrite': overwrite the file
            'file_append': append content to the file
        """
        self.__mode = mode
        self.__content: list[str] = []
        self.__file = None
        if filepath:
            self.__file = File(filepath)

    def set_content(self, content: list[str]):
        self.__content.extend(content)
        if self.__file:
            if 'overwrite' in self.__mode:
                self.__file.writelines(self.__content)
            elif 'append' in self.__mode:
                self.__file.appendlines(self.__content)
            self.__content = []

    @staticmethod
    def concatenate(oi1, oi2):
        oi = OutputInterface()
        oi.set_content(oi1.capture_content())
        oi.set_content(oi2.capture_content())
        return oi

    def capture_content(self):
        content = self.__content
        self.__content = []
        return content
