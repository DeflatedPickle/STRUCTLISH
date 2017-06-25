# STRUCTLISH
A slightly modified version of Structured English written in Python.

## What Is STRUCTLISH?
STRUCTLISH is a simple esoteric programming language designed to be easy to read and understand.
It follows many of the rules set by Structured English, and is inspired by it.

## Basic Rules of STRUCTLISH:
- A name must be provided at the top of the script.
- Keywords must be capitalised.
- `IF` statements must have an ENDIF below them.
- A data type must be declared before the data.
- An `EXIT` must be provided at the end of the script.

## Style Guide:
- Indent content of statements by one level.

## What Can STRUCTLISH do?
### Data Types:
When using creating and using data, you will need to declare the type of data that it is.

The currently supported types are:
- `STRING`
- `INTEGER`
- `BOOLEAN`
- `FLOAT`

### Operators:
The currently supported operators are:
- `NOT`
- `IDENTICAL TO`
- `MORE THAN`
- `LESS THAN`

### Comments:
Comments may be used in STRUCTLISH. Both in-line and on their own line.

Example:
```
COMMENT This is a comment.
```

### Variables:
Like many languages, STRUCTLISH can handle setting and using variables.

Example:
```
VARIABLE my_variable EQUALS INTEGER 3
```

### Statements:
Again, like many languages, STRUCTLISH has statements. These can be used for different things.
#### IF:
The `IF` statement will compare if the values you provide fit together through the operator.

Example:
```
IF INTEGER 3 IDENTICAL TO INTEGER 3 THEN
ENDIF
```

### Commands:
STRUCTLISH provides commands for you to use in your scripts.
#### PRINT:
This command will print given information to the terminal.

Example:
```
PRINT INTEGER 3
```

## Example STRUCTLISH Script:
```
EXAMPLE

VARIABLE my_variable EQUALS 3

IF INTEGER 3 IDENTICAL TO VARIABLE my_variable THEN
	PRINT STRING This number is identical to this variable.
ENDIF

EXIT
```
Converted to Python:
```python
"""Example"""

my_variable = 3

if 3 == my_variable:
    print("This number is identical to this variable.")
```
