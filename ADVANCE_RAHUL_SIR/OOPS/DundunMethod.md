## 🔷 What Are Dunder (Magic) Methods in Python?

# 🔷 Short Interview Answer (Most Useful)

If interviewer asks:

**"What are dunder methods?"**

You can say:

> Dunder methods, also known as magic methods, are special methods in Python that start and end with double underscores. They allow objects to define special behaviors such as initialization, string representation, operator overloading, and comparison operations.

---

# 🧠 Definition (Interview Answer)

**Dunder methods** (short for **Double UnderScore methods**) are **special methods in Python that start and end with double underscores (`__`)**.
They allow objects to **behave like built-in types** and define how objects interact with operators and built-in functions.

👉 In simple words:
**Dunder methods are special methods that give special behavior to objects.**

---

# 🔷 Why Are They Called "Magic Methods"?

They are called **magic methods** because:

✨ Python **automatically calls them**
✨ They add **special functionality** to classes
✨ They allow **operator overloading**

---

# 🔷 Why Are Dunder Methods Used?

They are used to:

✅ Initialize objects
✅ Represent objects as strings
✅ Overload operators
✅ Customize object behavior
✅ Work with built-in functions

---

# 🔷 Common Dunder Methods (Very Important)

Here are **frequently asked magic methods** in interviews:

| Method     | Purpose                         |
| ---------- | ------------------------------- |
| `__init__` | Constructor (initialize object) |
| `__str__`  | String representation for users |
| `__repr__` | Official string representation  |
| `__len__`  | Returns length                  |
| `__add__`  | Addition operator (+)           |
| `__sub__`  | Subtraction operator (-)        |
| `__mul__`  | Multiplication (*)              |
| `__eq__`   | Equality comparison             |
| `__lt__`   | Less than comparison            |
| `__del__`  | Destructor                      |

---

# 🔷 Example 1: `__init__()` Method

You already learned this — it's the **most common dunder method**.

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Roshan")

print(s1.name)
```

👉 `__init__()` runs automatically when object is created.

---

# 🔷 Example 2: `__str__()` Method

Used to define how object prints.

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"

s1 = Student("Roshan")

print(s1)
```

### Output

```
Student Name: Roshan
```

👉 Without `__str__()`, Python prints memory address.

---

# 🔷 Example 3: `__len__()` Method

Used with `len()` function.

```python
class MyList:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyList([1, 2, 3, 4])

print(len(obj))
```

### Output

```
4
```

👉 Python internally calls `__len__()`.

---

# 🔷 Example 4: Operator Overloading (`__add__()`)

Dunder methods allow **operator overloading**.

```python
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)
```

### Output

```
30
```

👉 `+` operator calls `__add__()`.

---

# 🔷 Example 5: `__eq__()` Method (Comparison)

```python
class Student:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(90)
s2 = Student(90)

print(s1 == s2)
```

### Output

```
True
```

👉 `==` calls `__eq__()`.

---

# 🔷 How Python Uses Dunder Methods Internally

When you write:

```python
a + b
```

Python internally does:

```python
a.__add__(b)
```

---

When you write:

```python
len(obj)
```

Python does:

```python
obj.__len__()
```

---

# 🔷 Important Categories of Dunder Methods

## 1️⃣ Object Initialization

* `__init__`
* `__new__`
* `__del__`

---

## 2️⃣ String Representation

* `__str__`
* `__repr__`

---

## 3️⃣ Operator Overloading

* `__add__`
* `__sub__`
* `__mul__`
* `__truediv__`

---

## 4️⃣ Comparison Operators

* `__eq__`
* `__lt__`
* `__gt__`

---

## 5️⃣ Container Methods

* `__len__`
* `__getitem__`
* `__setitem__`

---

# 🔷 Real-Life Example

Think of:

📦 **Custom Box Class**

You want:

* `len(box)` → number of items
* `box1 + box2` → combine boxes

👉 Use dunder methods to define behavior.

---

# 🔷 Advantages of Dunder Methods

✅ Operator overloading
✅ Better object representation
✅ Custom object behavior
✅ Makes classes behave like built-ins
✅ Cleaner syntax

---

# 🔷 Common Interview Questions

## 🎤 Q1: What are Dunder Methods?

**Answer:**

Dunder methods are special methods in Python that start and end with double underscores. They define special behaviors for objects, such as initialization, operator overloading, and string representation.

---

## 🎤 Q2: Why are they called magic methods?

**Answer:**

They are called magic methods because Python automatically invokes them to perform specific operations.

---

## 🎤 Q3: Give examples of common dunder methods.

**Answer:**

Some common dunder methods are:

* `__init__()`
* `__str__()`
* `__add__()`
* `__len__()`
* `__eq__()`

---


# 🔷 Very Important Interview Tip ⭐

If interviewer asks:

**"Give examples of dunder methods."**

Say:

* `__init__()` → constructor
* `__str__()` → string representation
* `__len__()` → length
* `__add__()` → addition
* `__eq__()` → comparison

These **5 methods** are most commonly asked.

---

# 🚀 Next Highly Important Topic

Since you're progressing through **advanced OOP topics**, the next important ones are:

1️⃣ **Method Overriding** ⭐
2️⃣ **Polymorphism** ⭐
3️⃣ **super() Function**
4️⃣ **MRO (Method Resolution Order)**
5️⃣ **Operator Overloading**

I recommend learning **Method Overriding** next — it's **very commonly paired with inheritance questions** in interviews.
