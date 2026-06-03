
# 🔹 Perfect Interview Definition

> `let` and `const` are block-scoped variables introduced in ES6. `let` allows reassignment but not redeclaration, while `const` does not allow reassignment and must be initialized at declaration. Both are hoisted but exist in a temporal dead zone until initialized.

---

If you want Roshan, I can also give:

* Deep explanation of TDZ with memory diagram
* 20 tricky output questions
* Real-world coding interview examples

Tell me 👍
# 🔹 1. let in JavaScript

## ✅ Definition

`let` is a block-scoped variable introduced in **ECMAScript 2015 (ES6)**.

---

## 🔹 Key Features of let

1. Block Scoped
2. Can be reassigned
3. Cannot be redeclared in same scope
4. Temporal Dead Zone (TDZ)
5. Hoisted but not initialized

---

## 🔹 Block Scope Example

```js
{
   let a = 10;
}
console.log(a); // ❌ Error
```

👉 Because `let` works inside `{}` block only.

---

## 🔹 Reassignment Allowed

```js
let a = 10;
a = 20;  // ✅ allowed
```

---

## 🔹 Cannot Redeclare

```js
let a = 5;
let a = 6;  // ❌ Error
```

---

## 🔹 Temporal Dead Zone (Important Interview Point)

```js
console.log(a);
let a = 10;
```

👉 ❌ ReferenceError

Although `let` is hoisted, it stays in **Temporal Dead Zone** until declaration line.

---

# 🔹 2. const in JavaScript

## ✅ Definition

`const` is also block-scoped and introduced in **ECMAScript 2015 (ES6)**.

---

## 🔹 Key Features of const

1. Block Scoped
2. Cannot be reassigned
3. Must be initialized
4. Cannot be redeclared
5. Value cannot change (but object properties can)

---

## 🔹 Basic Example

```js
const x = 5;
x = 6;  // ❌ Error
```

---

## 🔹 Must Initialize

```js
const a;  // ❌ Error
```

---

## 🔹 Object with const (Very Important Interview Question)

```js
const obj = {name:"Roshan"};

obj.name = "Raj";  // ✅ allowed
```

👉 const prevents reassignment, not mutation.

But:

```js
obj = {};  // ❌ Error
```

---

# 🔹 Difference Between var, let and const

| Feature   | var      | let       | const     |
| --------- | -------- | --------- | --------- |
| Scope     | Function | Block     | Block     |
| Reassign  | Yes      | Yes       | No        |
| Redeclare | Yes      | No        | No        |
| Hoisted   | Yes      | Yes (TDZ) | Yes (TDZ) |

---

# 🔹 Tricky Interview Outputs

### 1️⃣

```js
let a = 10;
{
  let a = 20;
}
console.log(a);
```

👉 10

---

### 2️⃣

```js
const a = [1,2];
a.push(3);
console.log(a);
```

👉 [1,2,3]

---

### 3️⃣

```js
{
 console.log(a);
 let a = 5;
}
```

👉 ReferenceError (TDZ)

---

# 🔹 Best Practices

✔ Use `const` by default
✔ Use `let` when value changes
❌ Avoid `var` in modern JS

---

