## 🔷 What is Inheritance? (With Example) — Interview Focused

**Inheritance** is one of the **four major pillars of OOP**, and it is **very commonly asked in Python interviews**.

---

# 🧠 Definition (Interview Answer)

**Inheritance** is a mechanism in Object-Oriented Programming where **one class acquires the properties and methods of another class**.

👉 In simple words:
**Inheritance allows one class to reuse the code of another class.**

---

# 🔷 Why Use Inheritance?

Inheritance helps to:

✅ Reuse existing code
✅ Reduce code duplication
✅ Improve maintainability
✅ Support hierarchical classification
✅ Extend existing functionality

---

# 🔷 Terminology in Inheritance

| Term          | Meaning                                  |
| ------------- | ---------------------------------------- |
| Parent Class  | The class whose properties are inherited |
| Child Class   | The class that inherits properties       |
| Base Class    | Another name for Parent class            |
| Derived Class | Another name for Child class             |

---

# 🔷 Syntax of Inheritance in Python

```python
class Parent:
    # Parent class code

class Child(Parent):
    # Child class code
```

👉 Child class **inherits** Parent class.

---

# 🔷 Basic Example of Inheritance (Very Important)

```python
class Parent:

    def show(self):
        print("This is Parent class")


class Child(Parent):

    def display(self):
        print("This is Child class")


c1 = Child()

c1.show()      # Inherited method
c1.display()   # Child method
```

### Output

```
This is Parent class
This is Child class
```

👉 The **Child class uses Parent method**, showing inheritance.

---

# 🔷 Real-Life Example (Interview Friendly)

## 🚗 Vehicle Example

**Parent Class → Vehicle**
**Child Class → Car**

Vehicle properties:

* speed
* fuel

Car properties:

* brand
* model

Car can reuse Vehicle features.

---

### Code Example

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car is Driving")


car1 = Car()

car1.start()   # Inherited method
car1.drive()   # Own method
```

---

# 🔷 Types of Inheritance in Python (Important)

Python supports **five types**:

1️⃣ Single Inheritance
2️⃣ Multiple Inheritance
3️⃣ Multilevel Inheritance
4️⃣ Hierarchical Inheritance
5️⃣ Hybrid Inheritance

---

# 🔷 1️⃣ Single Inheritance

One parent → One child

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

c = Child()
c.show()
```

---

# 🔷 2️⃣ Multiple Inheritance

Multiple parents → One child

```python
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()

c.skill1()
c.skill2()
```

---

# 🔷 3️⃣ Multilevel Inheritance

Grandparent → Parent → Child

```python
class Grandparent:
    def gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")

obj = Child()

obj.gp()
obj.p()
obj.c()
```

---

# 🔷 4️⃣ Hierarchical Inheritance

One parent → Multiple children

```python
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

---

# 🔷 5️⃣ Hybrid Inheritance

Combination of multiple types.

(Combination of single + multiple etc.)

---

# 🔷 Method Overriding in Inheritance (Very Important)

Child class modifies parent method.

```python
class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        print("Child method")


c = Child()

c.show()
```

### Output

```
Child method
```

👉 Child method overrides parent method.

---

# 🔷 Using `super()` Function

Used to call parent class method.

```python
class Parent:

    def show(self):
        print("Parent method")


class Child(Parent):

    def show(self):
        super().show()
        print("Child method")


c = Child()

c.show()
```

---

# 🔷 Advantages of Inheritance

✅ Code Reusability
✅ Reduces redundancy
✅ Easy maintenance
✅ Improves readability
✅ Supports polymorphism

---

# 🔷 Disadvantages of Inheritance

❌ Increases complexity
❌ Tight coupling between classes
❌ Hard to debug large hierarchies

---

# 🔷 Real-Life Examples of Inheritance

Very useful in interviews:

* Vehicle → Car, Bike
* Animal → Dog, Cat
* Employee → Manager, Developer
* Shape → Circle, Rectangle

---

# 🔷 Short Interview Answer (30–40 sec)

If interviewer asks:

**"What is Inheritance?"**

You can say:

> Inheritance is a feature of Object-Oriented Programming where one class inherits the properties and methods of another class. It promotes code reusability and reduces redundancy. The class that inherits is called the child class, and the class being inherited from is called the parent class.

---

# 🔷 Common Interview Questions

## 🎤 Q1: What is Inheritance?

**Answer:**
Inheritance allows a class to acquire properties and methods of another class.

---

## 🎤 Q2: What are the types of inheritance in Python?

**Answer:**
Python supports Single, Multiple, Multilevel, Hierarchical, and Hybrid inheritance.

---

## 🎤 Q3: What is the use of inheritance?

**Answer:**
It improves code reusability and reduces redundancy.

---

# 🔷 Practice Interview Question

**Create a Parent class `Animal` with method `eat()` and Child class `Dog` with method `bark()`.**

### Solution

```python
class Animal:

    def eat(self):
        print("Animal eats food")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()
```

---

# 🚀 Next Most Important Topic

After **Inheritance**, the **next very important interview topics** are:

1️⃣ **Polymorphism** ⭐
2️⃣ **Method Overriding** ⭐
3️⃣ **super() function**
4️⃣ **MRO (Method Resolution Order)**

I recommend learning **Polymorphism** next — it is **almost always asked after Inheritance** in interviews.
