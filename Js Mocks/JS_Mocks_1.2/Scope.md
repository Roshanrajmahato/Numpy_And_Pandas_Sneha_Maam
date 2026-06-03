
# 🎯 Interview Short Answer

> Scope in JavaScript defines the accessibility of variables. JavaScript has global scope, function scope, and block scope. Variables declared with `var` are function-scoped, while `let` and `const` are block-scoped.

# **4️⃣ What are JavaScript Scopes? (Detailed Explanation)**

---

# 🧠 What is Scope?

👉 **Scope determines where a variable is accessible in your code.**

In simple words:

> Scope = Visibility of a variable

---

# 📌 JavaScript Has 3 Main Types of Scope:

1️⃣ Global Scope
2️⃣ Function Scope
3️⃣ Block Scope

---

# 🔹 1️⃣ Global Scope

A variable declared outside any function or block.

```js
let name = "Roshan";

function greet() {
  console.log(name);
}

greet(); // Roshan
```

### ✅ Accessible everywhere in the file.

---

### ⚠ Problem with Global Variables

```js
let count = 0;

function increment() {
  count++;
}
```

Too many global variables can:

* Cause conflicts
* Increase bugs
* Pollute memory

---

# 🔹 2️⃣ Function Scope

Variables declared inside a function are accessible only inside that function.

```js
function test() {
  let x = 10;
  console.log(x);
}

test();      // 10
console.log(x); // ❌ Error
```

---

### ⚠ Important

`var` is function-scoped.

```js
function demo() {
  if (true) {
    var y = 20;
  }
  console.log(y); // ✅ 20
}
```

Because `var` ignores block scope.

---

# 🔹 3️⃣ Block Scope (ES6 Feature)

Variables declared using `let` or `const` inside `{}`.

```js
if (true) {
  let a = 5;
}
console.log(a); // ❌ Error
```

Works in:

* if blocks
* for loops
* while loops
* any `{}` block

---

# 🧠 Example – For Loop Scope

```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
console.log(i); // ❌ Error
```

But:

```js
for (var i = 0; i < 3; i++) {
  console.log(i);
}
console.log(i); // ✅ 3
```

---

# 🔥 Scope Chain (Advanced Concept)

When JS looks for a variable:

1️⃣ It checks current scope
2️⃣ Then parent scope
3️⃣ Then global scope

Example:

```js
let globalVar = "Global";

function outer() {
  let outerVar = "Outer";

  function inner() {
    console.log(globalVar);
    console.log(outerVar);
  }

  inner();
}

outer();
```

This is called **Lexical Scope**.

---

# 🧠 Visual Understanding

```
Global Scope
   ↓
Function Scope
   ↓
Block Scope
```

Child scope can access parent variables.
Parent scope cannot access child variables.

---
