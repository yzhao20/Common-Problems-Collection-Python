"""
This section covers two different searching methods: 
  1. Linear Search: called brute force search, aka British Museum algorithm. All cases are O(n) complexity.
    1.1 On unsorted list
    1.2 On sorted list
  2. Bisection Search
"""


# 1.1 Linear Search on unsorted list
def linear_search(L, e):  # L is a list, and e is one element
    found = False   # initialize our result, i.e output of this function
    for i in range(len(L)):  # look through all elements in the list
        if L[i] == e:     # check point
            found = True    
    return  found   # Output of this fucntion
print(linear_search(['e', 'd'], 'd'))    # Call the function, and pay attention to that element in list is case sensitive.



# 1.2 Linear Search on sorted list
def linear_search1(L, e):   # We need to make sure the L is SORTED! ascending (this case) or descending.
    for i in range(len(L)):  # Look through all elements in the list L
        if L[i] == e:    # If equality check returns true, then true
            return True
        if L[i] > e:   # If the L[i] is greater than e, False. Becase L is sorted, which means all elements after L[i] are all greater than e, always False.
            return False
    return False   # Cool statement, which returns an default value False.
print(linear_search1(['e', 'd'], 'd'))   # TRICKY ! As the user didn't enter a sorted list, the result would be WRONG !



# 2 Bisection Search
"""
Four steps: 1. Pick an index, i, that divides list in half.  2. Ask if L[i] == e  3. If not, ask if L[i] is larger or smaller than e.  4. Depending on answer, search left or
            right half of L for e.
Assumption: The list L is sorted alreay!
"""
def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):   # define another function with two extra arguments high and low
        if high == low:   # Base case in recursive function.
            return L[low]  == e  # Check if it is what we search for.
        mid = (low + high) // 2  # set the mid as another variable, which equals the half point (floor division here).
        if L[mid] == e:  # if found, return true
            return True
        elif L[mid] > e:  # not found and bigger than what we search for, trying to disgard the right half
            if low == mid:   # nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1) # Search in the left half only
        else:
            return bisect_search_helper(L, e, mid + 1, high)  # not found and smaller than what we search for, discard the left half
    if len(L) == 0:  # if the list is empty just in case, done
        return False
    else:   # if the list is NOT empty, call the function with low index is 0, and high index is (len(L) -1). The high index would indeed return the last element in the list.
        return bisect_search_helper(L, e, 0, len(L) - 1)
print(bisect_search2(['c', 'd', 'm'], 'd'))   # The first argument list MUST be sorted.
