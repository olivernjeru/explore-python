# hash set
# They are really useful because we can search them in constant time
mySet = set()
# We can also add values in constant time and there can never be any duplicates
mySet.add(1)
mySet.add(2)
print(mySet)
# To know how many elements have been inserted we can get the length of the hashset
print(len(mySet))
# To search the hashset without a function we can use the in operator
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

# We can remove values also in constant time
mySet.remove(2)
print(2 in mySet)

# To initialize a hashset with a bunch of values we can pass a list
# list to set
print(set([1, 2, 3]))

# Set Comprehension
mySet = {i for i in range(5)}
print(mySet)