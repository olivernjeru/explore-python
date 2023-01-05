# Sorting defaults to sorting in ascending order
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

# Sorting in descending order
arr.sort(reverse=True)
print(arr)

# Sort a list of strings, defaults to sorting based on alphabetical order
arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by length of the string) by passing in a lambda function, defaults to sorting in ascending order by default
arr.sort(key=lambda x: len(x))
print(arr)