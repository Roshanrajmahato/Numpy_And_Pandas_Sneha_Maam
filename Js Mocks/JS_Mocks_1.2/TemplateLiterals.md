
# 🎯 Interview Short Answer

> Template literals are strings enclosed in backticks that allow string interpolation, multi-line strings, and embedded expressions using `${}` syntax.

# **9️⃣ What are Template Literals in JavaScript? (Detailed Explanation)**

# 🧠 What are Template Literals?

> Template literals are a modern way to create strings using backticks `` ` ` `` instead of single or double quotes.

They were introduced in **ES6 (2015)**.

---

# 🔹 Basic Syntax

```js
let name = "Roshan";
let message = `Hello ${name}`;
console.log(message);
```

👉 Output:

```
Hello Roshan
```

---

# 🔥 Why Template Literals Are Powerful?

They provide:

1️⃣ String interpolation
2️⃣ Multi-line strings
3️⃣ Expression embedding
4️⃣ Cleaner string formatting

---

# 🔹 1️⃣ String Interpolation

Instead of:

```js
let name = "Roshan";
let age = 24;
let text = "My name is " + name + " and I am " + age + " years old.";
```

We use:

```js
let text = `My name is ${name} and I am ${age} years old.`;
```

✔ Cleaner
✔ More readable
✔ Less error-prone

---

# 🔹 2️⃣ Multi-line Strings

Before template literals:

```js
let text = "Hello\n" +
           "World";
```

Now:

```js
let text = `Hello
World`;
```

No need for `\n`.

---

# 🔹 3️⃣ Expression Inside `${}`

You can write JavaScript expressions inside template literals.

```js
let a = 10;
let b = 20;

console.log(`Sum is ${a + b}`);
```

👉 Output:

```
Sum is 30
```

---

# 🔹 4️⃣ Function Calls Inside Template Literal

```js
function greet(name) {
  return `Hello ${name}`;
}

console.log(`${greet("Roshan")} 👋`);
```

---

# 🔥 Real-World Example (HTML Template)

```js
let user = {
  name: "Roshan",
  age: 24
};

let card = `
  <div>
    <h2>${user.name}</h2>
    <p>Age: ${user.age}</p>
  </div>
`;

document.body.innerHTML = card;
```

Very commonly used in:

* React
* Dynamic HTML rendering
* Email templates
* API responses formatting

---

# 🔥 Template Literals vs Normal Strings

| Feature         | Normal String | Template Literal |
| --------------- | ------------- | ---------------- |
| Quotes          | ' or "        | ` (backticks)    |
| Multi-line      | ❌ Difficult   | ✅ Easy           |
| Variable Insert | ❌ Using +     | ✅ Using ${}      |
| Expression      | ❌             | ✅                |

---
