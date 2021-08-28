# Comments are lines that exist in computer programs that are ignored by
# compilers and interpreters.
#
# Including comments in programs makes code more readable
# for humans as it provides some information or explanation
# about what each part of a program is doing.
#
# In general, it is a good idea to write comments
# while you are writing or updating a program as it
# is easy to forget your thought process later on,
# and comments written later may be less useful in the
# long term.
#
# In Python, we use the hash (#) symbol to start writing a comment.

# this line prnints hello universe to the console
# print("Hello Universe!")

# Multi line Comments
# If we have comments that extend multiple lines,
# one way of doing it is to use hash (#) in the beginning of each line.

"""
hello everyone welcome to my channel kindly LIKE | SHARE | SUBSCRIBE
if you like the content
"""

# another way of doin this is """ """

# DocString in python
#
# Docstring is short for documentation string.
#
# It is a string that occurs as
# the first statement in a module, function, class, or method definition.
def add(a,b):
	""" This function adds two numbers """
	return a+b
print(add(5,4))
print(add.__doc__)
#
#
# Python Indentation
#
# Most of the programming languages like C, C++,
# Java use braces { } to define a block of code. Python uses indentation.
#
# A code block (body of a function, loop etc.)
# starts with indentation and ends with the
# first unindented line. The amount of indentation
# is up to you, but it must be consistent throughout that block.
# Generally four whitespaces are used for indentation
# and is preferred over tabs
# Indentation can be ignored in line continuation.
# But it's a good idea to always indent. It makes the code more readable.

for x in range(10):
	print(x)
	print(x*2)
print("LAALA")

if True:
	print("Data Science")
	a = "Dhoni"

if True: print("Machine Learning") ; d = 'dhoni'

# Python Statement
# Instructions that a Python interpreter can execute are called statements.

# Multi-Line Statement
# In Python, end of a statement is marked by a newline character.
# But we can make a statement extend over multiple lines with the line continuation character ().

# \\\\
s = 1+2+3+\
43+5+6+\
7+8+9
print(s)


# ()
f = (1+2+3+
43+5+6+
7+8+91)  
print(f)

# ;
a = 'Virat'; b = 'Dhoni'

print(a)
print(b)