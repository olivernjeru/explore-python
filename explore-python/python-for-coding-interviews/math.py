# Division is decimal by default
print(5 / 2)

# Double Slash rounds down to integer division
print(5 // 2)

# CAREFUL: most languages rounds towards 0 by default so negative numbers will round down
print(-3 // 2)

# A workaround for rounding towards zero is to use decimal division and then convert to int
print(int(-3 / 2))

# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-3 % 2)

# To be consistent with other languages modulo
import math
print(math.fmod(-10, 3))

# A few more math helpers
# To round down
print(math.floor(3 / 2))
# To round up
print(math.ceil(3 / 2))
# To find the square root
print(math.sqrt(3))
# To find the Power
print(math.pow(2, 3))

# Max / Min int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))
# But still less than infinity, to check if so, we use the statement below
print(math.pow(2, 200) < float("inf"))