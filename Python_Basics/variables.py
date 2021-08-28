# IDENTIFIERS
# Identifier is the name given to entities like class, functions, variables etc. in Python.
# It helps differentiating one entity from another.
# Rules for Writing Identifiers:
# Identifiers can be a combination of letters in lowercase (a to z) or
# uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# An identifier cannot start with a digit.
# 1variable is invalid, but variable1 is perfectly fine.
a = 10
# print(a)
# 14a = 10


# We cannot use special symbols like !, @, #, $, % etc. in our identifier.
# !b = 15

# VARIABLES
# A variable is a location in memory used to store some data (value).
# They are given unique names to differentiate between different memory locations.
# The rules for writing a variable name is same as the rules for writing identifiers in Python.
# We don't need to declare a variable before using it.
# In Python, we simply assign a value to a variable and it will exist.
# We don't even have to declare the type of the variable.
# This is handled internally according to the type of value we assign to the variable.

# Variable Assignments
# We use the assignment operator (=) to assign values to a variable
a = 15
b = 6.5
c = "LAALA"
print(type(b))

# Multiple Assignments
# a ,b ,c = 10 , 15 , 'LAALA'

a=b=c="LAALA"

# print(b)
# Storage Locations

t = 5
print(id(t))
s = 5
print(id(s))

s = 4
print(id(s))

# Observation: ?



# Key Differences between Identifier and Variable

# Both an identifier and a variable are the names allotted by users to a particular entity in a program.
# The identifier is only used to identify an entity uniquely in a program at the time of execution whereas
# , a variable is a name given to a memory location, that is used to hold a value.
# Variable is only a kind of identifier, other kinds of identifiers are function names, class names, structure names,
# etc. So it can be said that all variables are identifiers whereas, vice versa is not true.



# KEYWORDS
# Keywords are the reserved words in python
# We can't use a keyword as variable name, function name or any other identifier
# Keywords are case sensitive
# Keywords cannot be used as identifiers.

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as',
# 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
# 'raise', 'return', 'try', 'while', 'with', 'yield']

# global = 15
