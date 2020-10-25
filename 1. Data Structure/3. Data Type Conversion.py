"""
1. We have 5 common data types: list, tuple, set, dictionary.
This section is about how to convert one type into the other and tips associated.
"""








"""
2. Convert any positive integer to a string, nice code. Major steps:
    1. If this integer is 0, done.
    2. If positive, figure out the 1th gidit, 10th digit, 100th digit, 1000th digit.... Done.
"""
def intToStr(i):   # Input is an integer
    digits = "0123456789"   # Create a string varialbe '0123....9', which is NICE!
    if i == 0:  # Base case
        return "0"
    result = ""  # Initialize the result
    while i > 0:  # While loop when this integer is positive
        result = digits[i % 10] + result  # First time, get the 1th digit, Second time get the 100th digit...
        i = i // 10  # First time disgard the 1th digit as 1th digit has been added to the result, Second time disgard the 100th digit as 100th digit has been added...
    return result  # Output of this function
