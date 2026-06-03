
# 🎯 Interview Short Answer

> `undefined` means a variable has been declared but not assigned a value, while `null` represents an intentional absence of value set by the developer.

---

# 🚀 Pro-Level Answer

> `undefined` is automatically assigned by JavaScript when a variable is declared but not initialized, whereas `null` is explicitly assigned by the programmer to indicate an empty or non-existent value.

# 🔹 1️⃣ What is `undefined`?

> `undefined` means a variable has been declared but not assigned a value.

### ✅ Example

```js
let x;
console.log(x);
```

👉 Output:

```
undefined
```

### When does `undefined` occur?

* Variable declared but not assigned
* Function without return
* Missing function parameter
* Accessing non-existing object property

---

### Example – Function without return

```js
function test() {}
console.log(test());
```

👉 Output:

```
undefined
```

---

# 🔹 2️⃣ What is `null`?

> `null` represents an intentional empty value.

It means:

👉 “I intentionally set this variable to have no value.”

### Example

```js
let data = null;
console.log(data);
```

👉 Output:

```
null
```

---

# 🔥 Key Difference

| Feature | undefined    | null                    |
| ------- | ------------ | ----------------------- |
| Meaning | Not assigned | Intentionally empty     |
| Set by  | JavaScript   | Developer               |
| Type    | undefined    | object (historical bug) |

---

# 🧠 Interesting Interview Trick

```js
console.log(typeof undefined);
```

👉 Output:

```
"undefined"
```

```js
console.log(typeof null);
```

👉 Output:

```
"object"
```

⚠ `null` being `"object"` is a **historical JavaScript bug**.

---

# 🔥 Comparison with `==` and `===`

```js
console.log(null == undefined);
```

👉 true

Because loose equality treats them as equal.

But:

```js
console.log(null === undefined);
```

👉 false

Because types are different.

---

# 🔥 Real-World Example

```js
let user = null;  // User not logged in yet
let token;        // Not assigned yet
```

* `user = null` → intentional empty
* `token` → undefined because not assigned

---
