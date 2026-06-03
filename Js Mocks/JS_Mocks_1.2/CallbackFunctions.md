
# 🎯 Interview Short Answer

> A callback function is a function passed as an argument to another function and executed after a certain operation completes. It is commonly used in asynchronous programming and event handling.

---

# 🚀 Pro-Level Answer

> A callback is a higher-order function mechanism in JavaScript where a function is passed into another function to be invoked later, enabling asynchronous and event-driven programming.

# **🔟 What are Callback Functions? (Detailed Explanation)**

---

# 🧠 What is a Callback Function?

> A callback is a function that is passed as an argument to another function and is executed later.

In simple words:

👉 **Function inside another function**
👉 Called after some task completes

---

# 🔹 Basic Example

```js
function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}

function sayBye() {
  console.log("Goodbye!");
}

greet("Roshan", sayBye);
```

### 👉 Output:

```
Hello Roshan
Goodbye!
```

Here:

* `sayBye` is a callback function
* It is passed to `greet`
* It runs after greeting

---

# 🔥 Why Callbacks Are Important?

Callbacks are mainly used for:

* Asynchronous operations
* API calls
* Timers
* Event handling
* File reading
* Database operations

---

# 🔹 Example with `setTimeout` (Async Callback)

```js
setTimeout(function() {
  console.log("Executed after 2 seconds");
}, 2000);
```

Here:

* The anonymous function is a callback
* It runs after 2 seconds

---

# 🔹 Example with Event Listener

```js
button.addEventListener("click", function() {
  console.log("Button clicked!");
});
```

Here:

* The function runs when the user clicks
* It is a callback function

---

# 🔥 Synchronous vs Asynchronous Callback

## 1️⃣ Synchronous Callback

Runs immediately.

```js
function process(callback) {
  callback();
}

process(() => console.log("Done"));
```

---

## 2️⃣ Asynchronous Callback

Runs later.

```js
console.log("Start");

setTimeout(() => {
  console.log("Inside Timeout");
}, 2000);

console.log("End");
```

👉 Output:

```
Start
End
Inside Timeout
```

---

# 🔥 Callback Hell (Important Concept)

When multiple callbacks are nested:

```js
getData(function(a) {
  getMoreData(a, function(b) {
    getEvenMoreData(b, function(c) {
      console.log(c);
    });
  });
});
```

This becomes:
❌ Hard to read
❌ Hard to maintain

Solution:

* Promises
* Async/Await

---

# 🔥 Real-World Example (Array Method)

```js
let numbers = [1, 2, 3];

numbers.forEach(function(num) {
  console.log(num);
});
```

Here:

* The function inside `forEach` is a callback.

---
