import os


class File:
    def __init__(self, filepath: str):
        self.__filepath = filepath
        self.__filename = os.path.basename(filepath)

    def __open(self, mode: str = 'r'):
        return open(self.__filepath, mode)

    @staticmethod
    def __close(file):
        file.close()

    def read(self):
        file = self.__open()
        content = file.read()
        self.__close(file)
        return content

    def readlines(self):
        file = self.__open()
        content = file.readlines()
        self.__close(file)
        return content

    def write(self, content: str):
        file = self.__open('w')
        file.write(content)
        self.__close(file)

    def writelines(self, content: list[str]):
        file = self.__open('w')
        file.writelines(content)
        self.__close(file)

    def append(self, content: str):
        file = self.__open('a')
        file.write(content)
        self.__close(file)

    def appendlines(self, content: list[str]):
        file = self.__open('a')
        file.writelines(content)
        self.__close(file)

    def get_filename(self):
        return self.__filename

    def get_filepath(self):
        return self.__filepath
