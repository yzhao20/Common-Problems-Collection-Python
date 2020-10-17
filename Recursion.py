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
