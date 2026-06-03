Here are **Python Regex Interview Questions** arranged from **basic → advanced → coding**, exactly how they are asked in real interviews (especially for Python, Data Science, and Backend roles).

---

# 🐍 Python Regex Interview Questions

# 🟢 Basic Regex Interview Questions (Very Common)

These are asked in **almost every interview**.

---

## 1️⃣ What is Regex?

**Expected Answer:**

Regular Expression (Regex) is a sequence of characters used to define a **search pattern**.
It is mainly used for:

* Pattern matching
* Searching text
* Validating inputs
* Extracting data

In Python, Regex is implemented using the **`re` module**.

---

## 2️⃣ Which module is used for Regex in Python?

**Answer:**

```python
import re
```

Python uses the **`re` module** for working with regular expressions.

---

## 3️⃣ What is the difference between `match()` and `search()`?

**Very frequently asked**

| match()                               | search()               |
| ------------------------------------- | ---------------------- |
| Checks only at start                  | Checks entire string   |
| Returns match if pattern at beginning | Returns match anywhere |
| Faster                                | More flexible          |

Example:

```python
import re

text = "I love Python"

re.match("Python", text)   # None
re.search("Python", text)  # Match found
```

---

## 4️⃣ What does `findall()` do?

**Answer:**

`findall()` returns **all matches** of a pattern in a list.

Example:

```python
import re

text = "Price 100 200 300"

result = re.findall(r'\d+', text)

print(result)
```

Output:

```python
['100', '200', '300']
```

---

## 5️⃣ What is a raw string (`r''`) in Regex?

**Very common question**

**Answer:**

Raw string (`r''`) prevents Python from treating `\` as escape characters.

Example:

```python
r'\d+'   # correct
'\d+'    # may cause issues
```

Always use:

```python
r'\d+'
```

---

## 6️⃣ What are special characters in Regex?

Examples:

| Symbol | Meaning       |
| ------ | ------------- |
| `.`    | Any character |
| `^`    | Start         |
| `$`    | End           |
| `*`    | 0 or more     |
| `+`    | 1 or more     |
| `?`    | Optional      |

---

## 7️⃣ What is `\d` in Regex?

**Answer:**

`\d` matches **digits (0–9)**.

Example:

```python
re.findall(r'\d', "A1B2")
```

Output:

```python
['1', '2']
```

---

## 8️⃣ What is `\w` in Regex?

**Answer:**

`\w` matches:

* letters
* digits
* underscore

Equivalent to:

```python
[a-zA-Z0-9_]
```

---

## 9️⃣ What is the difference between `*` and `+`?

**Very important**

| `*`       | `+`       |
| --------- | --------- |
| 0 or more | 1 or more |

Example:

```python
a*   # "", a, aa, aaa
a+   # a, aa, aaa
```

---

## 🔵 Intermediate Regex Interview Questions

These are asked in **Python Developer and Data Science interviews**.

---

## 🔟 What is `re.sub()`?

Used to **replace matched text**.

Example:

```python
import re

text = "Python is good"

result = re.sub("good", "awesome", text)

print(result)
```

Output:

```python
Python is awesome
```

---

## 11️⃣ What is `re.split()`?

Splits string using pattern.

Example:

```python
re.split(r'[;,]', "a,b;c")
```

Output:

```python
['a', 'b', 'c']
```

---

## 12️⃣ What is grouping in Regex?

Grouping is done using parentheses `()`.

Example:

```python
import re

text = "12-05-2024"

match = re.search(r'(\d{2})-(\d{2})-(\d{4})', text)

print(match.group(1))
```

Output:

```python
12
```

---

## 13️⃣ What is the difference between `findall()` and `finditer()`?

| findall               | finditer              |
| --------------------- | --------------------- |
| Returns list          | Returns iterator      |
| Uses more memory      | Memory efficient      |
| Faster for small data | Better for large data |

---

## 14️⃣ What is greedy matching?

Greedy matching matches **maximum characters**.

Example:

```python
re.findall(r'<.*>', "<h1>Title</h1>")
```

Output:

```python
['<h1>Title</h1>']
```

---

## 15️⃣ What is non-greedy matching?

Uses `?` to match **minimum characters**.

Example:

```python
re.findall(r'<.*?>', "<h1>Title</h1>")
```

Output:

```python
['<h1>', '</h1>']
```

---

## 🟣 Advanced Regex Interview Questions

These appear in **experienced-level interviews**.

---

## 16️⃣ What are lookaheads in Regex?

Lookahead checks pattern **without consuming characters**.

Positive Lookahead:

```python
(?=...)
```

Example:

```python
re.findall(r'\d+(?=kg)', "10kg 20kg 30m")
```

Output:

```python
['10', '20']
```

---

## 17️⃣ What are lookbehinds?

Positive Lookbehind:

```python
(?<=...)
```

Example:

```python
re.findall(r'(?<=\$)\d+', "$100 $200")
```

Output:

```python
['100', '200']
```

---

## 18️⃣ What are Regex flags?

Common flags:

| Flag   | Meaning             |
| ------ | ------------------- |
| `re.I` | Ignore case         |
| `re.M` | Multi-line          |
| `re.S` | Dot matches newline |

Example:

```python
re.search("python", "PYTHON", re.I)
```

---

## 19️⃣ What is `^` and `$` in Regex?

| Symbol | Meaning         |
| ------ | --------------- |
| `^`    | Start of string |
| `$`    | End of string   |

Example:

```python
r'^hello'
r'world$'
```

---

## 20️⃣ What is character set `[]`?

Used to match **specific characters**.

Example:

```python
re.findall(r'[abc]', "apple")
```

Output:

```python
['a', 'p']
```

---

# 🔴 Coding-Based Regex Interview Questions

These are **very important**.

---

# 21️⃣ Validate Email Address

```python
import re

email = "test@gmail.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid")
```

---

# 22️⃣ Validate Phone Number

10-digit number:

```python
pattern = r'^\d{10}$'
```

---

# 23️⃣ Extract Numbers from String

```python
import re

text = "Order 123 costs 456"

numbers = re.findall(r'\d+', text)

print(numbers)
```

Output:

```python
['123', '456']
```

---

# 24️⃣ Remove Special Characters

```python
text = "Hello@#World123"

clean = re.sub(r'[^a-zA-Z0-9]', '', text)

print(clean)
```

Output:

```python
HelloWorld123
```

---

# 25️⃣ Count Number of Words

```python
text = "Python is very powerful"

words = re.findall(r'\w+', text)

print(len(words))
```

---

# 26️⃣ Extract Dates

```python
text = "Today is 12-05-2024"

dates = re.findall(r'\d{2}-\d{2}-\d{4}', text)
```

---

# 27️⃣ Extract URLs

```python
pattern = r'https?://\S+'
```

---

# 28️⃣ Validate Password

Minimum:

* 8 characters
* 1 uppercase
* 1 lowercase
* 1 digit

```python
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
```

---

# 🟡 Tricky Interview Questions

These test deeper understanding.

---

## 29️⃣ What is difference between `.` and `\.`?

| Pattern | Meaning       |
| ------- | ------------- |
| `.`     | Any character |
| `\.`    | Literal dot   |

---

## 30️⃣ Why use raw strings in regex?

To avoid escape sequence conflicts.

Example:

```python
r'\n'   # literal
'\n'    # newline
```

---

## 31️⃣ How to match whitespace?

```python
\s
```

---

## 32️⃣ How to match non-digit?

```python
\D
```

---

## 33️⃣ How to match start and end of string?

```python
^pattern$
```

---

# 🟠 Real Interview Practice Questions

Practice these — very realistic.

---

## Q34 — Extract all hashtags

Input:

```python
"I love #python and #datascience"
```

Expected:

```python
['#python', '#datascience']
```

---

## Q35 — Extract all words starting with capital letter

Input:

```python
"Roshan lives in Bangalore"
```

---

## Q36 — Extract email domains

Example:

```python
test@gmail.com → gmail.com
```

---

## Q37 — Replace multiple spaces with single space

---

## Q38 — Extract floating numbers

Example:

```python
"Price: 12.5 45.67"
```

---

## Q39 — Extract only alphabets

---

## Q40 — Validate Indian phone number

Example:

```python
+91-9876543210
```

---

# 🧠 Most Important Regex Questions to Prepare

If you're preparing for interviews, **focus strongly on these**:

⭐ match vs search
⭐ findall vs finditer
⭐ raw strings
⭐ greedy vs non-greedy
⭐ groups
⭐ email validation
⭐ phone validation
⭐ password validation
⭐ extracting numbers
⭐ regex flags

---

# If You're Preparing for Interviews Seriously

I recommend next:

✅ **50 Regex Coding Practice Problems**
✅ **Regex MCQs**
✅ **Regex Cheat Sheet (1-page)**
✅ **Real Company Interview Questions**

Just say:

**"Give me regex coding problems"**
