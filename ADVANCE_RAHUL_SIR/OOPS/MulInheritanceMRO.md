## 🔷 What is Multiple Inheritance and How Does Python Handle Conflicts (MRO)?

# 🔷 Short Interview Answer (Best Version)

If interviewer asks:

**"What is multiple inheritance and how does Python handle conflicts?"**

You can answer:

> Multiple inheritance is a feature where a class inherits from more than one parent class. When conflicts occur, Python resolves them using Method Resolution Order (MRO), which defines the order in which classes are searched for methods. Python uses the C3 Linearization algorithm to determine this order.

---

# 🧠 What is Multiple Inheritance?

## ✅ Definition (Interview Answer)

**Multiple Inheritance** is a feature in Python where a **child class inherits from more than one parent class.**

👉 In simple words:
**One child class + Multiple parent classes = Multiple Inheritance**

---

# 🔷 Syntax of Multiple Inheritance

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

👉 `Child` inherits from **both Parent1 and Parent2**.

---

# 🔷 Basic Example of Multiple Inheritance

```python
class Father:

    def skills(self):
        print("Father: Gardening")


class Mother:

    def talents(self):
        print("Mother: Cooking")


class Child(Father, Mother):

    def hobbies(self):
        print("Child: Playing")


c = Child()

c.skills()
c.talents()
c.hobbies()
```

### Output

```
Father: Gardening
Mother: Cooking
Child: Playing
```

👉 Child gets properties from **both parents**.

---

# 🔷 Problem in Multiple Inheritance (Conflict)

Conflict happens when:

👉 **Two parent classes have methods with the same name**

Example:

```python
class A:

    def show(self):
        print("Class A")


class B:

    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()

obj.show()
```

### Question:

Which `show()` method should run?

* Class A?
* Class B?

👉 This creates a **conflict problem**.

---

# 🔷 How Python Solves Conflict → MRO

## What is MRO?

## ✅ Definition

**MRO (Method Resolution Order)** is the **order in which Python searches classes** to find a method.

👉 It decides **which method will be executed**.

---

# 🔷 MRO Rule in Python

Python uses:

## ⭐ **C3 Linearization Algorithm**

But for interviews, remember:

👉 **Python searches from Left to Right.**

---

# 🔷 Example Showing MRO

```python
class A:

    def show(self):
        print("Class A")


class B:

    def show(self):
        print("Class B")


class C(A, B):
    pass


obj = C()

obj.show()
```

### Output

```
Class A
```

👉 Because:

```python
class C(A, B)
```

Python checks:

```
C → A → B
```

So **A is executed first**.

---

# 🔷 How to Check MRO in Python

Use:

```python
ClassName.mro()
```

or

```python
help(ClassName)
```

---

# 🔷 Example Using `mro()`

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.mro())
```

### Output

```
[C, A, B, object]
```

👉 This is the **method search order**.

---

# 🔷 Diamond Problem (Very Important)

This is the **most famous multiple inheritance problem**.

```
       A
      / \
     B   C
      \ /
       D
```

Example:

```python
class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


obj = D()

obj.show()
```

### Output

```
Class A
```

👉 Python avoids calling A twice using **MRO**.

---

# 🔷 Diamond Problem MRO Order

```python
print(D.mro())
```

Output:

```
[D, B, C, A, object]
```

👉 Python follows **C3 Linearization**.

---

# 🔷 C3 Linearization (Interview Concept)

You don't need deep math.

Just remember:

Python ensures:

✅ Parent order preserved
✅ No class repeated
✅ Logical method search

---

# 🔷 Advantages of Multiple Inheritance

✔ Code reuse
✔ Flexible design
✔ Combines multiple behaviors
✔ Supports polymorphism

---

# 🔷 Disadvantages

❌ Complexity increases
❌ Debugging becomes harder
❌ Conflict problems possible

---

# 🔷 Most Important Interview Points ⭐

Remember these:

✔ Multiple inheritance = Multiple parent classes
✔ Conflict occurs when methods have same name
✔ Python resolves conflict using **MRO**
✔ Python uses **C3 Linearization**
✔ Check MRO using `ClassName.mro()`

---

# 🔷 Practice Interview Question

**Write a Python program demonstrating multiple inheritance and print MRO.**

### Solution

```python
class A:

    def show(self):
        print("Class A")


class B:

    def display(self):
        print("Class B")


class C(A, B):
    pass


obj = C()

obj.show()
obj.display()

print(C.mro())
```

---

# 🚀 Next Important Topics (Highly Recommended)

Since you're preparing **Python OOP interview topics**, the next most important ones are:

1️⃣ **super() Function** ⭐
2️⃣ **Method Overriding** ⭐
3️⃣ **Operator Overloading** ⭐
4️⃣ **Duck Typing**
5️⃣ **Composition vs Inheritance**

**Best next topic:**
👉 **super() Function** — almost always asked with inheritance and MRO.
