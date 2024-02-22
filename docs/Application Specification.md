Application interface
=====================

Attributes
----------
`args : list[str]`  
>List of arguments passed to the application

Methods
-------
`eval() -> str`  
>Evaluates the application. If the arguments are invalid, an `InvalidArgumentError` is raised.
The output of the application is returned as a string.