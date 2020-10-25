"""
LEGB Rule applis for Variable and Function Scopes. Local -- Enclosing -- Global -- Builtins
Two keywords: global and nonlocal, but pay attention to them if used particularly global statement.
"""
x = "global x"  # Create a global varialbe x, assign the string to it.

def outer():    
    x = 'outer x'   # Create a variable x inside this outer function.
    def inner():    # Define this inner function
        nonlocal x     # Use this "nonlocal" keyword statement to indicate that the below x is going to used outside the inner function.
        x = "inner x"
        print(x)   # Print out the x.
    inner()  # Call the inner function.
    print(x)

outer()   # In the global scope, call the outer function.
print(x)  # Print out the x in global sense.
  
