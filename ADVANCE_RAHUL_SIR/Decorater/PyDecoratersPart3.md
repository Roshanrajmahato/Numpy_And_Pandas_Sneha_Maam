# 1️⃣ Functions as First-Class Citizens (Foundation of Decorators)

You should must understand that **functions in Python are first-class objects**.

That means:

* Functions can be stored in variables
* Functions can be passed as arguments
* Functions can return other functions

---

## Example: Passing Function as Argument

```python
def say_hello(name):
    return f"Hello {name}"

def be_with_me(name):
    return f"Hey {name}, be with me together"

def awesome(param):
    name = input("Enter the name: ")
    return param(name)

print(awesome(say_hello))
```

---

## 🔍 Detailed Logic

When you call:

```python
awesome(say_hello)
```

You are **NOT calling `say_hello()`**

You are passing:

```
say_hello   ← function reference (address)
```

Inside:

```python
return param(name)
```

This becomes:

```python
say_hello(name)
```

So output becomes:

```
Hello Roshan
```

---

## 🎯 Interview Point

**Why is this important?**

Because **decorators work by passing functions into other functions.**

---

# 2️⃣ What is a Decorator?

## 📖 Definition

**Decorator is a special function that modifies the behavior of another function without changing its original code.**

OR (Interview Definition):

**A decorator is a callable that takes a function as input and returns a modified function.**

---

## Real-Life Example 🎁

Think of:

* 🎁 Gift → Original Function
* 🎁 Wrapping → Decorator

The gift remains the same, but presentation changes.

---

# 3️⃣ Basic Structure of a Decorator

```python
def my_decorator(param):

    def inner():
        print("Something happens before call")

        param()

        print("Something happens after call")

    return inner
```

---

## Decorated Function

```python
def my_function():
    print("Hi, I am my_function")
```

---

## Manual Decoration

```python
value = my_decorator(my_function)

value()
```

---

## Output

```
Something happens before call
Hi, I am my_function
Something happens after call
```

---

# 4️⃣ Step-by-Step Execution Flow (Very Important)

This is **commonly asked in interviews**.

---

## Step 1

Python reads:

```python
value = my_decorator(my_function)
```

So:

```
param = my_function
```

---

## Step 2

Inside decorator:

```python
def inner():
```

Inner function is **created but not executed**.

---

## Step 3

Decorator returns:

```python
return inner
```

So:

```
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

So execution becomes:

```
Before message
Original function call
After message
```

---

# 5️⃣ Using @ Symbol (Decorator Syntax)

Instead of:

```python
value = my_decorator(my_function)
value()
```

We use:

```python
@my_decorator
def my_function():
    print("Hi, I am my_function")

my_function()
```

---

## Internal Working

Python automatically does:

```python
my_function = my_decorator(my_function)
```

This is called:

## 🧠 Syntactic Sugar

Cleaner syntax.

Used in professional coding.

---

# 6️⃣ Decorator With Arguments (Most Important)

Your current notes don't include this—**but interviewers love this topic.**

---

## Problem

If function has parameters:

```python
def greet(name):
    print("Hello", name)
```

Basic decorator **will fail**.

---

## Solution → Use *args and **kwargs

```python
def my_decorator(func):

    def inner(*args, **kwargs):

        print("Before Function")

        func(*args, **kwargs)

        print("After Function")

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

```
Before Function
Hello Roshan
After Function
```

---

## 🎯 Interview Point

**Why use `*args, **kwargs`?**

To handle:

* Any number of arguments
* Positional arguments
* Keyword arguments

---

# 7️⃣ Decorator That Returns Value

Very important concept.

---

```python
def my_decorator(func):

    def inner(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

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

```
Before
After
8
```

---

# 8️⃣ Real-World Use Cases of Decorators

Very important for interviews.

---

## 1️⃣ Logging

```python
def log_decorator(func):

    def inner():

        print("Function Started")

        func()

        print("Function Ended")

    return inner
```

Used in:

* Debugging
* Monitoring

---

## 2️⃣ Authentication

Used in:

* Web applications
* APIs

Example:

```python
def login_required(func):

    def inner():

        print("Checking Login")

        func()

    return inner
```

Used in frameworks like:

* Flask
* Django

---

## 3️⃣ Timing Execution

```python
import time

def timer(func):

    def inner():

        start = time.time()

        func()

        end = time.time()

        print("Time:", end - start)

    return inner
```

Used for:

* Performance measurement

---

# 9️⃣ Multiple Decorators

Yes, you can stack decorators.

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

```
Decor1
Decor2
Hello
```

---

## Execution Order

Bottom → Top

```
say = decor1(decor2(say))
```

Very common interview question.

---

# 🔟 Built-in Decorators (Must Know)

---

## @staticmethod

```python
class Test:

    @staticmethod
    def show():
        print("Static Method")
```

Does NOT use:

```
self
cls
```

---

## @classmethod

```python
class Test:

    @classmethod
    def show(cls):
        print("Class Method")
```

Uses:

```
cls
```

---

## @property

```python
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Used to access method like variable.

---

# 1️⃣1️⃣ functools.wraps (Advanced Topic ⭐)

Very important in real projects.

---

Problem:

Decorator hides original function name.

---

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

* Function name
* Docstring

---

# 1️⃣2️⃣ Decorator with Parameters (Advanced ⭐)

Very powerful concept.

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

```
Hello
Hello
Hello
```

---

# 🧾 Summary Table

| Term                | Meaning                             |
| ------------------- | ----------------------------------- |
| Decorator           | Function modifying another function |
| Decorating Function | Outer function                      |
| Decorated Function  | Original function                   |
| Inner Function      | Wrapper function                    |
| @ Symbol            | Shortcut syntax                     |
| *args, **kwargs     | Handles any arguments               |
| functools.wraps     | Keeps original metadata             |

---

# 🎯 Interview Questions You Must Prepare

These are **very common**:

1. What is a decorator?
2. Why decorators are used?
3. How does @ syntax work internally?
4. Why use `*args` and `**kwargs`?
5. What is decorator chaining?
6. What is `functools.wraps`?
7. Difference between decorator and function?

