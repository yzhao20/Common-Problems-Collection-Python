"""
1. List: sorted function and sort method are quite different!
"""
li = [9, 3, 2, 0, 33, 22, -98, 1]  
s_li = sorted(li, key=abs, reverse=True) # Sorted function returns a new variable and it does NOT affect the original list, the key/reverse argument are optional.
print("sorted varialbe:\t", s_li)
li.sort(reverse=True)                 # The sort method would change the original list for sure. By default, it's in an scending order.
print("original variable:\t", li)



"""
2. Tuple: sorted function still works. But it would generate a new LIST rather than a new tuple.
"""
tu = (9, 1, 2, 3, -9, 8, -8)
print("Original Tuple\t", tu)
s_tu = sorted(tu)                  # The sorted function still work with tuple.
print("Sorted Tuple:\t", s_tu)



"""
3 Dictionary: sorted function requires more arguments to determine the sort criteria.
"""
class Employee(object):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return "{},{},{}".format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)
employee = [e1, e2, e3]

def e_sort(emp):   # This is our customized sort criteria.
    return emp.salary  # Based on salary

#  s_employee = sorted(employee) # This line is WRONG simply because sorted function can't recognize to sort in what way
s_employee = sorted(employee, key=e_sort, rverse=True)   # Notice that there's () after the e_sort function, which is similar to the usage of abs function in a list.
#  s_employee = sorted(employee, key=lambda e: e.name, rverse=True)  # The lambda function returns e.name that is what we need. In this case, the function defined above is gone.
print(s_employee)



"""
4 Dictionary: the attrgetter function in the operator module can help with this.
"""
from operator import attrgetter  # One function in the operator module does the same job, which can be used in the sorted function.
s_employee = sorted(employee, key=attrgetter('name'), reverse=True)  # Use the attrgetter('name') as the key argument.
