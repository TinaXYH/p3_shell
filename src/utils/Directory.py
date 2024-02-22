import os
from .File import File


class Directory:
    def __init__(self, path: str):
        self.__path = path
        self.__dirname = os.path.basename(path)
        self.__files = []
        self.__directories = []
        self.__update()

    def __update(self):
        with os.scandir(self.__path) as it:
            for entry in it:
                if entry.is_file():
                    self.__files.append(File(entry.path))
                elif entry.is_dir():
                    self.__directories.append(Directory(entry.path))

    def get_directories(self):
        return self.__directories

    def get_files(self):
        return self.__files

    def get_contents(self):
        contents = []
        contents.extend(self.__directories)
        contents.extend(self.__files)
        return contents

    def get_dirname(self):
        return self.__dirname

    def get_path(self):
        return self.__path
