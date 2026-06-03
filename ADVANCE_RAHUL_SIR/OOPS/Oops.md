## 🔷 What is Object-Oriented Programming (OOPs)?

**Object-Oriented Programming (OOPs)** is a **programming paradigm** based on the concept of **objects**, which contain **data (variables)** and **methods (functions)** that operate on that data.

In simple words:
👉 **OOPs organizes code using objects and classes to make programs reusable, secure, and easy to maintain.**

---

# 🧠 Interview Definition (Best to Say)

**Object-Oriented Programming (OOPs)** is a programming approach where software is designed using **objects and classes**, allowing features like **encapsulation, inheritance, polymorphism, and abstraction**, which improve **code reusability, modularity, and maintainability.**

---

# 🎯 Short Interview Answer (30–40 sec)

If interviewer asks:

**"Explain OOPs."**

You can say:

> Object-Oriented Programming is a programming paradigm based on classes and objects. It helps organize code into reusable components. OOPs mainly focuses on four pillars: Encapsulation, Inheritance, Polymorphism, and Abstraction. These concepts improve code reusability, security, and maintainability, making software easier to manage and scale.

# 🧱 Basic Terminologies in OOPs

## 1️⃣ Class

A **Class** is a **blueprint** or **template** used to create objects.

It defines:

* Variables (attributes)
* Functions (methods)

### Example (Python)

```python
class Student:
    name = "Roshan"
    
    def show(self):
        print("Student Name:", self.name)
```

👉 Here **Student** is a class.

---

## 2️⃣ Object

An **Object** is an **instance of a class**.

It represents a real-world entity.

### Example

```python
class Student:
    def show(self):
        print("Hello Student")

s1 = Student()   # Object created
s1.show()
```

👉 `s1` is an **object** of class **Student**.

---

# 🔷 Four Pillars of OOPs (Very Important for Interviews)

These are **most asked interview topics**.

---

# 1️⃣ Encapsulation 🔒

## Definition

**Encapsulation** means **wrapping data and methods into a single unit (class)** and restricting direct access to data.

👉 Also called **Data Hiding**.

## Why Needed?

* Protect data
* Control access
* Improve security

---

## Example

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(500)

print(acc.get_balance())
```

👉 `__balance` is **private** (encapsulation).

---

## Interview Point

**Encapsulation = Data hiding + Binding data & methods together**

---

# 2️⃣ Inheritance 🧬

## Definition

**Inheritance** allows one class to **reuse properties and methods** of another class.

👉 Promotes **code reuse**.

---

## Types of Inheritance (Python)

1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid

---

## Example

```python
class Parent:
    def show(self):
        print("Parent Method")

class Child(Parent):
    def display(self):
        print("Child Method")

c = Child()
c.show()
c.display()
```

👉 Child inherits Parent methods.

---

## Interview Point

**Inheritance = Reusability**

---

# 3️⃣ Polymorphism 🔁

## Definition

**Polymorphism** means **same function name behaves differently**.

👉 "Many forms"

---

## Types

1. Method Overloading
2. Method Overriding

---

## Example (Method Overriding)

```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()
```

Output:

```
Dog barks
```

👉 Same method, different behavior.

---

## Interview Point

**Polymorphism = Same method, different behavior**

---

# 4️⃣ Abstraction 🎭

## Definition

**Abstraction** means **hiding implementation details** and showing only essential features.

👉 Focus on **what**, not **how**.

---

## Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print("Area of Circle")

c = Circle()
c.area()
```

👉 User sees **area()**, not internal logic.

---

## Interview Point

**Abstraction = Hide complexity**

---

# 🔷 Additional Important OOP Concepts

These are also frequently asked.

---

# Constructor (**init**)

## Definition

A **constructor** is a special method automatically called when object is created.

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Roshan")

print(s1.name)
```

---

# Self Keyword

`self` refers to **current object**.

```python
self.name
```

Means:

```
current object's name
```

---

# Method Overriding

Child class modifies parent method.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

---

# Method Overloading (Python way)

Python supports overloading using **default arguments**.

```python
class Demo:

    def add(self, a, b=0):
        print(a + b)

d = Demo()

d.add(5)
d.add(5,10)
```

---

# 🔷 Real-Life Example of OOPs

Imagine:

## 🚗 Car System

**Class** → Car
**Object** → BMW, Audi

Properties:

* color
* speed

Methods:

* start()
* stop()

Example:

```python
class Car:

    def __init__(self, color):
        self.color = color

    def start(self):
        print("Car Started")

car1 = Car("Red")

car1.start()
```

---

# 🔷 Advantages of OOPs (Interview Favorite)

✅ Code Reusability
✅ Security (Data Hiding)
✅ Easy Maintenance
✅ Modularity
✅ Scalability
✅ Real-world modeling

---

# 🔷 Disadvantages of OOPs

❌ More memory usage
❌ Complex design
❌ Slower than procedural in small programs

---

# 🔷 OOPs vs Procedural Programming

| Feature     | OOP          | Procedural |
| ----------- | ------------ | ---------- |
| Focus       | Objects      | Functions  |
| Security    | High         | Low        |
| Reusability | High         | Low        |
| Maintenance | Easy         | Hard       |
| Example     | Python, Java | C          |

---

# 🔷 Real Interview Questions on OOPs

You should prepare these answers:

1. What is OOPs?
2. What are the four pillars of OOPs?
3. Difference between **Class and Object**
4. What is **Encapsulation**?
5. What is **Inheritance**?
6. What is **Polymorphism**?
7. What is **Abstraction**?
8. Difference between **Overloading vs Overriding**
9. What is a **Constructor**?
10. What is **self** in Python?

---

---

# If You're Preparing for Python Interviews (Important for You)

Since you're preparing **Python interview topics**, next recommended OOP topics are:

* Class vs Object
* Inheritance types
* Method Overriding
* MRO (Method Resolution Order)
* super() function
* Abstract Class
* Multiple Inheritance

I can explain these **next in deep interview style** if you want.
