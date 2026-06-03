Great 👍 Since you're preparing for **Python interviews (especially for data science / developer roles)**, here are **Python File Handling Interview Coding Questions** from **basic → advanced**, exactly the way interviewers ask them.

I'll include:

✔ Problem
✔ Explanation
✔ Solution Code
✔ Interview Tip

---

# **Python File Handling — Interview Coding Questions**

# **Level 1️⃣ — Basic File Handling**

These are **very common fresher-level questions**.

---

# **Q1. Write a program to read entire file content**

## **Problem**

Read all content from a file and display it.

---

## **Code**

```python
with open("data.txt", "r") as f:

    content = f.read()

    print(content)
```

---

## **Explanation**

* `"r"` → read mode
* `read()` → reads full file
* `with` → auto closes file

---

## **Interview Tip**

Interviewers check:

✔ Do you use `with`
✔ Do you know `read()`

---

# **Q2. Read file line by line**

## **Problem**

Print each line separately.

---

## **Code**

```python
with open("data.txt", "r") as f:

    for line in f:

        print(line.strip())
```

---

## **Explanation**

* Loop reads line-by-line
* `strip()` removes newline

---

## **Interview Tip**

This method is:

✔ Memory efficient
✔ Used in large files

---

# **Q3. Count number of lines in a file**

## **Problem**

Count total lines.

---

## **Code**

```python
count = 0

with open("data.txt", "r") as f:

    for line in f:
        count += 1

print("Total lines:", count)
```

---

## **Interview Tip**

Very frequently asked.

---

# **Q4. Count number of words in file**

## **Code**

```python
with open("data.txt", "r") as f:

    text = f.read()

    words = text.split()

    print("Total words:", len(words))
```

---

# **Q5. Count number of characters**

## **Code**

```python
with open("data.txt", "r") as f:

    text = f.read()

    print("Characters:", len(text))
```

---

# **Level 2️⃣ — String Processing in Files**

These are **most common interview questions**.

---

# **Q6. Count uppercase letters**

## **Code**

```python
count = 0

with open("data.txt", "r") as f:

    data = f.read()

    for ch in data:

        if ch.isupper():
            count += 1

print("Uppercase letters:", count)
```

---

# **Q7. Replace uppercase letters with '@'**

(Your assignment question — very important)

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

## **Interview Tip**

They test:

✔ `r+` mode
✔ `seek(0)` logic

---

# **Q8. Find number of vowels**

## **Code**

```python
vowels = "aeiouAEIOU"

count = 0

with open("data.txt", "r") as f:

    data = f.read()

    for ch in data:

        if ch in vowels:
            count += 1

print("Vowels:", count)
```

---

# **Q9. Find number of digits**

## **Code**

```python
count = 0

with open("data.txt", "r") as f:

    data = f.read()

    for ch in data:

        if ch.isdigit():
            count += 1

print("Digits:", count)
```

---

# **Level 3️⃣ — Writing & Appending**

Very commonly asked.

---

# **Q10. Write user input into file**

## **Code**

```python
data = input("Enter text: ")

with open("data.txt", "w") as f:

    f.write(data)
```

---

# **Q11. Append text into file**

## **Code**

```python
data = input("Enter text: ")

with open("data.txt", "a") as f:

    f.write(data + "\n")
```

---

# **Q12. Copy content from one file to another**

Very popular question.

---

## **Code**

```python
with open("source.txt", "r") as f1:

    data = f1.read()

with open("target.txt", "w") as f2:

    f2.write(data)
```

---

## **Interview Tip**

This question appears **very often**.

---

# **Level 4️⃣ — Intermediate File Problems**

These test **logic + file handling**.

---

# **Q13. Reverse file content**

## **Code**

```python
with open("data.txt", "r") as f:

    data = f.read()

rev = data[::-1]

with open("data.txt", "w") as f:

    f.write(rev)
```

---

# **Q14. Find longest word**

## **Code**

```python
longest = ""

with open("data.txt", "r") as f:

    words = f.read().split()

    for word in words:

        if len(word) > len(longest):
            longest = word

print("Longest word:", longest)
```

---

# **Q15. Remove blank lines**

Very commonly asked.

---

## **Code**

```python
with open("data.txt", "r") as f:

    lines = f.readlines()

with open("data.txt", "w") as f:

    for line in lines:

        if line.strip() != "":
            f.write(line)
```

---

# **Level 5️⃣ — Advanced Interview Questions**

These appear in **experienced or strong fresher interviews**.

---

# **Q16. Count frequency of each word**

## **Code**

```python
freq = {}

with open("data.txt", "r") as f:

    words = f.read().split()

    for word in words:

        if word in freq:
            freq[word] += 1

        else:
            freq[word] = 1

print(freq)
```

---

# **Q17. Merge two files**

## **Code**

```python
with open("file1.txt", "r") as f1:

    data1 = f1.read()

with open("file2.txt", "r") as f2:

    data2 = f2.read()

with open("merged.txt", "w") as f3:

    f3.write(data1 + "\n" + data2)
```

---

# **Q18. Check if file exists**

Very useful in real applications.

---

## **Code**

```python
import os

if os.path.exists("data.txt"):

    print("File exists")

else:

    print("File not found")
```

---

# **Q19. Read only first N lines**

## **Code**

```python
n = 3

with open("data.txt", "r") as f:

    for i in range(n):

        print(f.readline().strip())
```

---

# **Q20. Find most frequent word**

Very popular in coding rounds.

---

## **Code**

```python
freq = {}

with open("data.txt", "r") as f:

    words = f.read().split()

    for word in words:

        freq[word] = freq.get(word, 0) + 1

max_word = max(freq, key=freq.get)

print("Most frequent:", max_word)
```

---

# **Level 6️⃣ — Real Interview Scenario Problems**

Very important for strong preparation.

---

# **Q21. Replace word in file**

## **Code**

```pytho 
old = "Python"
new = "Java"

with open("data.txt", "r") as f:

    data = f.read()

data = data.replace(old, new)

with open("data.txt", "w") as f:

    f.write(data)
```

---

# **Q22. Encrypt file content (basic)**

## **Code**

```python
with open("data.txt", "r") as f:

    data = f.read()

encrypted = ""

for ch in data:

    encrypted += chr(ord(ch) + 1)

with open("data.txt", "w") as f:

    f.write(encrypted)
```
