# Argument

`ArgumentContent` is an abstract class and doesn't have any methods.  
The contents of an argument are in a list of `ArgumentContent` objects.   
After parsing, the contents will be classified into 3 different categories: string, from an input interface or an output
redirection.

### Parsing
When the `Argument` class is parsing its contents, it will check if the output redirection is at the end of the argument
and there is only one output redirection. Otherwise, it throws an `InvalidArgumentError`.

### `get_arguments()` method
`get_arguments()` returns a tuple containing a list of input interfaces and strings, and an output interface for output
redirection.