# Utils

## `File`

### methods

#### Constructor
```python
def __init__(self, filepath: str)
```

#### Read file
```python
read() # returns the whole file
readlines() # returns the whole file in a list of lines
```

#### Write file
```python
write(content: str) # write content into the filepath provided
writelines(content: list[str])
append(content: str)
appendlines(content: list[str])
```

## `Directory`

### methods

#### Constructor
```python
def __init__(self, path: str)
```

#### Get folder content
```python
get_directories() -> list[Directory]
get_get_files() -> list[File]
```

## `InputInterface`

### methods
Constructor
```python
def __init__(self, content: str = '', mode: str = 'stdin', filepath: str = ''):
    self.__content = None
    if mode == 'file':
        self.__read_from_file(filepath)
    elif mode == 'from_call':
        self.__content = content
    elif mode == 'stdin':
        self.__read_from_stdin()
```

Get content
```python
def read(self):
    return self.__content
```

## `OutputInterface`

### methods
Constructor
```python
def __init__(self, content: str, mode: str = 'stdout', filepath: str = ''):
    self.__mode = mode
    self.__filepath = filepath
    self.__content = content
```

Write content
```python
def write(self, mode: str = 'w'):
    if self.__mode == 'stdout':
        self.__write_to_stdout()
    elif self.__mode == 'file':
        self.__write_to_file(mode)

def __write_to_file(self, mode: str):
    file = File(self.__filepath)
    if mode == 'w':
        file.write(self.__content)
    elif mode == 'a':
        file.append(self.__content)
```
