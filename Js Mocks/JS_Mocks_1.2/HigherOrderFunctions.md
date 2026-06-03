
# 💡 Interview One-Line Answer

> A higher-order function is a function that takes another function as an argument or returns a function as a result.

# ✅ 17. What are Higher-Order Functions in JavaScript?

---

## 🔹 Definition

A **Higher-Order Function (HOF)** is a function that:

1. ✅ Takes another function as an argument
   OR
2. ✅ Returns another function

If a function does either of these → it is a Higher-Order Function.

---

# 🔥 Why This Is Possible?

Because in JavaScript:

👉 **Functions are first-class citizens**

That means:

* Functions can be stored in variables
* Passed as arguments
* Returned from other functions

---

# 🔥 1️⃣ Function Taking Another Function (Most Common)

### Example:

```javascript
function greet(name) {
  return "Hello " + name;
}

function processUser(callback) {
  const name = "Roshan";
  return callback(name);
}

console.log(processUser(greet));
```

Output:

```
Hello Roshan
```

Here:

* `processUser` takes `greet` as argument
* So `processUser` is a Higher-Order Function

---

# 🔥 2️⃣ Function Returning Another Function

### Example:

```javascript
function multiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = multiplier(2);
console.log(double(5)); // 10
```

Here:

* `multiplier` returns a function
* So it is a Higher-Order Function

---

# 🔥 Real Built-in Higher-Order Functions (VERY IMPORTANT)

JavaScript provides many built-in HOFs:

* `map()`
* `filter()`
* `reduce()`
* `forEach()`
* `setTimeout()`

---

## 🔹 Example with `map()`

```javascript
const numbers = [1, 2, 3, 4];

const doubled = numbers.map(function(num) {
  return num * 2;
});

console.log(doubled); // [2, 4, 6, 8]
```

Here:

* `map()` takes a function as argument
* So `map()` is a Higher-Order Function

---

## 🔹 Example with `filter()`

```javascript
const numbers = [10, 20, 30, 40];

const result = numbers.filter(num => num > 20);

console.log(result); // [30, 40]
```

---

# 🔥 Real Project Example

In your frontend:

```javascript
const users = [
  { name: "Roshan", role: "Admin" },
  { name: "Aman", role: "User" }
];

const admins = users.filter(user => user.role === "Admin");
```

`filter()` is a higher-order function.

---

# 🔥 Why Higher-Order Functions Are Important?

They:

* Make code reusable
* Improve readability
* Support functional programming
* Reduce repetition
* Used heavily in React

---

# 🔥 Interview Comparison

| Normal Function    | Higher-Order Function        |
| ------------------ | ---------------------------- |
| Does task directly | Works with other functions   |
| Less flexible      | More reusable                |
| Basic logic        | Functional programming style |

---
