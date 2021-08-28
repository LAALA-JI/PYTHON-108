# Tuples are used to store multiple items in a single variable.
#
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Since tuples are indexed, they can have items with the same value
# --Allow Duplicates
# Since tuples are indexed , they can have items with the same value.

a_short_tuple = "LaaLa" , "Nawab"
print(type(a_short_tuple))
my_tuple = ("LaaLa" , "Nawab")
a =[("LaaLa" , "Nawab") , ("Abhi" , "Shreeji")]
a = ["LaaLa" , "Nawab"]
single_ele = "Laala",
print(single_ele)

# Access tuples
t = (1,2,3,4,5)
print(t[-1])
t.append(6)
t+=(6,)
t = t+(6,)
print(t)



# Tuple Methods
p=(1,2,3,4,5,6,5)
x = p[1:4]
print(x)
x,y,z,*other = p
print(x)
print(y)
print(type(other))
print(p.count(6))
print(p.index(5))












