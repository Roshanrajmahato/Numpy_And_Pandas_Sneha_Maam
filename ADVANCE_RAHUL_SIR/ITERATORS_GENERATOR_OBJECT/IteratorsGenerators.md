# 🎯 ITERATORS — Interview Explanation

## ⭐ Q1: What is an Iterator in Python?

**Interview Answer (Best Way to Say):**

An **iterator** in Python is an object that allows us to **traverse elements one at a time** from a collection like a list, tuple, or string.
It follows the **iterator protocol**, which means it must implement two methods:

* `__iter__()` — returns the iterator object
* `__next__()` — returns the next element

When no elements are left, it raises **StopIteration**.

---

## ⭐ Example You Can Explain

```python
l1 = [10, 20, 30]

it = iter(l1)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
```

**What to Say in Interview:**

Here, `iter()` converts the list into an iterator, and `next()` retrieves elements one by one until the list ends.

---

# ⭐ Q2: What is Iterable?

**Interview Answer:**

An **iterable** is any object that can be converted into an iterator.

Examples:

* List
* Tuple
* String
* Dictionary
* Set

Example:

```python
l = [1,2,3]

it = iter(l)   # iterable → iterator
```

---

# ⭐ Q3: How Does a `for` Loop Work Internally?

🔥 **Very Important Interview Question**

**Interview Answer:**

Internally, the `for` loop:

1. Converts iterable into iterator using `iter()`
2. Calls `next()` repeatedly
3. Stops when **StopIteration** occurs

Example:

```python
for i in [1,2,3]:
    print(i)
```

Internally:

```python
it = iter([1,2,3])

while True:
    try:
        print(next(it))
    except StopIteration:
        break
```

---

# ⭐ Q4: Create Custom Iterator Class

🔥 Frequently Asked Coding Question

```python
class Numbers:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 5:
            result = self.num
            self.num += 1
            return result
        else:
            raise StopIteration


n = Numbers()

for i in n:
    print(i)
```

---

## What to Say:

This class implements both `__iter__()` and `__next__()` methods, making it an iterator.
It returns numbers from **1 to 5** and stops using **StopIteration**.

---

# 🎯 GENERATORS — Interview Explanation

---

# ⭐ Q5: What is Generator in Python?

**Interview Answer (Best Way):**

A **generator** is a special type of function that uses the **yield** keyword to return values **one at a time**, instead of returning all values at once.

Generators automatically behave like iterators.

---

# ⭐ Q6: What is `yield`?

**Interview Answer:**

`yield` works like `return`, but instead of ending the function, it **pauses the function** and remembers its state.
When called again, it continues from where it stopped.

---

# ⭐ Generator Example

```python
def mygen():

    yield 10
    yield 20
    yield 30

g = mygen()

print(next(g))
print(next(g))
print(next(g))
```

---

## What to Say:

Each time `next()` is called, the function resumes from the previous `yield`.

---

# ⭐ Q7: Generator Using Loop

Very common question.

```python
def numbers():

    for i in range(1,6):
        yield i

g = numbers()

for i in g:
    print(i)
```

---

# ⭐ Q8: Generator vs Normal Function

**Interview Answer:**

Normal function uses `return` and finishes execution.
Generator uses `yield` and pauses execution, allowing multiple values to be produced.

---

# ⭐ Table Explanation

| Feature   | Normal Function | Generator  |
| --------- | --------------- | ---------- |
| Keyword   | return          | yield      |
| Execution | Ends            | Pauses     |
| Memory    | High            | Low        |
| Use       | Small data      | Large data |

---

# ⭐ Q9: Iterator vs Generator

🔥 Very common interview question

**Interview Answer:**

Iterator is created using a **class** and requires `__iter__()` and `__next__()` methods.
Generator is created using a **function** and uses `yield`.

Generators are easier to write and more memory efficient than iterators.

---

# ⭐ Q10: Why Generators Are Memory Efficient?

**Interview Answer:**

Generators generate values **only when required**, instead of storing all values in memory.
This concept is called **Lazy Evaluation**.

---

# ⭐ Example to Explain Memory Difference

List:

```python
nums = [i for i in range(1000000)]
```

Generator:

```python
nums = (i for i in range(1000000))
```

Generator uses **less memory**.

---

# ⭐ Q11: Infinite Generator Example

```python
def infinite():

    num = 1

    while True:
        yield num
        num += 1
```

---

## What to Say:

This generator produces numbers infinitely but only when requested.

---

# ⭐ Q12: Real-Life Example (Very Good for Interviews)

USN Generator (from your notes)

```python
def usn_generator(college, year, stream):

    num = 1

    while True:

        yield (
            str(1)
            + college
            + str(year)
            + stream
            + str(num)
        )

        num += 1


usn = usn_generator("BMS", 2026, "ME")

print(next(usn))
print(next(usn))
```

---

## What to Say:

This generator creates student USN numbers dynamically and generates them only when needed.

---

# 🎯 Most Important Interview Questions (Must Prepare)

These are commonly asked.

---

# ⭐ Q13: What is StopIteration?

**Interview Answer:**

StopIteration is an exception raised when no more elements are available in an iterator.

---

# ⭐ Q14: What is Lazy Evaluation?

**Interview Answer:**

Lazy evaluation means generating values **only when needed**, instead of storing all values beforehand.

Generators use lazy evaluation.

---

# ⭐ Q15: Can Generator Be Used Only Once?

**Interview Answer:**

Yes.
Once all values are consumed, the generator becomes empty and cannot be reused.

---

# ⭐ Q16: What is Generator Expression?

**Interview Answer:**

Generator expression is similar to list comprehension but uses **parentheses instead of brackets**.

Example:

```python
nums = (i for i in range(5))
```

---

# ⭐ Q17: When Should We Use Generators?

**Interview Answer:**

Generators should be used:

* When handling large datasets
* When memory efficiency is required
* When processing streaming data
* When generating infinite sequences

---

# ⭐ Q18: Real-Time Use Cases

Very strong interview point 💡

You can say:

Generators are used in:

* Reading large files
* Data pipelines
* Machine learning preprocessing
* Log processing
* API streaming

This is especially useful in **data science workflows**, which matches your project background.

---

# 🎯 Coding Questions Often Asked

Practice these:

1. Fibonacci Generator
2. Even Number Generator
3. Custom Iterator Class
4. Reverse Iterator
5. Infinite Counter Generator

---

# ⭐ If Interviewer Asks:

**"Explain Iterator and Generator in simple terms"**

You can say:

**Perfect Short Answer:**

Iterator allows us to traverse elements one by one using `next()`.
Generator is a simpler way to create iterators using `yield`, and it is memory efficient because it generates values only when needed.

---

# 🎯 Final Advice for You (Important)

Since you're preparing for **Python/Data Science interviews**, focus strongly on:

✔ Iterator vs Generator
✔ yield vs return
✔ Lazy evaluation
✔ Memory optimization
✔ Real-life examples

These are **frequently asked** in interviews.
