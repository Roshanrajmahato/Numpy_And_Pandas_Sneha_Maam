## 🔷 Define Encapsulation (with Example) — Interview Focused

**Encapsulation** is one of the **four pillars of OOP**, and this question is **very commonly asked in Python interviews**.

---

# 🧠 Definition (Interview Answer)

**Encapsulation** is the process of **wrapping data (variables) and methods (functions) into a single unit (class)** and **restricting direct access to data** to protect it from unauthorized modification.

👉 In simple words:
**Encapsulation = Data Hiding + Binding data and methods together**

---

# 🔷 Why is Encapsulation Used?

Encapsulation helps to:

✅ Protect data (Data Hiding)
✅ Improve security
✅ Control access to variables
✅ Make code modular and maintainable

---

# 🔷 Real-Life Example

## 🏦 ATM Machine Example

When you use an ATM:

* You **cannot directly access bank balance**
* You must use methods like:

  * withdraw()
  * deposit()
  * check_balance()

👉 This is **Encapsulation** — data is hidden and accessed through methods.

---

# 🔷 Example in Python (Very Important)

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc1 = BankAccount(1000)

acc1.deposit(500)

print(acc1.get_balance())
```

### Output

```
1500
```

---

# 🔷 Explanation of Example

```python
self.__balance
```

👉 `__balance` is a **private variable**
👉 It **cannot be accessed directly** from outside the class.

Access is done using:

```python
get_balance()
deposit()
```

This is called **data hiding**, which is part of encapsulation.

---

# 🔷 Trying to Access Private Variable (Important Concept)

```python
print(acc1.__balance)
```

❌ This will give an **error**.

Because:

👉 Private variables cannot be accessed directly.

---

# 🔷 Types of Access Specifiers in Python

Python supports **three types**:

| Type      | Symbol   | Access                             |
| --------- | -------- | ---------------------------------- |
| Public    | `name`   | Accessible everywhere              |
| Protected | `_name`  | Accessible inside class & subclass |
| Private   | `__name` | Accessible only inside class       |

---

# 🔷 Example with Private Variable

```python
class Student:

    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        return self.__marks


s1 = Student(80)

s1.set_marks(90)

print(s1.get_marks())
```

### Output

```
90
```

---

# 🔷 Key Features of Encapsulation

✔ Data hiding
✔ Access control
✔ Data protection
✔ Organized code
✔ Secure programs

---

# 🔷 Advantages of Encapsulation

✅ Improves security
✅ Prevents accidental modification
✅ Makes debugging easier
✅ Increases code flexibility
✅ Supports data hiding

---

# 🔷 Disadvantages of Encapsulation

❌ Slightly increases code length
❌ May reduce performance slightly

---

# 🔷 Short Interview Answer (30 Seconds)

If interviewer asks:

**"Define Encapsulation."**

You can say:

> Encapsulation is the process of wrapping data and methods into a single unit called a class and restricting direct access to the data. It helps achieve data hiding and improves security and maintainability of code.

---

# 🔷 Common Interview Questions

## 🎤 Q1: What is Encapsulation?

**Answer:**
Encapsulation is wrapping data and methods together into a class and restricting direct access to data.

---

## 🎤 Q2: How is Encapsulation achieved in Python?

**Answer:**
Encapsulation is achieved using **classes** and **private variables** (using double underscore `__`).

---

## 🎤 Q3: What is Data Hiding?

**Answer:**
Data hiding is restricting direct access to variables using private access specifiers.

---

# 🔷 Real Interview Tip ⭐

If asked:

**"Give a real-life example of Encapsulation."**

Best answer:

👉 **ATM Machine**
👉 **Bank Account System**
👉 **Login System**

These examples impress interviewers.

---

# 🚀 Next Important OOP Topics

After **Encapsulation**, the next most important topics are:

1️⃣ Inheritance
2️⃣ Polymorphism
3️⃣ Abstraction
4️⃣ Method Overriding
5️⃣ Multiple Inheritance
6️⃣ MRO (Method Resolution Order)

I recommend learning **Inheritance in Python** next — it's **very commonly asked** after Encapsulation.
