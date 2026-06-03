## 🔷 Difference Between Instance Methods, Class Methods, and Static Methods (Very Important Interview Topic)

This topic is **frequently asked in Python OOP interviews**, especially after **instance vs class variables**.

---

# 🧠 Overview

In Python, there are **three types of methods**:

1️⃣ Instance Method
2️⃣ Class Method
3️⃣ Static Method

Each method is used for **different purposes**.

---

# 🔷 1️⃣ Instance Method

## ✅ Definition (Interview Answer)

An **instance method** is a method that **works with instance variables** and **belongs to an object**.
It takes **`self`** as the first parameter.

👉 Most commonly used method.

---

## 🔧 Syntax

```python
class ClassName:

    def method_name(self):
        # Instance method
```

---

## 🔷 Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show(self):   # Instance method
        print("Name:", self.name)

s1 = Student("Roshan")

s1.show()
```

---

## 🔷 Why Use Instance Methods?

Use when:

✅ Working with object data
✅ Accessing instance variables
✅ Object-specific behavior

---

# 🔷 2️⃣ Class Method

## ✅ Definition (Interview Answer)

A **class method** is a method that **works with class variables** and **belongs to the class**, not objects.
It takes **`cls`** as the first parameter.

👉 Uses **`@classmethod` decorator**.

---

## 🔧 Syntax

```python
class ClassName:

    @classmethod
    def method_name(cls):
        # Class method
```

---

## 🔷 Example

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name

Student.change_school("XYZ School")

print(Student.school)
```

---

## 🔷 Why Use Class Methods?

Use when:

✅ Modifying class variables
✅ Working with class-level data
✅ Creating factory methods

---

# 🔷 3️⃣ Static Method

## ✅ Definition (Interview Answer)

A **static method** is a method that **does not depend on instance or class variables**.
It behaves like a **normal function inside a class**.

👉 Uses **`@staticmethod` decorator**.

---

## 🔧 Syntax

```python
class ClassName:

    @staticmethod
    def method_name():
        # Static method
```

---

## 🔷 Example

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)

print(result)
```

---

## 🔷 Why Use Static Methods?

Use when:

✅ Logic is related to class
✅ No instance or class data needed
✅ Utility/helper functions

---

# 🔷 All Three Methods in One Example (Very Important)

```python
class Employee:

    company = "TCS"   # Class variable

    def __init__(self, name):
        self.name = name   # Instance variable

    # Instance Method
    def show(self):
        print("Name:", self.name)

    # Class Method
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # Static Method
    @staticmethod
    def greet():
        print("Welcome to Company")

e1 = Employee("Roshan")

e1.show()                      # Instance method
Employee.change_company("Infosys")   # Class method
Employee.greet()               # Static method
```

---

# 🔷 Key Differences Table (Very Important)

| Feature              | Instance Method    | Class Method    | Static Method    |
| -------------------- | ------------------ | --------------- | ---------------- |
| First Parameter      | `self`             | `cls`           | None             |
| Works With           | Instance variables | Class variables | No variables     |
| Decorator            | No decorator       | `@classmethod`  | `@staticmethod`  |
| Called Using         | Object             | Class/Object    | Class/Object     |
| Access Instance Data | ✅ Yes              | ❌ No            | ❌ No             |
| Access Class Data    | ✅ Yes              | ✅ Yes           | ❌ No             |
| Purpose              | Object behavior    | Class behavior  | Utility function |

---

# 🔷 Memory Understanding

When:

```python
e1.show()
```

Python internally does:

```python
Employee.show(e1)
```

So:

👉 `e1` becomes `self`.

---

# 🔷 Real-Life Example

## 🏦 Bank System

Instance Method:

```python
def deposit(self, amount)
```

→ Works on individual account.

Class Method:

```python
@classmethod
def change_interest_rate(cls)
```

→ Changes interest rate for all accounts.

Static Method:

```python
@staticmethod
def calculate_tax(amount)
```

→ Utility calculation.

---

# 🔷 Common Interview Questions

## 🎤 Q1: What is an Instance Method?

**Answer:**

An instance method is a method that works with instance variables and takes `self` as the first parameter.

---

## 🎤 Q2: What is a Class Method?

**Answer:**

A class method works with class variables and takes `cls` as the first parameter. It is defined using the `@classmethod` decorator.

---

## 🎤 Q3: What is a Static Method?

**Answer:**

A static method does not depend on instance or class variables and behaves like a normal function inside a class.

---

## 🎤 Q4: Can static methods access class variables?

❌ No (unless explicitly passed)

---

## 🎤 Q5: Can instance methods access class variables?

✅ Yes

---

# 🔷 Short Interview Answer (Most Useful)

If interviewer asks:

**"Difference between instance, class, and static methods?"**

You can say:

> Instance methods work with object data and take `self` as the first parameter. Class methods work with class data and take `cls` as the first parameter, using the `@classmethod` decorator. Static methods do not work with class or instance data and use the `@staticmethod` decorator.

---

# 🔷 When to Use Each (Very Practical)

Use:

✔ **Instance Method** → Object-specific work
✔ **Class Method** → Class-level work
✔ **Static Method** → Utility/helper work

---

# 🚀 Next Most Important Topics for Interviews

Based on your OOP preparation, the **next high-priority topics** are:

1. **Method Overloading vs Method Overriding** ⭐
2. **Inheritance in Python** ⭐
3. **`super()` Function**
4. **MRO (Method Resolution Order)**

I recommend learning **Method Overriding** next — it’s **very commonly asked** in coding interviews.
