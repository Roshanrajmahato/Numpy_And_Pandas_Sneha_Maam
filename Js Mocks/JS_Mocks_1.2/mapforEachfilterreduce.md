
# 💡 Interview One-Line Answer

> `forEach()` loops without returning anything, `map()` transforms elements into a new array, `filter()` selects elements based on a condition, and `reduce()` combines array elements into a single value.

# ✅ 15. Difference Between `map()`, `forEach()`, `filter()`, and `reduce()`

All four are **Higher-Order Array Methods**.

They:

* Work on arrays
* Take a callback function
* Do not modify original array (except `forEach` if you manually change it)

---

# 🔹 1️⃣ `forEach()`

## 🔹 Purpose:

Used to **loop through an array**

It does NOT return a new array.

---

### Example:

```javascript
const numbers = [1, 2, 3];

numbers.forEach(num => {
  console.log(num * 2);
});
```

Output:

```
2
4
6
```

---

### ❌ Important:

```javascript
const result = numbers.forEach(num => num * 2);
console.log(result); // undefined
```

`forEach()` always returns `undefined`.

---

# 🔹 2️⃣ `map()`

## 🔹 Purpose:

Used to **transform** each element
Returns a **new array**

---

### Example:

```javascript
const numbers = [1, 2, 3];

const doubled = numbers.map(num => num * 2);

console.log(doubled); 
// [2, 4, 6]
```

✔ Returns new array
✔ Same length as original

---

# 🔹 3️⃣ `filter()`

## 🔹 Purpose:

Used to **filter elements based on condition**
Returns a new array

---

### Example:

```javascript
const numbers = [10, 20, 30, 40];

const result = numbers.filter(num => num > 20);

console.log(result);
// [30, 40]
```

✔ Returns only matching elements
✔ May return smaller array

---

# 🔹 4️⃣ `reduce()`

## 🔹 Purpose:

Used to **reduce array to a single value**

Can be:

* Sum
* Product
* Object
* Grouping
* Any complex logic

---

### Example (Sum)

```javascript
const numbers = [1, 2, 3, 4];

const total = numbers.reduce((acc, curr) => {
  return acc + curr;
}, 0);

console.log(total);
// 10
```

Where:

* `acc` = accumulator
* `curr` = current value
* `0` = initial value

---

# 🔥 Real Project Example

Suppose you have users:

```javascript
const users = [
  { name: "Roshan", role: "Admin" },
  { name: "Aman", role: "User" }
];
```

### Extract Names (map)

```javascript
const names = users.map(user => user.name);
```

---

### Get Only Admins (filter)

```javascript
const admins = users.filter(user => user.role === "Admin");
```

---

### Count Users (reduce)

```javascript
const count = users.reduce((acc) => acc + 1, 0);
```

---

# 🔥 Comparison Table (Very Important 🔥)

| Method  | Returns      | Use Case       | Length          |
| ------- | ------------ | -------------- | --------------- |
| forEach | undefined    | Just looping   | Same            |
| map     | New array    | Transform data | Same            |
| filter  | New array    | Filter data    | Smaller or same |
| reduce  | Single value | Aggregate data | Single value    |

---

# 🔥 When to Use What?

Use:

* `forEach()` → when you just want to loop
* `map()` → when transforming data
* `filter()` → when selecting data
* `reduce()` → when combining data into one result

---
