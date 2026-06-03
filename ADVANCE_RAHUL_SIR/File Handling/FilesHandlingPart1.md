# **Python File Handling — Detailed Explanation (Topic-Wise)**

# **1️⃣ Introduction to File Handling**

## **Definition**

**File Handling** is the process of storing data permanently in files so that it can be used later.

Python programs normally store data in **RAM (temporary memory)**, but files allow data to be stored in **secondary storage** like:

* Text files (.txt)
* CSV files (.csv)
* Binary files (.dat, .bin)

---

## **Purpose of File Handling**

✔ Store data permanently
✔ Read stored data later
✔ Share data between programs
✔ Maintain logs and records
✔ Save user input

---

## **Core Concepts**

### **1. Serialization**

**Definition:**
Serialization means **writing data from Python into a file**.

Example:

```python
f = open("data.txt", "w")
f.write("Hello World")
f.close()
```

Here:
Python → File

---

### **2. Deserialization**

**Definition:**
Deserialization means **reading data from file into Python**.

Example:

```python
f = open("data.txt", "r")
data = f.read()
print(data)
f.close()
```

Here:
File → Python

---

## **Basic Syntax**

```python
file_object = open(filename, mode)
```

Example:

```python
f = open("data.txt", "r")
```

---

## **Important Points**

✔ File handling makes data permanent
✔ open() connects Python to file
✔ Mode defines operation
✔ Always close file after use

---

## **Interview Questions**

**Q1:** What is file handling?
**Answer:** File handling is the process of storing and retrieving data from files permanently.

**Q2:** Difference between serialization and deserialization?

| Serialization | Deserialization |
| ------------- | --------------- |
| Write data    | Read data       |
| Python → File | File → Python   |

---

# **2️⃣ The open() Function & Read Mode**

## **open() Function**

Used to open a file.

```python
open(filename, mode)
```

Returns:

✔ **File Object**

Example:

```python
f = open("data.txt", "r")
print(type(f))
```

Output:

```
<class '_io.TextIOWrapper'>
```

---

## **Read Mode ('r')**

Used to **read data** from file.

```python
f = open("data.txt", "r")
```

If file doesn't exist:

❌ **FileNotFoundError**

---

## **readable() Method**

Checks if file is readable.

```python
f = open("data.txt", "r")

print(f.readable())
```

Output:

```
True
```

---

## **Important Points**

✔ Default mode is `'r'`
✔ File must exist
✔ Used for reading
✔ Returns file object

---

## **Interview Questions**

**Q:** What happens if file doesn't exist in 'r' mode?
**Answer:** Python raises `FileNotFoundError`.

---

# **3️⃣ Reading Methods & Navigation**

These methods control **how data is read**.

---

# **read() Method**

Reads entire file.

```python
f = open("data.txt", "r")
data = f.read()

print(data)
```

---

## **read(n)**

Reads **n characters**.

```python
f = open("data.txt", "r")

data = f.read(5)

print(data)
```

Output:

```
Hello
```

---

## **Important Points**

✔ Reads from cursor position
✔ Cursor moves forward
✔ Empty string when file ends

---

# **readline() Method**

Reads **one line**.

```python
f = open("data.txt", "r")

line = f.readline()

print(line)
```

---

# **readlines() Method**

Reads all lines into **list**.

```python
f = open("data.txt", "r")

lines = f.readlines()

print(lines)
```

Output:

```
['Hello\n', 'Python\n']
```

---

# **tell() Method**

Returns **cursor position**.

```python
f = open("data.txt", "r")

print(f.tell())
```

Output:

```
0
```

---

# **seek(n) Method**

Moves cursor to position.

```python
f.seek(5)
```

Moves cursor to index 5.

---

## **Important Points**

✔ Cursor controls reading
✔ tell() shows location
✔ seek() changes location

---

## **Interview Questions**

**Q:** Difference between read(), readline(), readlines()?

| Method      | Output        |
| ----------- | ------------- |
| read()      | Full file     |
| readline()  | One line      |
| readlines() | List of lines |

---

# **4️⃣ Connection Management**

Very important to avoid **data corruption**.

---

# **close() Method**

Closes file connection.

```python
f = open("data.txt", "r")

f.close()
```

---

## **Why close() is important**

✔ Saves data
✔ Frees memory
✔ Avoids corruption

---

# **with Keyword (Best Method)**

Automatically closes file.

```python
with open("data.txt", "r") as f:
    data = f.read()
```

No need:

```python
f.close()
```

---

## **Important Points**

✔ Always use `with`
✔ Prevents memory leak
✔ Safer method

---

## **Interview Questions**

**Q:** Why is `with` preferred over `close()`?

**Answer:**
Because it automatically closes file even if an error occurs.

---

# **5️⃣ Write and Append Modes**

Used for **serialization**.

---

# **Write Mode ('w')**

Overwrites file.

```python
f = open("data.txt", "w")

f.write("New Data")
```

If file exists:

❌ Old data deleted

If file doesn't exist:

✔ New file created

---

## **Append Mode ('a')**

Adds data at end.

```python
f = open("data.txt", "a")

f.write("More Data")
```

---

## **writable() Method**

Checks if writable.

```python
print(f.writable())
```

Output:

```
True
```

---

# **write() Method**

Writes single string.

```python
f.write("Hello")
```

---

# **writelines() Method**

Writes multiple lines.

```python
lines = ["Hello\n", "Python\n"]

f.writelines(lines)
```

---

## **Important Points**

✔ 'w' deletes old data
✔ 'a' keeps old data
✔ writelines() needs iterable

---

## **Interview Questions**

**Q:** Difference between 'w' and 'a'?

| Mode | Behavior   |
| ---- | ---------- |
| w    | Overwrites |
| a    | Appends    |

---

# **6️⃣ Advanced Modes — Plus (+) and X**

Very important for interviews.

---

# **x Mode**

Exclusive create mode.

```python
f = open("data.txt", "x")
```

If file exists:

❌ Error

```
FileExistsError
```

---

## **Use Case**

✔ Prevent overwriting important files

---

# **r+ Mode**

Read + Write.

File must exist.

```python
f = open("data.txt", "r+")
```

---

# **w+ Mode**

Write + Read.

Overwrites file.

```python
f = open("data.txt", "w+")
```

---

# **a+ Mode**

Append + Read.

```python
f = open("data.txt", "a+")
```

Cursor at end.

---

## **Important Rule**

After writing:

```python
seek(0)
```

Required before reading.

---

## **Example**

```python
f = open("data.txt", "w+")

f.write("Hello")

f.seek(0)

print(f.read())
```

---

## **Interview Questions**

**Q:** Why use seek(0) after write in w+ mode?

**Answer:**
Because cursor moves to end after writing.

---

# **7️⃣ Cursor (File Pointer) Logic — Very Important**

Most critical concept.

---

## **What is Cursor?**

Cursor is:

📍 Current position inside file

Like:

📖 Bookmark in book

---

## **Cursor Positions**

| Mode | Start Position |
| ---- | -------------- |
| r    | Beginning      |
| w    | Beginning      |
| a    | End            |

---

## **Cursor Movement**

After:

✔ read()
✔ write()

Cursor moves forward.

---

## **Example**

```python
f = open("data.txt", "r")

print(f.read(5))

print(f.tell())
```

---

## **Important Points**

✔ Cursor moves automatically
✔ seek() resets cursor
✔ tell() checks position

---

## **Interview Question**

**Q:** What is file pointer?

**Answer:**
It is the current position of cursor inside file.

---

# **8️⃣ Comparison of Writing Modes**

| Mode | If Exists | If Not Exists | Use Case      |
| ---- | --------- | ------------- | ------------- |
| w    | Overwrite | Create        | Reset file    |
| a    | Append    | Create        | Logging       |
| x    | Error     | Create        | Safe creation |

---

# **9️⃣ Assignment Logic — Replace Uppercase with @**

This is **classic interview/program question**.

---

## **Problem**

Replace all uppercase letters with `@`.

---

## **Steps**

1 Open file in r+
2 Read content
3 Replace uppercase
4 seek(0)
5 Write modified content

---

## **Code**

```python
with open("data.txt", "r+") as f:

    data = f.read()

    new_data = ""

    for ch in data:

        if ch.isupper():
            new_data += "@"

        else:
            new_data += ch

    f.seek(0)

    f.write(new_data)
```

---

## **Logic**

```text
HELLO → @@@@@
Hello → @ello
```

---

## **Interview Questions**

**Q:** Why use r+ mode here?

**Answer:**
To read and write in same file.

---

# **🔟 Summary of Methods**

## **Information Methods**

✔ tell()
✔ readable()
✔ writable()

---

## **Action Methods**

✔ read()
✔ write()
✔ seek()
✔ close()

---

## **Bulk Methods**

✔ readlines()
✔ writelines()

---

# **Most Important Interview Questions (Must Prepare)**

Here are **top questions** based on your notes:

1 What is file handling in Python?
2 What is serialization?
3 What is deserialization?
4 Explain open() function.
5 Difference between read(), readline(), readlines().
6 Difference between write() and writelines().
7 What is file pointer?
8 What is seek() and tell()?
9 Difference between 'w' and 'a'.
10 What is 'x' mode?
11 Difference between r+, w+, a+.
12 Why use with keyword?
13 What happens if file is not closed?
14 Why use seek(0) after writing?
15 Write program to replace uppercase letters.

---

# If you're preparing for interviews 👇

Since you're working toward **data science and Python roles**, next useful topics after this are:

* **Binary File Handling**
* **Pickle Module**
* **CSV File Handling**
* **Exception Handling in Files**
* **OS File Handling**

I can create:

✔ **Practice Questions**
✔ **Interview Coding Problems**
✔ **MCQs on File Handling**
✔ **Real Interview Scenarios**

Just say:
**"Give me Python File Handling interview coding questions"**
