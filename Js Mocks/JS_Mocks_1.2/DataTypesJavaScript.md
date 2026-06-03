# 🎯 Interview Short Answer

> JavaScript has 7 primitive data types: string, number, bigint, boolean, undefined, null, and symbol. It also has non-primitive types like objects, arrays, and functions, which are stored by reference.

# **2️⃣ What are the different Data Types in JavaScript? (Detailed Explanation)**

JavaScript has **2 main categories** of data types:

```
1️⃣ Primitive Data Types
2️⃣ Non-Primitive (Reference) Data Types
```

---

# 🔹 1️⃣ Primitive Data Types

👉 These store **single values**
👉 They are **immutable**
👉 Stored directly in memory

There are **7 primitive types**:

---

## 1️⃣ String

Used to store text.

```js
let name = "Roshan";
let city = 'Bangalore';
```

✔ Can use single quotes, double quotes, or backticks.

---

## 2️⃣ Number

Stores integers and decimals.

```js
let age = 25;
let price = 99.99;
```

⚠ JavaScript has only ONE number type (no int/float difference).

---

## 3️⃣ BigInt

Used for very large numbers.

```js
let bigNumber = 123456789012345678901234567890n;
```

Used when number exceeds safe integer limit.

---

## 4️⃣ Boolean

Stores true or false.

```js
let isLoggedIn = true;
let isAdmin = false;
```

---

## 5️⃣ Undefined

A variable declared but not assigned value.

```js
let x;
console.log(x); // undefined
```

---

## 6️⃣ Null

Represents intentional empty value.

```js
let data = null;
```

Difference from undefined:

* undefined → not assigned
* null → intentionally empty

---

## 7️⃣ Symbol

Used to create unique identifiers.

```js
let id = Symbol("userId");
```

Mostly used in advanced object handling.

---

# 🔹 2️⃣ Non-Primitive (Reference) Data Types

👉 Store multiple values
👉 Stored by reference
👉 Mutable

Main types:

---

## 1️⃣ Object

Collection of key-value pairs.

```js
let person = {
  name: "Roshan",
  age: 24
};
```

---

## 2️⃣ Array

Stores multiple values in order.

```js
let fruits = ["apple", "banana", "mango"];
```

Arrays are actually objects internally.

---

## 3️⃣ Function

Functions are also objects in JavaScript.

```js
function greet() {
  console.log("Hello");
}
```

---

# 🔥 Primitive vs Non-Primitive (Important Interview Table)

| Feature       | Primitive      | Non-Primitive    |
| ------------- | -------------- | ---------------- |
| Stored        | By value       | By reference     |
| Mutable       | No             | Yes              |
| Example       | string, number | object, array    |
| Copy behavior | Copies value   | Copies reference |

---

## 🧠 Example of Reference Behavior

```js
let obj1 = { name: "Roshan" };
let obj2 = obj1;

obj2.name = "Rahul";

console.log(obj1.name); // Rahul
```

Because both refer to same memory location.

