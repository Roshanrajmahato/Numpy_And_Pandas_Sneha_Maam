Great 👍 — here is a **complete Markdown file** covering the next important Python functions:
`filter()`, `reduce()`, `lambda`, `zip()`, and `enumerate()` — all in **one single Markdown file** you can save as:

`python_important_functions.md`

````markdown
# Important Python Functions for Coding & Interviews

This document covers:

- lambda
- map()
- filter()
- reduce()
- zip()
- enumerate()

These functions are widely used in **coding interviews**, **data processing**, and **Python problem solving**.

---

# 1. lambda Function

A **lambda function** is a small anonymous function (a function without a name).

## Syntax

```python
lambda arguments: expression
````

## Example 1: Simple Lambda

```python
square = lambda x: x * x

print(square(5))
```

### Output

```python
25
```

Equivalent Normal Function:

```python
def square(x):
    return x * x
```

---

## Example 2: Lambda with Multiple Arguments

```python
add = lambda a, b: a + b

print(add(3, 4))
```

### Output

```python
7
```

---

# 2. map() Function

The **map()** function applies a function to every item in an iterable.

## Syntax

```python
map(function, iterable)
```

Returns a **map object** (convert using list()).

---

## Example 1: Convert Strings to Integers

```python
numbers = ["1", "2", "3"]

result = list(map(int, numbers))

print(result)
```

### Output

```python
[1, 2, 3]
```

---

## Example 2: Multiply Numbers Using Lambda

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

### Output

```python
[2, 4, 6, 8]
```

---

## Very Important Input Example

```python
numbers = list(map(int, input().split()))
```

### Input

```
2 4 6
```

### Output

```python
[2, 4, 6]
```

---

# 3. filter() Function

The **filter()** function selects elements that satisfy a condition.

## Syntax

```python
filter(function, iterable)
```

---

## Example 1: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

### Output

```python
[2, 4, 6]
```

---

## Example 2: Filter Odd Numbers

```python
numbers = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)
```

### Output

```python
[1, 3, 5]
```

---

# 4. reduce() Function

The **reduce()** function applies a function cumulatively to elements.

It is available in:

```python
from functools import reduce
```

---

## Syntax

```python
reduce(function, iterable)
```

---

## Example 1: Find Sum of List

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

### Output

```python
10
```

---

## How reduce() Works

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

Final result = **10**

---

## Example 2: Find Product of List

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x * y, numbers)

print(result)
```

### Output

```python
24
```

---

# 5. zip() Function

The **zip()** function combines multiple iterables element-wise.

## Syntax

```python
zip(iterable1, iterable2, ...)
```

---

## Example 1: Combine Two Lists

```python
names = ["A", "B", "C"]
marks = [90, 80, 70]

result = list(zip(names, marks))

print(result)
```

### Output

```python
[('A', 90), ('B', 80), ('C', 70)]
```

---

## Example 2: Loop Using zip()

```python
names = ["A", "B", "C"]
marks = [90, 80, 70]

for name, mark in zip(names, marks):
    print(name, mark)
```

### Output

```python
A 90
B 80
C 70
```

---

# 6. enumerate() Function

The **enumerate()** function adds an index to elements.

## Syntax

```python
enumerate(iterable, start=0)
```

---

## Example 1: Basic enumerate()

```python
names = ["A", "B", "C"]

result = list(enumerate(names))

print(result)
```

### Output

```python
[(0, 'A'), (1, 'B'), (2, 'C')]
```

---

## Example 2: enumerate() with Start Index

```python
names = ["A", "B", "C"]

result = list(enumerate(names, start=1))

print(result)
```

### Output

```python
[(1, 'A'), (2, 'B'), (3, 'C')]
```

---

## Example 3: Loop with enumerate()

```python
names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)
```

### Output

```python
0 A
1 B
2 C
```

---

# Quick Summary Table

| Function    | Purpose                            | Example Use                 |
| ----------- | ---------------------------------- | --------------------------- |
| lambda      | Create small anonymous functions   | `lambda x: x*x`             |
| map()       | Apply function to all elements     | Convert strings to integers |
| filter()    | Select elements based on condition | Filter even numbers         |
| reduce()    | Combine elements into one result   | Find sum or product         |
| zip()       | Combine multiple lists             | Pair names and marks        |
| enumerate() | Add index to elements              | Loop with index             |

---

# Most Important Interview Patterns 🚀

```python
# map input
numbers = list(map(int, input().split()))

# filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# sum using reduce
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)

# zip lists
pairs = list(zip(list1, list2))

# enumerate loop
for i, val in enumerate(numbers):
    print(i, val)
```

---

# Memory Tricks 🧠

* **lambda** → small function
* **map()** → modify all items
* **filter()** → select some items
* **reduce()** → combine items
* **zip()** → join lists
* **enumerate()** → add index

```
