# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# We can index them but not modify them
# Can be used as keys for a hashMap/set
# Map a pair of values 1,2 as a key to 3
myMap = {(1,2) : 3}
print(myMap)

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists can not be keys