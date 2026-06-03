
# 💡 Interview One-Line Answer

> A function declaration is fully hoisted and can be called before definition, while a function expression is assigned to a variable and cannot be used before it is defined.

# ✅ 16. Difference Between Function Declaration and Function Expression

---

# 🔹 1️⃣ Function Declaration

## 🔹 Definition

A **function declaration** defines a named function using the `function` keyword.

### Example:

```javascript
function greet() {
  console.log("Hello");
}
```

---

## 🔥 Key Feature: Hoisting

Function declarations are **fully hoisted**.

That means you can call them **before** they are defined.

### Example:

```javascript
greet(); // ✅ Works

function greet() {
  console.log("Hello");
}
```

✔ No error
✔ JavaScript moves the function to the top during compilation

---

# 🔹 2️⃣ Function Expression

## 🔹 Definition

A **function expression** is when a function is assigned to a variable.

### Example:

```javascript
const greet = function() {
  console.log("Hello");
};
```

---

## 🔥 Hoisting Behavior

Function expressions are **NOT fully hoisted**.

Only the variable is hoisted — not the function body.

### Example:

```javascript
greet(); // ❌ Error

const greet = function() {
  console.log("Hello");
};
```

Why error?

Because:

* `greet` is hoisted
* But it is in **Temporal Dead Zone (TDZ)** (since it's `const`)
* Function is not initialized yet

---

# 🔥 If Using `var`

```javascript
greet(); // ❌ TypeError

var greet = function() {
  console.log("Hello");
};
```

Why TypeError?

Because:

* `var greet` is hoisted and initialized as `undefined`
* JS tries to call `undefined()` → Error

---

# 🔥 Named vs Anonymous

Function declaration:

```javascript
function greet() {}
```

Must have a name.

Function expression:

```javascript
const greet = function() {};
```

Can be anonymous or named:

```javascript
const greet = function sayHello() {};
```

---

# 🔥 Arrow Function (Also a Function Expression)

```javascript
const greet = () => {
  console.log("Hello");
};
```

Arrow functions are always expressions.

---

# 🔥 Interview Comparison Table

| Feature                    | Function Declaration | Function Expression |
| -------------------------- | -------------------- | ------------------- |
| Hoisted                    | ✅ Yes (fully)        | ❌ No                |
| Can call before definition | ✅ Yes                | ❌ No                |
| Must have name             | ✅ Yes                | ❌ Not required      |
| Stored in variable         | ❌ No                 | ✅ Yes               |
| Common in                  | Traditional JS       | Modern JS / React   |

---

# 🔥 Real Project Usage

### Use Function Declaration:

* Utility functions
* Global helper functions

### Use Function Expression:

* Callback functions
* React components
* Event handlers
* When passing as argument

Example:

```javascript
button.addEventListener("click", function() {
  console.log("Clicked");
});
```

---
