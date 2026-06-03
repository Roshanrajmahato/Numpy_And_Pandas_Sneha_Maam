# 💡 Interview One-Line Answer

> The rest operator (`...`) collects multiple arguments into a single array and is mainly used in function parameters and destructuring.

# ✅ 21. What is the Rest Operator (`...args`)?

--- 

## 🔹 Definition

The **rest operator (`...`)** allows a function to accept **any number of arguments** and store them in an array.

It is mainly used in:

* Function parameters
* Destructuring

---

# 🔥 1️⃣ Rest Operator in Functions

### Without Rest Operator ❌

```javascript
function sum(a, b, c) {
  return a + b + c;
}

sum(1, 2, 3); // 6
```

Problem:

* Only accepts 3 parameters
* Cannot handle unlimited arguments

---

### With Rest Operator ✅

```javascript
function sum(...numbers) {
  console.log(numbers);
}
```

If you call:

```javascript
sum(1, 2, 3, 4, 5);
```

Output:

```javascript
[1, 2, 3, 4, 5]
```

✔ All arguments collected into an array

---

## 🔥 Real Example (Sum All Numbers)

```javascript
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(10, 20, 30)); // 60
console.log(sum(1, 2, 3, 4, 5)); // 15
```

Works with unlimited values.

---

# 🔥 Important Rule

The rest parameter must be:

* The **last parameter** in function

❌ Wrong:

```javascript
function test(...nums, a) {}
```

✅ Correct:

```javascript
function test(a, ...nums) {}
```

---

# 🔥 2️⃣ Rest Operator in Destructuring

## Array Example

```javascript
const arr = [1, 2, 3, 4, 5];

const [first, ...rest] = arr;

console.log(first); // 1
console.log(rest);  // [2, 3, 4, 5]
```

---

## Object Example

```javascript
const user = {
  name: "Roshan",
  age: 22,
  city: "Delhi"
};

const { name, ...details } = user;

console.log(name);    // Roshan
console.log(details); // { age: 22, city: "Delhi" }
```

---

# 🔥 Rest vs Spread (Very Important Interview Question)

They look same (`...`) but work differently.

| Feature  | Rest Operator           | Spread Operator           |
| -------- | ----------------------- | ------------------------- |
| Purpose  | Collect values          | Expand values             |
| Used in  | Function parameters     | Arrays, Objects           |
| Converts | Many values → One array | Array → Individual values |

---

## Spread Example (for comparison)

```javascript
const arr = [1, 2, 3];

console.log(...arr); 
// 1 2 3
```

Here it spreads array elements.

---

# 🔥 Real Project Example

In your backend API:

```javascript
function createUser(name, email, ...otherDetails) {
  console.log(otherDetails);
}
```

You can accept flexible user data without breaking function.

---

