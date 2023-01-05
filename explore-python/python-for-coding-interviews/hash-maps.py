# hashMap (aka dict)
myMap = {}
# Adding values to a hash map, we can never have duplicate keys here
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
# Checking for the length of the hashMap will give us the number of keys in the hashMap
print(len(myMap))

# Values mapped to a key can be modified
myMap["alice"] = 80
print(myMap["alice"])

# Searching for whether a key exists in a hashMap takes O(1)
print("alice" in myMap)
print("bob" in myMap)
print("dan" in myMap)

# We can remove a key in a hashMap which will also remove that value
myMap.pop('alice')
print('alice' in myMap)

# To initialize a hashMap we can add pairs inside the carli braces
myMap = {'alice':90, 'bob': 69}
print(myMap)

# Dict comprehension
myMap = {i: 2*i for i in range(5)}
print(myMap)

# Looping through a map
myMap = {'alice': 80, 'bob': 40}
# By default we iterate through every single key and then print that key and then print the value that key maps to
for key in myMap:
    print(key, myMap[key])

# Loop through the values of the hashmap if we dont even need the key
for val in myMap.values():
    print(val)

# Loop through the items of that map which will give us the key and the value
for key, val in myMap.items():
    print(key, val)