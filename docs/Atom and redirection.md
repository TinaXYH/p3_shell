# Atom and redirection

## `Atom`

The content of the atom is either a string or a `Quoted` object

## `Redirection` (Base Class)
Constructor
```python
def __init__(self, filepath):
    self.filepath = filepath.get_content()
```

## `InputRedirection(Redirection)`
Creates an input interface using `InputInterface(mode='file', filepath=self.filepath)`

## `OutputRedirection(Redirection)` (Abstract class)
Provides `get_output_handle() -> OutputInterface` method

## Subclasses of `OutputRedirection`
Provides `set_content(content: str)` to assign value for `get_output_handle()`.