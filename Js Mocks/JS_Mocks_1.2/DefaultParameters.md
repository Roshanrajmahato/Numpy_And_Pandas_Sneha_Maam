
# 💡 Interview One-Line Answer

> Default parameters allow function parameters to have predefined values when no argument or `undefined` is passed.

# ✅ 20. What are Default Parameters in JavaScript?

---

## 🔹 Definition

**Default parameters** allow you to assign a default value to a function parameter if no value (or `undefined`) is passed.

This feature was introduced in **ES6 (ECMAScript 2015)**.

---

# 🔥 Why We Need Default Parameters?

Before ES6, we had to manually check:

```javascript
function greet(name) {
  name = name || "Guest";
  console.log("Hello " + name);
}
```

Problem:

* Not clean
* Can cause bugs (if name = "" or 0)

---

# ✅ With Default Parameters (Modern Way)

```javascript
function greet(name = "Guest") {
  console.log("Hello " + name);
}

greet();        // Hello Guest
greet("Roshan"); // Hello Roshan
```

If no value is passed → default is used.

---

# 🔥 Important Behavior

Default value is used only when:

* Argument is `undefined`
* OR no argument is passed

Example:

```javascript
function test(a = 10) {
  console.log(a);
}

test();          // 10
test(undefined); // 10
test(null);      // null (default NOT used)
```

⚠ `null` does NOT trigger default value.

---

# 🔥 Multiple Default Parameters

```javascript
function calculate(a = 0, b = 0) {
  return a + b;
}

console.log(calculate());      // 0
console.log(calculate(5));     // 5
console.log(calculate(5, 10)); // 15
```

---

# 🔥 Default Parameter Using Another Parameter

```javascript
function greet(name, message = "Hello " + name) {
  console.log(message);
}

greet("Roshan"); 
// Hello Roshan
```

Default parameters can use previous parameters.

---

# 🔥 Default Parameter with Function

```javascript
function getValue() {
  return 100;
}

function test(a = getValue()) {
  console.log(a);
}

test(); // 100
```

Default value can be:

* Expression
* Function call
* Calculation

---

# 🔥 Real Project Example

In your API backend:

```javascript
function createUser(name, role = "user") {
  console.log(name, role);
}
```

If role not provided → automatically "user".

---

# 🔥 Interview Comparison (Before vs After ES6)

| Before ES6   | ES6              |
| ------------ | ---------------- |
| Manual check | Built-in support |
| More code    | Cleaner code     |
| Error-prone  | Safe             |

---
