# 🎯 Interview Short Answer

> `var` is function-scoped and can be re-declared and updated.
> `let` is block-scoped and can be updated but not re-declared.
> `const` is block-scoped and cannot be updated or re-declared.

# **3️⃣ Difference Between `var`, `let`, and `const` in JavaScript (Detailed Explanation)**

These are used to **declare variables** in JavaScript.

---

# 🔹 1️⃣ `var`

### ✅ Old way (before ES6 – 2015)

```js
var name = "Roshan";
```

### 🔹 Features:

* Function scoped ❗
* Can be re-declared
* Can be updated
* Hoisted with `undefined`
* Not block scoped

---

### 🧠 Example – Function Scope

```js
function test() {
  var x = 10;
}
console.log(x); // ❌ Error
```

But:

```js
if (true) {
  var y = 20;
}
console.log(y); // ✅ 20 (Not block scoped!)
```

⚠ This causes bugs.

---

# 🔹 2️⃣ `let`

### ✅ Introduced in ES6 (Modern JS)

```js
let age = 25;
```

### 🔹 Features:

* Block scoped ✅
* Cannot be re-declared
* Can be updated
* Hoisted but in TDZ (Temporal Dead Zone)

---

### 🧠 Example – Block Scope

```js
if (true) {
  let x = 10;
}
console.log(x); // ❌ Error
```

---

### ❌ Cannot Redeclare

```js
let a = 10;
let a = 20; // ❌ Error
```

---

# 🔹 3️⃣ `const`

### ✅ Used for constants

```js
const PI = 3.14;
```

### 🔹 Features:

* Block scoped
* Cannot be re-declared
* Cannot be updated
* Must initialize at declaration

---

### ❌ Not Allowed

```js
const x;
```

---

### ⚠ Important Confusion

Objects declared with `const` CAN be modified!

```js
const person = { name: "Roshan" };
person.name = "Rahul"; // ✅ Allowed
```

But:

```js
person = {}; // ❌ Not allowed
```

Because reference cannot change.

---

# 🔥 var vs let vs const (Comparison Table)

| Feature    | var             | let       | const     |
| ---------- | --------------- | --------- | --------- |
| Scope      | Function        | Block     | Block     |
| Re-declare | Yes             | No        | No        |
| Update     | Yes             | Yes       | No        |
| Hoisted    | Yes (undefined) | Yes (TDZ) | Yes (TDZ) |
| Preferred? | ❌ No            | ✅ Yes     | ✅ Yes     |

---

# 🔥 What is Hoisting Difference?

```js
console.log(a);
var a = 10;
```

Output:

```
undefined
```

But:

```js
console.log(b);
let b = 20;
```

Output:

```
ReferenceError
```

Because `let` and `const` stay in **Temporal Dead Zone (TDZ)**.

---

# 🎯 Best Practice (Important for Interviews)

✅ Use `const` by default
✅ Use `let` when value changes
❌ Avoid `var`

