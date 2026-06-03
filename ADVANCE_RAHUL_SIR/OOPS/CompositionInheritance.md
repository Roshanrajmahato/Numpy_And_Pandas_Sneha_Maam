## 🔷 What is Composition in OOP? How is it Different from Inheritance?

# 🔷 Short Interview Answer (Best Version)

If interviewer asks:

**"What is composition in OOP?"**

You can say:

> Composition is an OOP concept where one class contains an object of another class to reuse its functionality. It represents a "has-a" relationship.

---

If interviewer asks:

**"Difference between composition and inheritance?"**

You can say:

> In inheritance, a class derives from another class representing an "is-a" relationship, while in composition, a class contains another object representing a "has-a" relationship. Composition is generally more flexible than inheritance.

---

# 🧠 What is Composition?

## ✅ Definition (Interview Answer)

**Composition** is an OOP concept where **one class contains an object of another class** to reuse its functionality.

👉 In simple words:
**Composition = "Has-A" Relationship**

Example:

* A **Car has an Engine**
* A **Computer has a CPU**

---

# 🔷 Real-Life Example

## 🚗 Car and Engine

A **Car** does not inherit from **Engine**,
but **Car contains an Engine**.

👉 Car **HAS-A** Engine
👉 This is **Composition**

---

# 🔷 Basic Example of Composition in Python

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()   # Composition

    def start_car(self):
        self.engine.start()


c = Car()

c.start_car()
```

### Output

```
Engine Started
```

---

# 🔷 Explanation

```python
self.engine = Engine()
```

👉 The **Car class creates an object of Engine**

So:

✔ Car **uses** Engine
✔ But Car is **not** Engine
✔ That is **Composition**

---

# 🔷 Types of Composition

There are two related concepts:

1️⃣ **Composition** (Strong relationship)
2️⃣ **Aggregation** (Weak relationship)

### Example:

* **Composition:** Human → Heart
  (Heart cannot exist independently)

* **Aggregation:** School → Student
  (Student can exist independently)

---

# 🔷 What is Inheritance?

Before comparing, quick recap:

## ✅ Definition

**Inheritance** allows a class to **reuse properties and methods from another class.**

👉 It represents:

**"Is-A" Relationship**

Example:

* Dog **is an** Animal
* Car **is a** Vehicle

---

# 🔷 Inheritance Example

```python
class Animal:

    def eat(self):
        print("Animal eats")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


d = Dog()

d.eat()
d.bark()
```

---

# 🔷 Composition vs Inheritance (Very Important)

| Feature      | Composition    | Inheritance       |
| ------------ | -------------- | ----------------- |
| Relationship | **Has-A**      | **Is-A**          |
| Reusability  | Uses objects   | Uses parent class |
| Flexibility  | More flexible  | Less flexible     |
| Coupling     | Loose coupling | Tight coupling    |
| Example      | Car has Engine | Dog is Animal     |
| Code Reuse   | By objects     | By subclassing    |

---

# 🔷 Key Difference (Most Important Concept)

👉 **Inheritance = IS-A relationship**
👉 **Composition = HAS-A relationship**

This is **frequently asked in interviews**.

---

# 🔷 Example Showing Difference

## Inheritance Example

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car(Engine):   # Inheritance

    pass


c = Car()

c.start()
```

👉 Car **is treated like Engine**

(Not realistic design)

---

## Composition Example (Better Design)

```python
class Engine:

    def start(self):
        print("Engine Started")


class Car:

    def __init__(self):
        self.engine = Engine()   # Composition

    def start_car(self):
        self.engine.start()


c = Car()

c.start_car()
```

👉 Car **has Engine**

(Realistic design)

---

# 🔷 Why Composition is Often Preferred Over Inheritance

This is a **very common interview concept**.

Composition is preferred because:

✅ More flexible
✅ Easier to modify
✅ Reduces dependency
✅ Improves code maintainability
✅ Supports better design

---

# 🔷 Real-Life Practical Example

## 🖥 Computer Example

```python
class CPU:

    def process(self):
        print("Processing data")


class Computer:

    def __init__(self):
        self.cpu = CPU()   # Composition

    def start(self):
        self.cpu.process()


pc = Computer()

pc.start()
```

---

# 🔷 Advantages of Composition

✔ More flexible design
✔ Loose coupling
✔ Better code reuse
✔ Easier maintenance
✔ Safer than inheritance

---

# 🔷 Disadvantages

❌ Slightly more complex structure
❌ More objects to manage

---

# 🔷 Most Important Interview Points ⭐

Remember these:

✔ Composition = HAS-A
✔ Inheritance = IS-A
✔ Composition uses objects
✔ Inheritance uses subclassing
✔ Composition is more flexible
✔ Prefer composition over inheritance in design

---

# 🚀 Next Highly Important OOP Topics

Since you're covering **advanced OOP interview preparation**, the next best topics are:

1️⃣ **Aggregation vs Composition** ⭐
2️⃣ **super() Function** ⭐
3️⃣ **Method Overriding** ⭐
4️⃣ **Duck Typing** ⭐
5️⃣ **SOLID Principles (Intro)**

**Recommended next topic:**
👉 **super() Function** — very commonly asked with inheritance questions.
