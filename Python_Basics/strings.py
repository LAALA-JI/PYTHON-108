# What are Strings
# String is sequence of Unicode characters.
# We can use single quotes or double quotes to represent strings.
# Multi-line strings can be denoted using triple quotes, ''' or """.
# A string in Python consists of a series or sequence of characters - letters, numbers, and special characters.
# Strings can be indexed - often synonymously called subscripted as well.
# Similar to C, the first character of a string has the index 0.

# String Assignment

a = "Virat"
print(a)
print(type(a))
b = 'kohli'
print(b)
c = """ Hello
World How
you
Doing"""
print(c)
d = "Rohit" \
    " Sharma"
print(d)
# string Concatination
first_name = "Shikhar"
last_name = "Dhawan"
full_name = first_name +" "+ last_name
print(full_name)








# Escape Sequence

weather  = "It\'s \"kind of\" sunny today"
print(weather)
weather_1 = "\tIt\'s \"kind of\" sunny today"
print(weather_1)
weather_2 = "\tIt\'s \"kind of\" sunny today. \n Hope you are having a good day "
print(weather_2)

# Formatted Strings

name = "Dhoni"
jersey_no = 7
# a = "Dhoni"
# print(name + " wears jersey of number " + str(jersey_no) )
print(f"{name} wears jersey number of {jersey_no}")
print("{} wears jersey number of {}".format('Dhoni' ,'7'))
print("{} wears jersey number of {}".format(name ,jersey_no))
print("{0} wears jersey number of {1}".format('Dhoni' ,'7'))
print("{new_name} wears jersey number of {jersey}".format(new_name = 'Dhoni' ,jersey = '7'))


# String Indexes
# l = "The Coding"
     # 0123456789
print(l[1])
# [start : stop : Stepover]
print(l)
print(l[0:len(l):1])
print(l[::1])

print(l[::-1])
print(l[::-2])

print(l[0:4])

# STRINGS are IMMUTABLE !!

g = "LAALA"
#
g[0]="M"
g = "M" + g
print(g)

# STRING METHODS
# builtin functions
print('hello ')
# len()
# int()
# str()
# float()

quote = "it is what it is "
intro = "MY NAME IS LAALA"
print(quote.upper())
print(len(quote))
print(quote.find('it'))
print(quote.replace('it','this'))
q_2 = quote.replace('it','this')
print(quote)
print(q_2)
print(intro.capitalize())

















