# Data Structure:
# A data structure is a collection of data elements
# (such as numbers or characters—or even other data structures)
# that is structured in some way, for example, by numbering the elements.
# The most basic data structure in Python is the "sequence".
# -> List is one of the Sequence Data structure
# -> Lists are collection of items (Strings, integers or even other lists)
# -> Lists are enclosed in [ ]
# -> Each item in the list has an assigned index value.
# -> Each item in a list is separated by a comma
# -> Lists are mutable, which means they can be changed.

# List Creation
empty_lst = []
lst = [1,2,3,4,5,6]
print(lst)
lst1 = ['a','b','c','d','e']
lst2 =[1,2,3,4,"LAALA" , True]
lst3 = [ [1,2,3,4],[5,6,7,8] ]

# List Length
print(len(lst1))



# List Slicing

# string = "LAALA"
# print(string[0])
# string[0] = "M"
# print(string)

# amzn_cart = ['laptop','notebooks','mango','Table','Chair']
# print(amzn_cart)
# amzn_cart[1] = 'IPAD'
print(amzn_cart)
# print(amzn_cart[::2])
print(amzn_cart)
new_cart = amzn_cart[::2]
print(new_cart)
new_cart = amzn_cart[:]
amzn_cart[0] = 'MacBook Pro'
print(amzn_cart)
print(new_cart)
print(type(lst))




# LIST METHODS





























# List Append
l = ['one','two','three','four','five']
l.append('six')
print(l)
# List Insert
l2 =  ['one','three','four','five']
l2.insert(1,'two')
print(l2)

# List Remove
l2.remove('two')
print(l2)

lst3 = [1,2,3,4,5,6]
lst3.append(7)
print(lst3)


a = [1,2,3,4,5,6,7,8]
b = [9,10,11]
# a.append(b)
print(a)

# [[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11]]
# list Extend

a.extend(b)
print(a)

# List Delete
del(a[10])
print(a)

# POP
d = a.pop(9)
print(d)

# List Reverse
g = ['one' , 'two' , 'three']
g.reverse()
print(g)

# List Sorting
# sorted(lst5)

numbers = [2,5,7,8,10,15,1,3]
print(sorted(numbers))
print(numbers)


l1 = ['rohit sharma' , 'shikhar dhawan' , 'virat kohli']
l2 = ['Shreyas Iyer','Suryakumar yadav' , 'Hardik Pandya']
l3  = l1 + l2
print(l3)

# List Count
v = [1,1,1,1,2,2,2,3,3,3,34,4,5,6,7,89,0]
print(v.count(17))

fruits = ['apple', 'banana', 'cherry', 'orange']

# fruits.clear()
# print(fruits)
# new_fruits  = fruits.copy()
# print(new_fruits)
frts = ['apple' , 'oranges' , 'mango' , 'Strawberries' , 'Cheeku']
# frts.clear()
print(frts)
new_frts = frts.copy()
print(new_frts)
# print(new_frts.index('apple'))

print(new_frts.index('cheeku'))


# lst = ['one', 'two', 'three', 'four']

# lst.append('five') # append will add the item at the end
#
# print(lst)
#
# List Insert

#syntax: lst.insert(x, y)
#
# lst = ['one', 'two', 'four']
#
# lst.insert(2, "three") # will add element y at location x
#
# print(lst)
#
# lst = ['one', 'two', 'three', 'four']

#remove an item from list
# lst.remove('three')
#
# print(lst)
#syntax: lst.remove(x)

# lst = ['one', 'two', 'three', 'four', 'two']
#
# lst.remove('two') #it will remove first occurence of 'two' in a given list
#
# print(lst)

# List Append & Extend

# lst = ['one', 'two', 'three', 'four']
#
# lst2 = ['five', 'six']
#
# #append
# lst.append(lst2)
#
# print(lst)

# lst = ['one', 'two', 'three', 'four']
#
# lst2 = ['five', 'six']
#
# #extend will join the list with list1
#
# lst.extend(lst2)

# print(lst)

# List Delete

#del to remove item based on index position

# lst = ['one', 'two', 'three', 'four', 'five']

# del(lst[])
# print(lst)

#or we can use pop() method
# a = lst.pop(1)
# print(a)

# print(lst)



# lst = ['one', 'two', 'three', 'four']

#remove an item from list
# lst.remove('three')
#
# print(lst)




# LIST Reverse
#reverse is reverses the entire list
#
# lst = ['one', 'two', 'three', 'four']
#
# lst.reverse()
#
# print(lst)


 # LIST SORTING
# The easiest way to sort a List is with the sorted(list) function.

# That takes a list and returns a new list with those elements in sorted order.

# The original list is not changed.

# The sorted() optional argument reverse=True, e.g. sorted(list, reverse=True), makes it sort backwards.


#create a list with numbers
# numbers = [3, 1, 6, 2, 8]

# sorted_lst = sorted(numbers)


# print("Sorted list :", sorted_lst)

#original list remain unchanged
# print("Original list: ", numbers)


#print a list in reverse sorted order
# print("Reverse sorted list :", sorted(numbers, reverse=True))

#orginal list remain unchanged
# print("Original list :",  numbers)