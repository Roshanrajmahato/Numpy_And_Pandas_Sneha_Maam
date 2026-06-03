# 🔥 Important Interview Concepts

* Promise is an object
* It handles asynchronous operations
* Has 3 states
* Supports chaining
* Can be used with async/await

# 💡 Interview One-Line Answer

> A Promise is an object that represents the eventual success or failure of an asynchronous operation and allows handling it using `.then()`, `.catch()`, and `async/await`.

# ✅ 14. What are JavaScript Promises?

---

## 🔹 Definition

A **Promise** is an object that represents the **eventual completion (or failure)** of an asynchronous operation.

👉 It is used to handle asynchronous tasks like:

* API calls
* Database queries
* File reading
* Timers

---

# 🔥 Why Promises Were Introduced?

Before Promises, we used:

❌ Callbacks → which led to **Callback Hell**

Example:

```javascript
getData(function(result) {
  processData(result, function(finalResult) {
    saveData(finalResult, function() {
      console.log("Done");
    });
  });
});
```

Messy 😓

Promises solve this problem.

---

# 🔹 Promise States

A Promise has 3 states:

1️⃣ **Pending** → Initial state
2️⃣ **Fulfilled** → Operation successful
3️⃣ **Rejected** → Operation failed

---

# 🔥 Creating a Promise

```javascript
const myPromise = new Promise((resolve, reject) => {

  let success = true;

  if (success) {
    resolve("Task completed");
  } else {
    reject("Task failed");
  }

});
```

---

# 🔥 Consuming a Promise

We use:

* `.then()` → for success
* `.catch()` → for error
* `.finally()` → always runs

---

### Example:

```javascript
myPromise
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.log(error);
  })
  .finally(() => {
    console.log("Done");
  });
```

---

# 🔥 Real Example with `setTimeout`

```javascript
const wait = new Promise((resolve) => {
  setTimeout(() => {
    resolve("2 seconds finished");
  }, 2000);
});

wait.then(message => console.log(message));
```

Output after 2 seconds:

```
2 seconds finished
```

---

# 🔥 Real Project Example (API Call)

```javascript
fetch("https://api.example.com")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

`fetch()` returns a Promise.

---

# 🔥 Promise Chaining (Very Important)

```javascript
fetch("https://api.example.com")
  .then(res => res.json())
  .then(data => {
    return data.user;
  })
  .then(user => {
    console.log(user);
  })
  .catch(error => console.log(error));
```

Each `.then()` returns a new Promise.

---

# 🔥 Async/Await (Modern Way 🔥🔥)

Promises can be written cleaner using `async/await`.

### Same example:

```javascript
async function getData() {
  try {
    const response = await fetch("https://api.example.com");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

getData();
```

✔ Looks synchronous
✔ Easier to read
✔ Preferred in modern JS

---

# 🔥 Promise vs Callback

| Feature         | Callback  | Promise         |
| --------------- | --------- | --------------- |
| Readability     | Messy     | Cleaner         |
| Error Handling  | Difficult | Easy with catch |
| Chaining        | Hard      | Easy            |
| Modern Standard | ❌ Old     | ✅ Modern        |

---


---
