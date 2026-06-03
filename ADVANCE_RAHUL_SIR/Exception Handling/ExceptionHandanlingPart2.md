# 🧠 **Python Exception Handling Interview Questions**

I'll organize them into:

1️⃣ Basic Questions
2️⃣ Intermediate Questions
3️⃣ Advanced Questions
4️⃣ Coding-Based Questions
5️⃣ Output-Based Questions
6️⃣ Real Interview Scenario Questions

---

# **1️⃣ Basic Exception Handling Interview Questions**

These are **very frequently asked** in fresher interviews.

---

## **Q1. What is an Exception in Python?**

**Answer:**

An **exception** is an error that occurs **during program execution** and disrupts the normal flow of the program.

Example:

```python
print(10/0)
```

Raises:

```text
ZeroDivisionError
```

---

## **Q2. What is Exception Handling?**

**Answer:**

Exception Handling is a technique used to **handle runtime errors** so that the program **does not crash** and continues execution.

---

## **Q3. What is the purpose of try block?**

**Answer:**

The **try block** contains **risky code** that may generate an exception.

---

## **Q4. What is except block?**

**Answer:**

The **except block** handles the exception raised inside the try block.

---

## **Q5. What is finally block?**

**Answer:**

The **finally block** executes **always**, whether an exception occurs or not.

Used for:

* Closing files
* Closing database connections

---

## **Q6. What is else block in exception handling?**

**Answer:**

The **else block** executes **only when no exception occurs** in the try block.

---

## **Q7. What happens if an exception is not handled?**

**Answer:**

The program **terminates abruptly** and displays an error message.

---

## **Q8. Can we write try without except?**

**Answer:**

Yes, but **try must be followed by either except or finally**.

Valid:

```python
try:
    x = 10/0
finally:
    print("Done")
```

---

## **Q9. Can finally run without except?**

**Answer:**

Yes.

```python
try:
    print("Hello")
finally:
    print("Always runs")
```

---

## **Q10. What is a built-in exception?**

**Answer:**

Exceptions that are **predefined in Python**.

Examples:

* ZeroDivisionError
* ValueError
* TypeError
* IndexError

---

# **2️⃣ Intermediate Interview Questions**

These test **concept clarity**.

---

## **Q11. What is the difference between error and exception?**

| Error                    | Exception           |
| ------------------------ | ------------------- |
| Serious problem          | Runtime issue       |
| Cannot be handled easily | Can be handled      |
| Example: SyntaxError     | Example: ValueError |

---

## **Q12. How Python searches for except block?**

**Answer:**

Python checks **except blocks sequentially** from top to bottom and executes the **first matching exception**.

---

## **Q13. Can we have multiple except blocks?**

**Answer:**

Yes.

Example:

```python
try:
    x = int(input())
    print(10/x)

except ZeroDivisionError:
    print("Divide by zero")

except ValueError:
    print("Invalid input")
```

---

## **Q14. Can one except handle multiple exceptions?**

**Answer:**

Yes.

```python
except (ValueError, ZeroDivisionError):
    print("Error occurred")
```

---

## **Q15. What is the use of raise keyword?**

**Answer:**

The **raise keyword** is used to **manually generate an exception**.

Example:

```python
age = 15

if age < 18:
    raise Exception("Not eligible")
```

---

## **Q16. What is a user-defined exception?**

**Answer:**

An exception created by the programmer using **class inheritance** from Exception.

---

## **Q17. How to create a custom exception?**

**Answer:**

```python
class MyError(Exception):
    pass
```

---

## **Q18. What is nested try-except?**

**Answer:**

A **try block inside another try block**.

Used for handling multiple risky operations.

---

## **Q19. What is exception object?**

**Answer:**

An exception instance created when an error occurs.

Example:

```python
except ValueError as e:
    print(e)
```

Here:

```text
e → exception object
```

---

## **Q20. What is the difference between finally and else?**

| finally          | else                   |
| ---------------- | ---------------------- |
| Runs always      | Runs only if no error  |
| Used for cleanup | Used for success logic |

---

# **3️⃣ Advanced Interview Questions**

These are asked in **real technical interviews**.

---

## **Q21. What is exception hierarchy in Python?**

**Answer:**

All exceptions inherit from:

```text
BaseException
    |
    Exception
        |
        ValueError
        TypeError
        IndexError
        etc.
```

---

## **Q22. What is exception chaining?**

**Answer:**

When one exception occurs while handling another exception.

---

## **Q23. What is the use of finally in real-world applications?**

**Answer:**

Used to release **costly resources** like:

* File handles
* Database connections
* Network sockets

---

## **Q24. What is try-except-else-finally flow order?**

Order:

```text
try → except → else → finally
```

---

## **Q25. What happens if exception occurs inside finally?**

**Answer:**

It overrides the previous exception.

---

## **Q26. Can we write multiple finally blocks?**

**Answer:**

No.

Only **one finally block** is allowed per try.

---

## **Q27. Can except block be empty?**

**Answer:**

No.

It must contain at least one statement.

---

## **Q28. What is the difference between pass and raise?**

| pass         | raise               |
| ------------ | ------------------- |
| Does nothing | Generates exception |

---

## **Q29. Why should we avoid bare except?**

```python
except:
```

Because:

* It catches **all exceptions**
* Makes debugging difficult

---

## **Q30. What is re-raising an exception?**

**Answer:**

Throwing the same exception again.

```python
except Exception:
    raise
```

---

# **4️⃣ Coding Interview Questions**

These are **very important**.

---

## **Q31. Write a program to handle division by zero**

```python
try:
    a = int(input())
    b = int(input())

    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## **Q32. Handle invalid integer input**

```python
try:
    num = int(input())

except ValueError:
    print("Enter valid integer")
```

---

## **Q33. Write a program using finally**

```python
try:
    f = open("file.txt")

except FileNotFoundError:
    print("File missing")

finally:
    print("Execution completed")
```

---

## **Q34. Create a custom exception**

```python
class InvalidAge(Exception):
    pass

age = int(input())

if age < 18:
    raise InvalidAge("Not eligible")
```

---

## **Q35. Write nested try-except**

```python
try:
    a = int(input())
    b = int(input())

    try:
        print(a/b)

    except ZeroDivisionError:
        print("b cannot be zero")

except ValueError:
    print("Invalid input")
```

---

# **5️⃣ Output-Based Interview Questions**

These are **very common**.

---

## **Q36. What will be output?**

```python
try:
    print("A")
    x = 10/0

except ZeroDivisionError:
    print("B")

finally:
    print("C")
```

✅ **Output:**

```text
A
B
C
```

---

## **Q37. Output Question**

```python
try:
    print("Hello")

except:
    print("Error")

else:
    print("World")
```

✅ **Output:**

```text
Hello
World
```

---

## **Q38. Output Question**

```python
try:
    x = int("abc")

except ValueError:
    print("Invalid")

finally:
    print("Done")
```

✅ **Output:**

```text
Invalid
Done
```

---

# **6️⃣ Real Interview Scenario Questions**

These simulate **real-world problems**.

---

## **Q39. How do you handle file errors in Python?**

**Answer:**

Use:

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
```

---

## **Q40. Why use custom exceptions?**

**Answer:**

To handle **business logic errors**.

Example:

* Invalid age
* Invalid salary
* Invalid login

---

## **Q41. How to log exceptions in production?**

Use:

```python
import logging
logging.error("Error occurred")
```

---

## **Q42. When should we use finally?**

Use when:

* Resource must be released
* Cleanup is required

---

## **Q43. How to catch all exceptions safely?**

```python
except Exception as e:
    print(e)
```

---

# **Most Important Interview Questions (Must Prepare)**

These are **high-priority**.

⭐ What is Exception Handling?
⭐ try vs except vs finally
⭐ raise keyword
⭐ Custom Exception
⭐ Multiple except
⭐ Nested try
⭐ finally usage
⭐ Output-based questions

