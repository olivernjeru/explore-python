# Nested functions have access to outer variables
def outer(a, b):
    c = 'c'

    def inner():
        return a + b + c
    return inner()

print(outer('a', 'b'))

# Can modify objects but not reassign values unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # the code below will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)