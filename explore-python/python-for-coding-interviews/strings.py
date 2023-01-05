# Strings are pretty similar to arrays
s = "abc"
r = 'xyz'
# Slicing
# Print only characters from index 0 to 2 but not including 2
print(s[0:2])
# Print only characters from index 0 to 1 but not including 1
print(r[0:1])

# But they are immutable meaning that we cannot modify the string or reassign values to it
# This will result into an error if ran s[0] = "A"
# We can however update the string, so that will create a new string to accomodate for the new characters added at the end
# Modifying a String is considered O(n) operation
s += "def"
print(s)

# Valid numeric strings can be converted into integers
print(int("123") + int("123"))
# Integers can be converted into strings
print(str(123) + str(123))

# In rare cases you may need the ASCII value of a character you may use the ord function
print(ord('a'))
print(ord("b"))

# Combine a list of strings together with a delimitor
strings = ["ab", 'cd', 'ef']
print(strings)
# Join them with an empty string delimitor below
print("".join(strings))