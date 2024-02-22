# Commands

## `Command` (Abstract Base Class)

### method

```python
@abstractmethod
def exec(self) -> str:
    pass
```

## `SequenceCommand(Command)`

### methods
Constructor:
```python
def __init__(self, left_call: CallCommand, right_call: CallCommand)
```

Override method
```python
def exec(self) -> str:
    return f"{self.__left.exec()}\n{self.__right.exec()}"
```

## `PipeCommand(Command)` (Empty Base Class)

## `SimplePipeCommand(PipeCommand)`

### methods
Constructor
```python
def __init__(self, left_call: CallCommand, right_call: CallCommand)
```

Override method
```python
def exec(self) -> str:
    stdin = InputInterface(self.__left.exec(), 'from_call')
    self.__right.add_stdin(stdin)
    return self.__right.exec()
```

## `RecursivePipeCommand(PipeCommand)`

### methods
Constructor
```python
def __init__(self, left_call: PipeCommand, right_call: CallCommand)
```

Override method is the same as `SimplePipeCommand`

## `CallCommand(Command)`

### methods
Constructor
```python
def __init__(self, appname: str, arg: Argument):
```

```python
def add_stdin(self, stdin: InputInterface):
    self.__arg.add_stdin(stdin)
```

Override method
```python
def exec(self) -> str:
    args, output_handle = self.__arg.get_arguments()
    self.__application = ApplicationFactory.get_application(self.__appname, args)
    self.__output = self.__application.eval()
    if output_handle:
        output_handle.write(self.__output)
    return '' if output_handle else self.__output
```