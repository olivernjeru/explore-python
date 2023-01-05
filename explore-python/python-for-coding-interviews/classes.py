# Class
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        # Creating a member variable called nums and assigning it to the nums that was passed in as a parameter to the constructor
        self.nums = nums
        self.size = len(nums)

    # Self key word required as a param to create a method for this class whether you are passing an argument or not so that we can have access to member variables such as self.size
    def getLength(self):
        return self.size

    # Call another member function from a member function
    def getDoubleLength(self):
        return 2 * self.getLength()