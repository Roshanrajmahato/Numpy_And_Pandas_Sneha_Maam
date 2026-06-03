
# 💡 Interview One-Line Answer

> A shallow copy copies only top-level properties and shares nested references, while a deep copy creates a completely independent copy including nested objects.

# ✅ 13. Difference Between Deep Copy and Shallow Copy in JavaScript

---

# 🔹 First Understand: What is Copy?

When we copy an object or array, there are two possibilities:

* 🔹 **Shallow Copy**
* 🔹 **Deep Copy**

---

# 🔹 1️⃣ Shallow Copy

## 🔹 Definition

A **shallow copy** copies only the **top-level properties**.

If the object contains nested objects,
👉 it copies the **reference**, not the actual value.

---

## 🔥 Example

```javascript
const user = {
  name: "Roshan",
  address: {
    city: "Delhi"
  }
};

const copyUser = { ...user };

copyUser.name = "Aman";
copyUser.address.city = "Mumbai";

console.log(user.name);         // Roshan ✅
console.log(user.address.city); // Mumbai ❌
```

---

### ❓ Why did city change in original?

Because:

* `{ ...user }` creates shallow copy
* Nested object `address` is still referencing same memory

So:

```
user.address === copyUser.address  // true
```

---

# 🔹 How Shallow Copy Works

Shallow copy copies:

✔ Primitive values (string, number, boolean)
❌ References for objects

---

# 🔹 Ways to Create Shallow Copy

### Object

```javascript
const copy = { ...original };
```

or

```javascript
const copy = Object.assign({}, original);
```

---

### Array

```javascript
const arrCopy = [...arr];
```

or

```javascript
const arrCopy = arr.slice();
```

---

# 🔹 2️⃣ Deep Copy

## 🔹 Definition

A **deep copy** copies:

✔ All levels
✔ Nested objects
✔ Creates completely new memory references

Changes in copy do NOT affect original.

---

## 🔥 Example

```javascript
const user = {
  name: "Roshan",
  address: {
    city: "Delhi"
  }
};

const deepCopy = JSON.parse(JSON.stringify(user));

deepCopy.address.city = "Mumbai";

console.log(user.address.city); // Delhi ✅
```

Original not affected.

---

# 🔥 Important Limitation of JSON Method

`JSON.parse(JSON.stringify())`:

❌ Does NOT copy:

* Functions
* Undefined
* Date objects
* Circular references

---

# 🔥 Modern Way (Best Method)

```javascript
const deepCopy = structuredClone(user);
```

✔ Handles nested objects
✔ Safer
✔ Modern browsers support it

---

# 🔥 Visual Difference

### Shallow Copy

```
Original ----> address
Copy     ----> address   (same reference)
```

### Deep Copy

```
Original ----> address (new memory)
Copy     ----> address (different memory)
```

---

# 🔥 Real Project Example (React State)

Wrong ❌

```javascript
state.user.address.city = "Mumbai";
```

Correct ✅

```javascript
setState(prev => ({
  ...prev,
  user: {
    ...prev.user,
    address: {
      ...prev.user.address,
      city: "Mumbai"
    }
  }
}));
```

React requires immutability → deep copy style updates.

---

# 🔥 Comparison Table

| Feature                 | Shallow Copy     | Deep Copy |
| ----------------------- | ---------------- | --------- |
| Copies first level      | ✅ Yes            | ✅ Yes     |
| Copies nested objects   | ❌ No (reference) | ✅ Yes     |
| Memory reference shared | ✅ Yes            | ❌ No      |
| Safe for nested updates | ❌ No             | ✅ Yes     |

---
