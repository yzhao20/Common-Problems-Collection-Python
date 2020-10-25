"""
1. The General idea is that define or create a new list based on exsiting/specific data list/set/dictionary.E
Eg1. List Comprehension
"""
a = ["math", 100, "him", "her"]
b = [str(i) for i in a]   # The item a could be a string or tuple whichever it could be iterable.
c = [type(i) for i in b]
print(c)  # The result is still a list, including 4 items are all <class 'str'>.

num = [8, 3, 4, 9, 11, 23, 44, -1, 9]
my_list = [i for i in num if i % 2 == 0]  # Produce a new list containing even number only.

new_list = [(letter, num) for letter in "abcd" for num in range(4)]  # This would generate a list composed of tuple pairs. (each element could be list/dictionary/set too!)

"""
2. Comprehension using Lambda function
Syntax: lambda arguments: expression
"""
a = lambda x, y: x * y * 20 + x ** 2 + 10
print(a(10, 20))

num = [8, 3, 4, 9, 11, 23, 44, -1, 9]
my_list = filter(lambda n: n % 2 == 0, num)



"""
3. Zip function and Comprehension in dictionary, creating a "nested loop" work.
"""
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
print(list(zip(names, heros)))

my_dic = {}
for name, hero in zip(names, heros):  # As zip function returns pair values.
    my_dic[name] = hero  # Set the hero to each element in names list.
print(my_dic)

my_dic = {name: hero for name, hero in zip(names, heros) if name != "Peter"}   # Dictionary comprehension, a pair of values in a zip object combined with a if condition.
print(my_dic)


"""
4. Comprehension in Set. By definition, set would NOT has dupulicate numbers and order does NOT matter.
"""
num = [1, 2, 3, 1, 4, 3, 4, 4, 1, 7, 0, 3, 9, 9, -2]    # Obviously, this list has so many duplicate numbers.
my_set = set()   # Create an empty set
for item in num:
    my_set.add(item)   # Add element to the set.
print(my_set)

my_set1 = {i for i in num if i < 2}  # This just does what the above loop does. And the "if i < 2" depends if we need it or not.
print(my_set1)



"""
5. Generator Expression, quite similar to comprehension but with slight difference.
"""
li = [1, 2, 3, 1, 4, 3, 4, 4, 1, 7, 0, 3, 9, 9, -2]
def gen_func(nums):
    """
    Generator Expressions: It's going to yield "n*n" for each "n" in num list.
    """
    for n in nums:
        yield n * n   # yield keyword would return an object of generator class.

my_gen = gen_func(li)
print(list(my_gen))  # Convert it into a list

my_gen_1 = (n*n for n in li)   # This single line does the same thing as the above loop, but similar to list comprehension but minor different.
print(list(my_gen_1))
