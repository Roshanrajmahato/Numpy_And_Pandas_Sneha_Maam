# 1️⃣ Functions as First-Class Citizens in Python

## 📖 Definition

**In Python, functions are first-class citizens, which means functions are treated like any other variable (like int, string, list).**

That means functions can:

1️⃣ Be stored in variables
2️⃣ Be passed as arguments
3️⃣ Be returned from functions

This is the **core reason decorators work**.

---

# 🧠 First Understand: Function is an Object

In Python:

```python
def greet():
    print("Hello")
```

Python internally does:

```python
greet → function object stored in memory
```

So:

```python
print(greet)
```

Output:

```text
<function greet at 0x00000123>
```

That memory address proves:

✅ **Function is an object**

Just like:

```python
x = 10
name = "Roshan"
```

You can also do:

```python
f = greet
```

---

# 1️⃣ Functions Can Be Stored in Variables

## Example

```python
def greet():
    print("Hello Roshan")

# Store function in variable
f = greet

# Call using variable
f()
```

---

## Output

```text
Hello Roshan
```

---

## 🔍 Deep Explanation

This line:

```python
f = greet
```

Does NOT call function.

❌ Not:

```python
f = greet()
```

Instead:

```text
f → stores address of greet function
```

Memory View:

```text
greet  → 0x101
f      → 0x101
```

Both point to same function.

So:

```python
f()
```

Actually means:

```python
greet()
```

---

## 🎯 Interview Point

**Why don't we use parentheses?**

Because:

```python
greet
```

means:

👉 reference to function

But:

```python
greet()
```

means:

👉 execute function

Very important distinction.

---

# 2️⃣ Functions Can Be Passed as Arguments

This is **most important for decorators**.

---

## Example

```python
def greet(name):
    return f"Hello {name}"

def welcome(func):
    name = input("Enter Name: ")
    result = func(name)
    print(result)

welcome(greet)
```

---

## 🔍 Step-by-Step Execution

### Step 1

```python
welcome(greet)
```

This sends:

```text
greet → function reference
```

So:

```python
func = greet
```

---

### Step 2

```python
name = input("Enter Name: ")
```

User enters:

```text
Roshan
```

---

### Step 3

```python
result = func(name)
```

Since:

```python
func = greet
```

This becomes:

```python
result = greet("Roshan")
```

---

### Step 4

Output:

```text
Hello Roshan
```

---

## 🧠 Why This Matters

Because **decorators pass functions into other functions**.

Example:

```python
my_decorator(my_function)
```

Same concept.

---

## 🎯 Real-Life Example

Think of:

```text
function = recipe
argument = ingredient
```

You pass different recipes into same kitchen.

---

# 3️⃣ Functions Can Return Other Functions

This is called:

# 🧠 Closure (Important Concept)

---

## Example

```python
def outer():

    def inner():
        print("Hello from inner function")

    return inner
```

---

## Usage

```python
f = outer()

f()
```

---

## 🔍 Step-by-Step Execution

### Step 1

```python
f = outer()
```

Calls:

```python
outer()
```

Inside:

```python
return inner
```

So:

```text
f = inner
```

---

### Step 2

```python
f()
```

Means:

```python
inner()
```

Output:

```text
Hello from inner function
```

---

## Memory View

```text
outer → returns → inner function

f → points to inner
```

---

## 🎯 Interview Point

**Why return function?**

Because we want to:

✔ Modify behavior
✔ Wrap functions
✔ Create decorators

---

# 🧠 Combining All Three Concepts

Now see powerful example.

---

```python
def outer(func):

    def inner():
        print("Before execution")

        func()

        print("After execution")

    return inner


def say_hello():
    print("Hello Roshan")

# Pass function
decorated = outer(say_hello)

# Execute
decorated()
```

---

## Output

```text
Before execution
Hello Roshan
After execution
```

---

## This is actually:

# 🎯 A Decorator Without @ Symbol

---

# 🧠 Why Python Supports This?

Because Python supports:

## First-Class Functions

Other languages:

❌ C
❌ Java (partially)

Python supports fully.

---

# 🧪 Real-World Uses

These concepts are used in:

1️⃣ Decorators
2️⃣ Callbacks
3️⃣ Flask APIs
4️⃣ Django Middleware
5️⃣ Event Handling
6️⃣ Machine Learning pipelines
7️⃣ Async programming

Even in your **AI projects**, decorators are used in:

* Flask routes
* Logging
* Timing functions

---

# 🔥 Advanced Insight (Very Useful)

Functions are objects of:

```python
type(function)
```

Example:

```python
def test():
    pass

print(type(test))
```

Output:

```text
<class 'function'>
```

That proves:

✅ Function is object

---

# 🧾 Quick Summary Table

| Feature           | Meaning                           | Example               |
| ----------------- | --------------------------------- | --------------------- |
| Store in variable | Function assigned to variable     | `f = greet`           |
| Pass as argument  | Function sent to another function | `welcome(greet)`      |
| Return function   | Function returns another function | `return inner`        |
| Function object   | Function stored in memory         | `<function at 0x123>` |

---

# 🎯 Interview Questions From This Topic

You should prepare these:

1. What are first-class functions?
2. Why are functions called first-class citizens?
3. Can functions be stored in variables?
4. Can functions be passed as arguments?
5. Can functions return functions?
6. What is closure?
7. How do decorators depend on first-class functions?

These are **very common Python interview questions**.
