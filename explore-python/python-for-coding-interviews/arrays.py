# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack so you can push to the array, AKA append
arr.append(4)
arr.append(5)
print(arr)

# You can also pop from the array which will obv pop from the end
arr.pop()
print(arr)

# Because this is an array and not a stack, we can insert into the middle, eg, at index 1 we can insert a value 7 O(N)
arr.insert(3, 7)
print (arr)

# O(1) operations
arr[0] = 0
arr[4] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Be careful when indexing an array, -1 is not out of bounds it is the last value
arr = [1, 2, 3]
print(arr[-1])

# Sublists aka(slicing)
# Below we are taking the values from index one to index 3 but not including index 3
arr = [1, 2, 3, 4]
print(arr[1:3])

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)
# Be careful though because we have to make sure that the number of variables on the left hand side matches the number of variables on the right hand side

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without Index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)