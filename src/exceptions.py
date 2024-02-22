class InvalidArgumentError(Exception):
    def __init__(self, message):
        super().__init__(message)


class IllegalCommandError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CommandNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)
