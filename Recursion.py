"""
1. Please find the power set of integers of integer n. This problem is a recursion question, as if we know the power set of n-1, which can generates the
   power set of n by simply adding n to each element of n-1 power set. 
Example:
  n = 1, power set is: [], [1]
  n = 2, power set is: [], [1], [2], [1, 2] (notice that the new two elements are just adding 2 to each element of 1's power set.)
  n = 3, power set is: [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]  (notice that the new 4 elements are just adding 3 to each element of 2's power set.)
Such a classical resursion problem whih O(2**n), that means it has a high compuational complexity.
"""
def getsubsets(L):
    if len(L) == 0: # base case, need to specify this. 
        return [[]] # list of empty list
    smaller = getsubsets(L[:-1])  # all subsets without the last element
    extra = L[-1:] # create a list just with the only last one element
    new = []
    for item in smaller:
        new.append(item + extra) # for each element in smaller power set solution,
        # add one with last element
    return smaller + new  # combine those with last element and those without
print(getsubsets([1, 2, 3, 4]))

"""
2. Fibonacci numbers: commonly denoted Fn, form a sequence called Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
    i.e. F0 = 0, F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5 ...  obviously an iterative question.
"""
def fib_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n - 1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_i 
        return fib_ii
print(fib_iter(6))
