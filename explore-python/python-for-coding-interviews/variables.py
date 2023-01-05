# Variables are dynamically typed

n = 0
print('n=', n)

# Past this point, n changes

n = "abc"
print('n=', n)

# Multiple Assignments
n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# Increment
n = n + 1 # good
n += 1 # good
# n++ # bad

# None is null (absence of a value)
n = 4
n = None
print('n=', n)