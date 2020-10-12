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
