 Here is the **previous explanation of `map()` converted fully into clean Markdown (.md) format** so you can save it directly as a `.md` file.

````markdown
# map() Function in Python — How It Works (with Examples)

The **map()** function is used to **apply a function to every item of an iterable** (like a list, tuple, etc.).

---

# Syntax

```python
map(function, iterable)
````

* **function** → The function to apply to each element
* **iterable** → The data (list, tuple, etc.)
* **Returns** → A **map object** (convert to list if needed)

---

# Basic Example 1: Convert Strings to Integers

```python
numbers = ["1", "2", "3", "4"]

result = map(int, numbers)

print(list(result))
```

## Output

```python
[1, 2, 3, 4]
```

## How It Works Internally

```
int("1") → 1
int("2") → 2
int("3") → 3
int("4") → 4
```

So:

```python
map(int, ["1","2","3","4"])
```

becomes:

```python
[1,2,3,4]
```

(after converting to list)

---

# Example 2: Square Numbers Using a Function

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))
```

## Output

```python
[1, 4, 9, 16]
```

## What Happens

```
square(1) → 1
square(2) → 4
square(3) → 9
square(4) → 16
```

---

# Example 3: Using lambda (Most Common)

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

## Output

```python
[2, 4, 6, 8]
```

Here:

```
lambda x: x * 2
```

means:

```
Multiply each number by 2
```

---

# Example 4: Multiple Iterables

`map()` can take **multiple lists**.

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)

print(list(result))
```

## Output

```python
[5, 7, 9]
```

## What Happens

```
1 + 4 → 5
2 + 5 → 7
3 + 6 → 9
```

---

# Very Important Example (Your Case)

```python
requests = list(map(int, input().split()))
```

## Suppose Input Is

```
2 2 5
```

### Step-by-step:

```
input() → "2 2 5"

.split() → ["2","2","5"]

map(int, ["2","2","5"])
        ↓
        2 2 5

list(...) → [2,2,5]
```

Final:

```python
requests = [2, 2, 5]
```

---

# Difference Between map() and Loop

## Using Loop

```python
numbers = ["1", "2", "3"]

result = []

for n in numbers:
    result.append(int(n))

print(result)
```

## Using map() (Shorter)

```python
numbers = ["1", "2", "3"]

result = list(map(int, numbers))

print(result)
```

Same output:

```python
[1, 2, 3]
```

---

# Key Points to Remember ⭐

* `map()` applies a function to **every element**
* Returns a **map object**
* Use `list()` to see results
* Faster and shorter than loops
* Often used with:

  * `int`
  * `float`
  * `lambda`
  * `input().split()`

---

# Memory Trick 🧠

Think:

```
map() = Apply function to ALL items
```

Example:

```python
map(int, ["1","2","3"])
```

Means:

```
Apply int() to every element
```

```

If you're building **Python notes or interview prep Markdown**, I can also create similar `.md` files for:

- `filter()`  
- `reduce()`  
- `lambda`  
- `zip()`  
- `enumerate()`  

These five together are **very important for interviews and coding tests**.
```
