# 🧠 What is `super()` Function?

## ✅ Definition (Interview Answer)

**`super()`** is a built-in function in Python used to **call methods or constructors of the parent class from the child class.**

👉 In simple words:
**`super()` lets a child class use parent class methods.**

---

# 🔷 Short Interview Answer (Best Version)

If interviewer asks:

**"What is super() in Python?"**

You can answer:

> The `super()` function in Python is used to call methods or constructors of the parent class from a child class. It helps in method overriding, avoids code duplication, and follows the method resolution order (MRO).

---
# 🔷 Why Do We Use `super()`?

`super()` is used to:

✅ Call parent class constructor
✅ Access parent class methods
✅ Avoid rewriting parent code
✅ Support multiple inheritance
✅ Maintain proper **MRO (Method Resolution Order)**

---

# 🔷 Basic Example of `super()` (Constructor Call)

```python
class Person:

    def __init__(self, name):
        self.name = name
        print("Person Constructor")


class Student(Person):

    def __init__(self, name, roll):
        super().__init__(name)   # Calling parent constructor
        self.roll = roll
        print("Student Constructor")


s = Student("Roshan", 101)
```

### Output

```
Person Constructor
Student Constructor
```

---

# 🔷 Explanation

```python
super().__init__(name)
```

👉 Calls the **parent class constructor**
👉 Avoids writing:

```python
Person.__init__(self, name)
```

---

# 🔷 Without Using `super()` (Not Recommended)

```python
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll):
        Person.__init__(self, name)   # Manual call
        self.roll = roll
```

⚠️ This works but is **not recommended**, especially in **multiple inheritance**.

---

# 🔷 Using `super()` to Call Parent Method

```python
class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        super().sound()   # Call parent method
        print("Dog barks")


d = Dog()

d.sound()
```

### Output

```
Animal makes sound
Dog barks
```

👉 Child extends parent behavior.

---

# 🔷 `super()` in Method Overriding (Very Important)

```python
class Employee:

    def show(self):
        print("Employee details")


class Manager(Employee):

    def show(self):
        super().show()
        print("Manager details")


m = Manager()

m.show()
```

---

# 🔷 `super()` in Multiple Inheritance (Important)

`super()` follows **MRO** to determine which parent method to call.

```python
class A:

    def show(self):
        print("Class A")


class B(A):

    def show(self):
        super().show()
        print("Class B")


class C(B):

    def show(self):
        super().show()
        print("Class C")


obj = C()

obj.show()
```

### Output

```
Class A
Class B
Class C
```

👉 `super()` follows **MRO order**.

---

# 🔷 How `super()` Works Internally

When you write:

```python
super().method()
```

Python internally:

✔ Finds next class in **MRO**
✔ Calls method from that class

---

# 🔷 How to Check MRO (Very Useful)

```python
print(ClassName.mro())
```

Example:

```python
print(Student.mro())
```

Output:

```
[Student, Person, object]
```

---

# 🔷 Advantages of `super()`

✔ Avoids code duplication
✔ Supports multiple inheritance
✔ Makes code cleaner
✔ Maintains proper MRO
✔ Improves maintainability

---

# 🔷 Common Mistakes

❌ Forgetting to call parent constructor
❌ Incorrect use in multiple inheritance
❌ Mixing manual parent calls with `super()`

---


# 🔷 Most Important Interview Points ⭐

Remember these:

✔ `super()` calls parent methods
✔ Used in inheritance
✔ Follows MRO
✔ Commonly used with constructors
✔ Cleaner than manual parent calls

---

# 🔷 Real-Life Analogy

## 👨‍👦 Parent–Child Example

A **child** inherits qualities from **parent**,
but can also **extend behavior**.

👉 `super()` = Asking parent to do their part first.

---

# 🔷 Practice Question (Interview Level)

**Create a class `Vehicle` with constructor and extend it in `Car` using `super()`.**

### Solution

```python
class Vehicle:

    def __init__(self, brand):
        self.brand = brand
        print("Vehicle Created")


class Car(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print("Car Created")


c = Car("Toyota", "Innova")
```

---

# 🚀 Next Highly Important Topics

Since you're systematically covering **Python OOP interview topics**, the next important ones are:

1️⃣ **Method Overriding** ⭐
2️⃣ **Operator Overloading** ⭐
3️⃣ **Duck Typing** ⭐
4️⃣ **Static vs Class Methods** ⭐
5️⃣ **SOLID Principles (Basics)**

**Recommended next topic:**
👉 **Duck Typing** — frequently asked in Python interviews.
