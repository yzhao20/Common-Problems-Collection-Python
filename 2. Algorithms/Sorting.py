"""
Four major sorting algorithms:
1. Monkey sort: aka bogosort, stupid sort, slowsort, permutation sort, shotgun sort. Best case: O(n). Worst case: unbounded !! n factorial, n to n power or even more!
2. Bubble sort: Famous sorting approach. O(n^2)
3. Selection sort: Easy to understand. O(n^2)
4. Merge sort: Best among those approaches. O(n*log(n)), which increases slowly particularly when n is large.
"""

"""
1. Monkey sort's major steps. E.g to sort a deck of cards: 
   1. Throw them in the air
   2. Pick them up
   3. Check if they are sorted alreay. If yes, done. Otherwise repeat the throw again.
"""
def monkey_sort(L):
    while not is_sorted(L):  # This piece of code is just a demonstration as we need to define is_sorted function and import random library first.
        random.shuffle(L)


"""
2. Bubble sort's major steps: 
   1. Compare consecutive paris
   2. Swap elements in pair if needed, such that smaller element is first
   3. When reach end of list, start over again
   4. Stop when no more swaps have been made in the last look through.
"""
def bubble_sort(L):
    swap = False   # Initialize the swap variable as False
    while not swap:  # While loop is for doing multiple passes until no more swaps
        print('bubble sort: ' + str(L))
        swap = True   # Initialize swap varialbe as True
        for j in range(1, len(L)): # The for loop is for doing the comparions, indexes starting from 1 to len(L) because we always check the second element in paris.
            if L[j-1] > L[j]:  # If the first one is bigger than the second one in paris.
                swap = False   # In this case, a swap have to be made and swap variable is set as False
                temp = L[j]  # Let the second one element equal to a temprary variable
                L[j] = L[j - 1]  # Let the bigger element to the second one.
                L[j - 1] = temp  # Let the temporary element (smaller value) to the first one.

               
"""
3. Selection sort's major steps: 
   1. Compare consecutive paris
   2. Swap elements in pair if needed, such that smaller element is first
   3. When reach end of list, start over again
   4. Stop when no more swaps have been made in the last look through.
"""
def selection_sort(L):
    suffixSt = 0   # The initial position 0, i.e 1st element.
    while suffixSt != len(L):  # The loop condition until reaches the end of the list, look through the entire list
        for i in range(suffixSt, len(L)):  # Look through all elements in the list.
            if L[i] < L[suffixSt]:  # If some element is smaller than the left element
                L[suffixSt], L[i] = L[i], L[suffixSt] # Make a swap for these two values.
        suffixSt += 1  # This statement is used to go to the next for loop step.
    return L # Finanly output the result.
print(selection_sort([3, 4, 1, -8, -9]))


"""
4. Merge sort's major steps: 
   1. If list is of length 0 or 1, done.
   2. If list has more than one element, split into two lists and sort each.
   3. Merge sorted sublists
      3.1 Look at first element of each, move smaller one to the result list
      3.2 when one list is empty, just copy rest of the other list.
"""
def merge(left, right): # Two arguments as input.
    result = []   # Initialize an empty result list
    i, j = 0, 0  # Assign 0's to both i and j
    while i < len(left) and j < len(right):  # When lef and righ are both not empty
        if left[i] < right[j]:  # If the first element in left is smaller than the first element in right
            result.append(left[i]) # Append the small value in the result list
            i += 1 
        else:     # If the first element in left is bigger than the first element in right
            result.append(right[j])  # Append the small value in the result list
            j += 1 
    while (i < len(left)):  # Once the right list is empty
        result.append(left[i])  # Copy the left list
        i += 1
    while (j < len(right)):  # Once the left list is empty
        result.append(right[j])  # Copy the right list
        j += 1
    return result
def merge_sort(L):  # This is the main function, input is the original list and return the sorted list.
    if len(L) < 2:   # Base case for the recursive function
        return L[:]   # If empty or only one element, done.
    else:  
        mid = len(L) // 2
        left = merge_sort(L[:mid])   # Call this function itself with left part of the original list, return a list
        right = merge_sort(L[mid:])   # Call this function itself with right part of the original list, return a list
        return  merge(left, right)   # Call the merge function with two arguments.
print(merge_sort([-5, 2, -1, 3, 100, -100]))
