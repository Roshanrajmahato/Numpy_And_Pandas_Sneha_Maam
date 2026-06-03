# 💡 Interview One-Line Answer

> A pure function always returns the same output for the same input and does not cause any side effects.

# ✅ 23. What is a Pure Function?

## 🔹 Definition

A **pure function** is a function that:

1. ✅ Always returns the same output for the same input
2. ✅ Has **no side effects**

---

# 🔥 Condition 1: Same Input → Same Output

Example:

```javascript
function add(a, b) {
  return a + b;
}

add(2, 3); // 5
add(2, 3); // 5
```

No matter how many times you call it with `2,3`, the result is always `5`.

✔ This is pure.

---

# 🔥 Condition 2: No Side Effects

Side effects mean:

* Modifying global variables
* Changing DOM
* Making API calls
* Logging to console
* Changing input data

---

## ❌ Not a Pure Function (Has Side Effect)

```javascript
let total = 0;

function addToTotal(num) {
  total += num;
}
```

Why not pure?

* It modifies external variable `total`
* Output depends on previous state

---

## ❌ Not Pure (Uses Random)

```javascript
function getRandom() {
  return Math.random();
}
```

Same input → different output
Not predictable → Not pure

---

# ✅ Pure Function Example

```javascript
function multiply(a, b) {
  return a * b;
}
```

✔ No external dependency
✔ No side effects
✔ Same input → same output

---

# 🔥 Tricky Example (Important for Interview)

```javascript
function updateArray(arr) {
  arr.push(5);
  return arr;
}
```

❌ Not pure
Because it modifies original array.

---

## ✔ Pure Version

```javascript
function updateArray(arr) {
  return [...arr, 5];
}
```

Now:

* Original array unchanged
* Returns new array
* No mutation

✔ Pure

---

# 🔥 Why Pure Functions Are Important?

They:

* Are easier to test
* Are predictable
* Avoid bugs
* Work well in React
* Improve maintainability

---

# 🔥 Real Project Example

In React:

Bad ❌

```javascript
state.count++;
```

Good ✅

```javascript
setState(prev => ({ count: prev.count + 1 }));
```

Because React prefers immutability (pure logic).

---

# 🔥 Pure vs Impure Comparison

| Feature                  | Pure Function | Impure Function |
| ------------------------ | ------------- | --------------- |
| Same input → same output | ✅             | ❌               |
| Modifies global variable | ❌             | ✅               |
| Changes input data       | ❌             | ✅               |
| Predictable              | ✅             | ❌               |

---

