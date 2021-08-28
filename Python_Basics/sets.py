# Sets are used to store multiple items in a single variable.
# Sets are unordered collection of unique objects.
# Sets are written with curly brackets.
# my_set = {1,2,3,4,5}
# # print(type(my_set))
# # print(my_set)
my_set.add(6)
my_set.add(2)
print(my_set)

my_list = [1,2,4,4,3,3,5,5,6]
print(set(my_list))

my_set = {1,2,3,4,5,5}
print(my_set[2])
my_set.remove(5)
print(my_set)
print(len(my_set))
print(7 in my_set)

new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)


# Set Methods

# .difference
# print(my_set.difference(your_set))
# print(my_set)
# .discard
# It removes the element from the set if it is the member
# print(my_set.discard(5))
# print(my_set)
# .difference_update
# print(my_set.difference_update(your_set))
# print(my_set)

# .intersection
# print(my_set.intersection(your_set))
# # .isdisjoint
# print(my_set.isdisjoint(your_set))
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
# .issubset
print(my_set.issubset(your_set))
# .issuperset
print(your_set.issuperset(my_set))
my_set = {1,2,3,4,5,5}
your_set = {4,5,6,7,8,9,10}
# .union
# print(my_set.union(your_set))
print(my_set | your_set)
print(my_set & your_set)






















