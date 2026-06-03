# **Exception Handling in Python — Detailed Notes**

# **1️⃣ Introduction to Exception Handling**

## **What is an Exception?**

An **Exception** is an **error or unexpected event** that occurs **during the execution of a program**.

When an exception occurs:

* The program **stops normal execution**
* Python generates an **error message**
* If not handled, the program **terminates abruptly**

---

## **Examples of Exceptions**

```python
print(10/0)
```

Output:

```
ZeroDivisionError: division by zero
```

Here:

* Dividing by **zero** is not allowed
* Python raises **ZeroDivisionError**

---

## **Common Built-in Exceptions**

| Exception         | Meaning                |
| ----------------- | ---------------------- |
| ZeroDivisionError | Division by zero       |
| ValueError        | Invalid value          |
| TypeError         | Wrong data type        |
| IndexError        | Invalid index          |
| KeyError          | Invalid dictionary key |
| FileNotFoundError | File not found         |

---

# **Exception Handler**

An **Exception Handler** is a **block of code** that executes when an exception occurs.

It **prevents program crash** and allows the program to continue.

---

# **2️⃣ The Four Main Blocks in Exception Handling**

Python provides **four main blocks**:

1. try
2. except
3. else
4. finally

---

# **🔹 try Block**

## **Definition**

The **try block** contains the **risky code** (code that may cause an error).

Python **first executes try block**.

---

## **Syntax**

```python
try:
    # Risky code
```

---

## **Example**

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)
```

Risky parts:

* Conversion to integer
* Division

---

# **🔹 except Block**

## **Definition**

The **except block** handles the exception raised in the try block.

It runs **only when an exception occurs**.

---

## **Syntax**

```python
try:
    # Risky code

except ExceptionName:
    # Handling code
```

---

## **Example**

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")
```

---

# **🔹 else Block**

## **Definition**

The **else block** executes **only if no exception occurs** in try.

Used for **success logic**.

---

## **Syntax**

```python
try:
    # Risky code

except Exception:
    # Error handling

else:
    # Executes if no error
```

---

## **Example**

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
```

---

# **🔹 finally Block**

## **Definition**

The **finally block** executes **always**, whether an exception occurs or not.

Used for:

* Closing files
* Closing database connections
* Releasing memory/resources

---

## **Syntax**

```python
try:
    # Risky code

except:
    # Handling code

finally:
    # Always runs
```

---

## **Example**

```python
try:
    f = open("data.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution completed")
```

---

# **3️⃣ Execution Flow of Exception Handling**

Python follows this order:

1. try block runs first
2. If error occurs → Python checks matching except block
3. Matching except executes
4. finally runs always
5. else runs only if no error

---

## **Flow Example**

```python
try:
    a = int(input())
    b = int(input())
    print(a/b)

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")

else:
    print("Successful execution")

finally:
    print("Program ended")
```

---

# **4️⃣ Multiple except Blocks**

You can handle **different errors separately**.

---

## **Example**

```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a/b)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Enter integer values only")
```

---

# **5️⃣ Nested Try-Except**

A **try block inside another try block**.

Used for handling **complex logic**.

---

## **Example: Division Retry Program**

```python
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    try:
        print(a/b)

    except ZeroDivisionError:
        print("b cannot be zero")

        b = int(input("Enter new b: "))
        print(a/b)

except ValueError:
    print("Enter valid integers")
```

---

# **Explanation**

Outer try handles:

```
ValueError
```

Inner try handles:

```
ZeroDivisionError
```

---

# **6️⃣ Using except Without Exception Name**

Handles **all exceptions**.

---

## **Syntax**

```python
except:
    # Handles all errors
```

---

## **Example**

```python
try:
    x = int(input())
    print(10/x)

except:
    print("Some error occurred")
```

⚠️ Not recommended in interviews — always specify exception.

---

# **7️⃣ Using Multiple Exceptions in One except**

You can combine exceptions.

---

## **Syntax**

```python
except (Exception1, Exception2):
```

---

## **Example**

```python
try:
    x = int(input())
    print(10/x)

except (ZeroDivisionError, ValueError):
    print("Invalid operation")
```

---

# **8️⃣ The raise Keyword**

## **Definition**

The **raise keyword** is used to **manually trigger an exception**.

Used when:

* Custom validation fails
* Invalid conditions occur

---

## **Syntax**

```python
raise ExceptionName("Message")
```

---

## **Example**

```python
age = int(input("Enter age: "))

if age < 18:
    raise Exception("Not eligible")

print("Eligible")
```

---

# **9️⃣ User-Defined Exceptions (Custom Exceptions)**

Python allows you to create **your own exceptions**.

Used for:

* Business logic validation
* Custom error messages

---

# **How to Create Custom Exception**

Step 1: Create class
Step 2: Inherit from Exception

---

## **Example: Age Validation**

```python
class InvalidAge(Exception):
    pass


def check_age(age):

    if age < 18:
        raise InvalidAge("Age is less than 18")

    else:
        print("Age is", age)


try:

    age = int(input("Enter age: "))
    check_age(age)

except InvalidAge as e:

    print("Error:", e)
```

---

# **Output**

If age = 15

```
Error: Age is less than 18
```

---

# **10️⃣ Example: Temperature Classification**

Custom exceptions based on temperature range.

---

## **Program**

```python
import random

class TemperatureTooHigh(Exception):
    pass

class TemperatureTooLow(Exception):
    pass

class ModerateTemperature(Exception):
    pass


temps = [10, 25, 35, 55]

temp = random.choice(temps)

try:

    if temp > 50:
        raise TemperatureTooHigh("Temperature is too high")

    elif temp < 30:
        raise TemperatureTooLow("Temperature is too low")

    else:
        raise ModerateTemperature("Temperature is moderate")

except TemperatureTooHigh as e:
    print(e)

except TemperatureTooLow as e:
    print(e)

except ModerateTemperature as e:
    print(e)
```

---

# **11️⃣ Exception Handling with finally (Resource Handling)**

Used for **closing costly resources**.

Example:

* Files
* Database connections
* Network connections

---

## **Example**

```python
try:

    file = open("data.txt", "r")

    data = file.read()

    print(data)

except FileNotFoundError:

    print("File does not exist")

finally:

    print("Closing file")
```

---

# **12️⃣ Summary Table**

| Block   | Purpose      | When Runs     |
| ------- | ------------ | ------------- |
| try     | Risky code   | First         |
| except  | Handle error | Only on error |
| else    | Success code | No error      |
| finally | Cleanup      | Always        |

---

# **13️⃣ Interview Questions on Exception Handling**

These are **very commonly asked**.

---

## **Basic Questions**

1. What is an exception?
2. What is exception handling?
3. Difference between error and exception?
4. What is try block?
5. What is except block?
6. What is finally block?
7. What is else block?

---

## **Intermediate Questions**

8. What is raise keyword?
9. How to create custom exception?
10. Difference between finally and else?
11. What happens if exception is not handled?
12. Can we use multiple except blocks?
13. What is nested try?

---

## **Advanced Questions**

14. What is Exception class?
15. How Python searches for except block?
16. Can finally run without except?
17. Can we write try without except?
18. What is exception chaining?

---

# **14️⃣ Very Important Exam Programs**

You should practice these:

✔ Division with exception
✔ Multiple except
✔ Nested try
✔ Custom exception
✔ File handling with finally
✔ raise keyword

---

# **If You're Preparing for Interviews**

Since you're already studying **Python advanced topics** (like decorators and file handling recently), the **most important interview topics** from Exception Handling are:

⭐ Custom Exceptions
⭐ raise keyword
⭐ finally usage
⭐ Multiple except blocks
⭐ Nested try-except
⭐ Exception hierarchy basics

---

# If you want next:

I can also provide:

✅ **50+ Exception Handling Interview Questions**
✅ **MCQs on Exception Handling**
✅ **Practice Coding Problems**
✅ **Real Interview Coding Scenarios**
