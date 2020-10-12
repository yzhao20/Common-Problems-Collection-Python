"""
1. List comprehension
Syntax: 
expression for item in list.
"""
a = ["math", 100, "him", "her"]
b = [str(i) for i in a]   # The item a could be a string or tuple whichever it could be iterable.
c = [type(i) for i in b]
print(c)  # The result is still a list, including 4 items are all <class 'str'>.

"""
2. Lambda function
Syntax: 
lambda arguments: expression
"""
