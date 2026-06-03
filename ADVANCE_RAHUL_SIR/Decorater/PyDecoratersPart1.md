# 1️⃣ What is a Decorator in Python?

## 📖 Definition (Simple)

**A decorator is a function that modifies the behavior of another function without changing its original code.**

**A decorator is a function that takes another function as an argument and returns a new function (a "wrapper") with the modified behavior. This is possible because functions in Python are first-class objects, meaning they can be passed as arguments, assigned to variables, and returned from other functions.**

**When you use a Python decorator, you wrap a function with another function, which takes the original function as an argument and returns its modified version. This technique provides a simple way to implement higher-order functions in Python, enhancing code reusability and readability.**

---

## 📖 Interview Definition

**A decorator is a callable that takes another function as input, adds extra functionality, and returns a modified function.**

---

# 🧠 Why Decorators Are Used

Sometimes we want to:

* Add logging
* Add authentication
* Add timing
* Add validation
* Add debugging

But we **don't want to change the original function**.

So we use:

# 🎁 Decorators (Wrapper Concept)

---

# 2️⃣ Real-Life Analogy (Very Helpful)

Think:

```text
Original Function → Mobile Phone
Decorator → Mobile Cover
```

Phone stays same.

Cover adds protection.

Decorator adds functionality.

---

# 3️⃣ Basic Structure of a Decorator

A decorator always has:

1️⃣ Outer function
2️⃣ Inner function
3️⃣ Return inner function

---

## Basic Example

```python
def my_decorator(func):

    def inner():
        print("Before function call")

        func()

        print("After function call")

    return inner
```

---

# 4️⃣ Decorated Function

```python
def my_function():
    print("Hello, I am my_function")
```

---

# 5️⃣ Applying Decorator (Manual Way)

```python
value = my_decorator(my_function)

value()
```

---

# 🔍 Step-by-Step Execution (Very Important)

This is frequently asked in interviews.

---

## Step 1

```python
value = my_decorator(my_function)
```

Means:

```text
func = my_function
```

---

## Step 2

Inside decorator:

```python
def inner():
```

Inner function is **created but NOT executed**.

---

## Step 3

Decorator returns:

```python
return inner
```

So:

```text
value = inner
```

---

## Step 4

Now:

```python
value()
```

Means:

```python
inner()
```

Execution becomes:

```text
Before function call
Hello, I am my_function
After function call
```

---

# 6️⃣ Using @ Symbol (Modern Way)

Instead of:

```python
value = my_decorator(my_function)
value()
```

We write:

```python
@my_decorator
def my_function():
    print("Hello, I am my_function")

my_function()
```

---

## 🔍 Internal Working of @

Python converts:

```python
@my_decorator
def my_function():
```

Into:

```python
my_function = my_decorator(my_function)
```

Very important interview concept.

---

# 7️⃣ Decorator With Arguments (*Most Important*)

Basic decorator fails if function has parameters.

So we use:

```python
*args
**kwargs
```

---

## Example

```python
def my_decorator(func):

    def inner(*args, **kwargs):

        print("Before execution")

        func(*args, **kwargs)

        print("After execution")

    return inner
```

---

## Usage

```python
@my_decorator
def greet(name):
    print("Hello", name)

greet("Roshan")
```

---

## Output

```text
Before execution
Hello Roshan
After execution
```

---

# 🧠 Why *args and **kwargs?

Because function may have:

```python
greet(name)

add(a,b)

login(user,password)
```

Decorator must handle:

✔ Any number of arguments
✔ Any type of arguments

---

# 8️⃣ Decorator Returning Value

Very important concept.

---

```python
def my_decorator(func):

    def inner(*args, **kwargs):

        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return inner
```

---

## Example

```python
@my_decorator
def add(a, b):
    return a + b

print(add(5, 3))
```

---

## Output

```text
Before execution
After execution
8
```

---

# 9️⃣ Real-World Use Cases

These are used in real projects.

---

# 1️⃣ Logging Decorator

```python
def log_decorator(func):

    def inner():

        print("Function Started")

        func()

        print("Function Ended")

    return inner
```

Used for:

✔ Debugging
✔ Monitoring

---

# 2️⃣ Timing Decorator

```python
import time

def timer(func):

    def inner():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start)

    return inner
```

Used in:

✔ Performance optimization

---

# 3️⃣ Authentication Decorator

Used in web applications.

```python
def login_required(func):

    def inner():

        print("Checking login...")

        func()

    return inner
```

Used in:

✔ Flask
✔ Django

---

# 🔟 Multiple Decorators (Stacking)

Yes, you can use more than one.

---

```python
def decor1(func):

    def inner():
        print("Decor1")
        func()

    return inner


def decor2(func):

    def inner():
        print("Decor2")
        func()

    return inner
```

---

## Usage

```python
@decor1
@decor2
def say():
    print("Hello")

say()
```

---

## Output

```text
Decor1
Decor2
Hello
```

---

## Execution Order

Very important:

```text
say = decor1(decor2(say))
```

Bottom → Top execution.

---

# 1️⃣1️⃣ Built-in Decorators (Must Know)

---

# @staticmethod

```python
class Test:

    @staticmethod
    def show():
        print("Static Method")
```

No:

```text
self
cls
```

---

# @classmethod

```python
class Test:

    @classmethod
    def show(cls):
        print("Class Method")
```

Uses:

```text
cls
```

---

# @property

```python
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Used to:

✔ Access method like variable.

---

# 1️⃣2️⃣ functools.wraps (Advanced ⭐)

Problem:

Decorator hides original function name.

Solution:

```python
from functools import wraps

def my_decorator(func):

    @wraps(func)

    def inner():
        func()

    return inner
```

Preserves:

✔ Function name
✔ Docstring

Very important in production.

---

# 1️⃣3️⃣ Decorator With Parameters (Advanced ⭐)

Very common in interviews.

---

```python
def repeat(n):

    def decorator(func):

        def inner():

            for i in range(n):
                func()

        return inner

    return decorator
```

---

## Usage

```python
@repeat(3)
def hello():
    print("Hello")

hello()
```

---

## Output

```text
Hello
Hello
Hello
```

---

# 🧾 Decorator Execution Flow Summary

```text
@decorator
def function():
```

Internally becomes:

```text
function = decorator(function)
```

Then:

```text
function()
→ inner()
→ original function()
```

---

# 🎯 Most Important Interview Questions

Prepare these:

1. What is decorator?
2. Why decorators are used?
3. How does @ work internally?
4. Why use *args and **kwargs?
5. What is decorator chaining?
6. What is functools.wraps?
7. Difference between decorator and closure?
