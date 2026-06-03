
# 🎯 Interview Short Answer

> Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their scope before execution. Variables declared with `var` are hoisted and initialized with undefined, while `let` and `const` are hoisted but remain in the Temporal Dead Zone until initialized.

# **5️⃣ What is Hoisting in JavaScript? (Detailed Explanation)**

---

# 🧠 What is Hoisting?

> Hoisting is JavaScript's default behavior of moving declarations to the top of their scope before code execution.

⚠ Important:

* Only **declarations** are hoisted
* Not initializations

---

# 🔹 Example with `var`

```js
console.log(a);
var a = 10;
```

### 👉 Output:

```
undefined
```

### 🧠 Why?

JavaScript internally converts it to:

```js
var a;        // hoisted
console.log(a);
a = 10;
```

So `a` exists but has value `undefined`.

---

# 🔹 Example with `let`

```js
console.log(b);
let b = 20;
```

### 👉 Output:

```
ReferenceError
```

Why?

Because `let` is hoisted BUT placed in **Temporal Dead Zone (TDZ)**.

---

# 🔥 What is Temporal Dead Zone (TDZ)?

TDZ is the time between:

* Variable declaration being hoisted
* And actual initialization

Example:

```js
{
  console.log(x); // ❌ Error
  let x = 5;
}
```

Even though `x` is hoisted, you cannot access it before initialization.

---

# 🔹 Example with `const`

```js
console.log(c);
const c = 30;
```

👉 Also gives **ReferenceError**

Because `const` also lives in TDZ.

---

# 🔹 Function Hoisting

## ✅ Function Declaration (Fully Hoisted)

```js
greet();

function greet() {
  console.log("Hello");
}
```

✔ Works perfectly.

Because function declarations are fully hoisted.

---

## ❌ Function Expression (Not Hoisted Like Declaration)

```js
greet();

var greet = function() {
  console.log("Hello");
};
```

👉 Output:

```
TypeError: greet is not a function
```

Because only variable `greet` is hoisted, not the function definition.

Internally:

```js
var greet;
greet(); // undefined()
greet = function() { ... }
```

---

# 🔥 Hoisting Summary Table

| Type                 | Hoisted? | Behavior                   |
| -------------------- | -------- | -------------------------- |
| var                  | Yes      | Initialized with undefined |
| let                  | Yes      | In TDZ                     |
| const                | Yes      | In TDZ                     |
| Function Declaration | Yes      | Fully hoisted              |
| Function Expression  | No       | Only variable hoisted      |

---

# 🧠 Important Interview Trick Question

```js
var x = 10;

function test() {
  console.log(x);
  var x = 20;
}

test();
```

👉 Output:

```
undefined
```

Why?

Inside function:

```js
function test() {
  var x;        // hoisted locally
  console.log(x);
  x = 20;
}
```

Local `x` shadows global `x`.

---
