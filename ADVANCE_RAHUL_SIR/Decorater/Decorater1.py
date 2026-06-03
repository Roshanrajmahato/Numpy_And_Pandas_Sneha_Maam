"""
"""
"""

#️⃣ 1. What is a Decorator?

A Decorator is a special function in Python that modifies the behavior of another function 
without changing its actual code (implementation).

OR

A decorator is a callable that takes another function as input and returns a new function.

#️⃣ 2. Why Do We Use Decorators?
Decorators are used to:-
1️⃣ Add extra functionality (before/after execution)
2️⃣ Logging
3️⃣ Authentication
4️⃣ Measuring execution time
5️⃣ Input validation
6️⃣ Code reuse

#️⃣ 3. Important Rules of Decorator

✅ Rule 1:- It must be a nested function

✅ Rule 2:- It must return the inner function

✅ Rule 3:- It should take a function as a parameter

#️⃣ Basic Structure of a Decorator
def mydecorator(func):          # Step 1: decorator function

    def inner():                # Step 2: inner function
        print("Before function call")
        func()                  # Step 3: calling original function
        print("After function call")

    return inner                # Step 4: return inner function

🔎 What happens internally?

mydecorator(myfunction) → returns inner

value = inner

value() → runs inner()

inner() calls original functionfunc()

🔹 Output:
Before function call
Hi, I am myfunction
After function call

"""
def mydecorator(func):
    def innerfunction():
        print("Something Happend Before the Call")
        func()
        print("Something Happen After the Call")

    return innerfunction


def myfunction():
    print("Hi I am The Original Function")

value=mydecorator(myfunction) # myfunction => func or func() => myfunction
# value -> innerfunction
value()
# value() -> innerfunction()

"""

def myfunction():
    print("Hi, I am myfunction")
value = mydecorator(myfunction)
value()
or
@mydecorator
def myfunction():
    print("Hi, I am myfunction")
myfunction()

mydecorator() :- This is a decorating function
myfunction()  :- This is a decorated function which is being modified by decorating function


#️⃣1️⃣ Example 1 
# Decorator with Arguments
If original function has parameters:
"""
def mydecorator(func):
    def inner(a, b):
        print("Before execution")
        result = func(a, b)
        print("After execution")
        return result
    return inner


@mydecorator
def add(x, y):
    return x + y

print(add(5, 3))
'''
Output:
Before execution
After execution
8
'''
"""

#️⃣2️⃣ Example 2 :- Real world

"""
import time

def timer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return inner

@timer
def task():
    for i in range(1000000):
        pass

task()

'''
This measures execution time.
👉 Decorator = Function that takes a function and returns a modified function.
'''
"""

##Python Decorators**
A decorator is a function that takes another function as an argument and returns a new function (a "wrapper") 
with the modified behavior. This is possible because functions in Python are first-class objects, 
meaning they can be passed as arguments, assigned to variables, and returned from other functions.

When you use a Python decorator, you wrap a function with another function, which takes the original function 
as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, 
enhancing code reusability and readability.

"""

