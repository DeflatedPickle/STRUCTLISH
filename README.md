# STRUCTLISH
A slightly modified version of Structured English written in Python.

## What Is STRUCTLISH?
STRUCTLISH is a simple esoteric programming language designed to be easy to read and understand.
It follows many of the rules set by Structured English, and is inspired by it.

## Using STRUCTLISH:
If you'd like to use STRUCTLISH, download this repository, edit the example script and run `interpreter.py`.
In the future, this will obviously be changed.

### Syntax Highlighting:
Most programmers are used to having the syntax of a language be highlighted in their Editor/IDE.
Since STRUCTLISH is a ;new, small, unpopular language, no IDE natively supports it.
However, if you look in the "Language Files", you'll find the language files I have made for some Editors/IDEs.

#### Currently Supported Editors/IDEs:
- Notepad++

## Basic Rules of STRUCTLISH:
- A name must be provided at the top of the script.
- Keywords must be capitalised.
- `IF` statements must have an ENDIF below them.
- A data type must be declared before the data.
- An `EXIT` must be provided at the end of the script.

## Style Guide:
- Indent content of statements by one level.
- Use only lowercase for variables.
- Separate words in variables with underscores (`my_variable`).

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

### Commands:
STRUCTLISH provides commands for you to use in your scripts.
#### PRINT:
This command will print given information to the terminal.

Example:
```
PRINT INTEGER 3
```
Output:
```
3
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
	PRINT INTEGER 3
ENDIF
```
Output:
```
3
```

### Loops:
#### FOR:
The `FOR` loop will continue to run till it's objective is satisfied.

Example:
```
FOR VARIABLE i IN RANGE 0 TO 5 THEN
	PRINT VARIABLE i
ENDFOR
```
Output:
```
0
1
2
3
4
```

## Example STRUCTLISH Script:
```
PROGRAM EXAMPLE

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
