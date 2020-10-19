"""
1. Define or create a new list based on exsiting list(or string, or something is iterable)
Solution: List comprehension
Syntax: expression for item in list.
Takeaway:
"""
a = ["math", 100, "him", "her"]
b = [str(i) for i in a]   # The item a could be a string or tuple whichever it could be iterable.
c = [type(i) for i in b]
print(c)  # The result is still a list, including 4 items are all <class 'str'>.


"""
2. Return
Solution: Lambda function
Syntax: lambda arguments: expression
Takeaway:
"""
a = lambda x, y: x * y * 20 + x ** 2 + 10
print(a(10, 20))


"""
3. Convert any positive integer to a string, nice code. Major steps:
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
