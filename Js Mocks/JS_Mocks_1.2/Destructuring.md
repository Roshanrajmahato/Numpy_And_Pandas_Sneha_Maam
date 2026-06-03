
# 💡 Interview One-Line Answer

> Destructuring is a JavaScript feature that allows extracting values from arrays and objects into variables using a clean and concise syntax.

> Destructuring :-Assigning a value to a distinct variable by unpacking collection is known as desctructing
# ✅ 19. What is Destructuring in JavaScript?

---

## 🔹 Definition

**Destructuring** is a syntax that allows you to extract values from:

* Arrays
* Objects

And assign them to variables easily.

👉 It makes code cleaner and shorter.

---

# 🔥 1️⃣ Array Destructuring

## ❌ Without Destructuring

```javascript
const arr = [10, 20, 30];

const a = arr[0];
const b = arr[1];
const c = arr[2];
```

Too much code 😓

---

## ✅ With Destructuring

```javascript
const arr = [10, 20, 30];

const [a, b, c] = arr;

console.log(a); // 10
console.log(b); // 20
console.log(c); // 30
```

✔ Cleaner
✔ More readable

---

## 🔥 Skipping Values

```javascript
const arr = [10, 20, 30];

const [first, , third] = arr;

console.log(first); // 10
console.log(third); // 30
```

---

## 🔥 Using Rest Operator

```javascript
const arr = [1, 2, 3, 4, 5];

const [first, ...rest] = arr;

console.log(first); // 1
console.log(rest);  // [2, 3, 4, 5]
```

---

# 🔥 2️⃣ Object Destructuring

## ❌ Without Destructuring

```javascript
const user = {
  name: "Roshan",
  age: 22,
  city: "Delhi"
};

const name = user.name;
const age = user.age;
```

---

## ✅ With Destructuring

```javascript
const user = {
  name: "Roshan",
  age: 22,
  city: "Delhi"
};

const { name, age } = user;

console.log(name); // Roshan
console.log(age);  // 22
```

---

## 🔥 Rename Variables

```javascript
const { name: userName } = user;

console.log(userName); // Roshan
```

---

## 🔥 Default Values

```javascript
const { country = "India" } = user;

console.log(country); // India
```

If property doesn’t exist → default is used.

---

# 🔥 Nested Destructuring (Important 🔥)

```javascript
const user = {
  name: "Roshan",
  address: {
    city: "Delhi",
    pincode: 110001
  }
};

const { address: { city } } = user;

console.log(city); // Delhi
```

---

# 🔥 Destructuring in Function Parameters (Very Common in React)

```javascript
function greet({ name, age }) {
  console.log(name, age);
}

greet({ name: "Roshan", age: 22 });
```

Used heavily in:

* React props
* API responses
* Backend controllers

---

# 🔥 Real Project Example (API Response)

```javascript
const response = {
  status: 200,
  data: {
    user: "Roshan",
    role: "Admin"
  }
};

const { data: { user, role } } = response;

console.log(user); // Roshan
```

---

# 🔥 Why Destructuring is Important?

* Cleaner code
* Less repetition
* Improves readability
* Used heavily in modern JS frameworks

---
