
# 🎯 Interview Short Answer

> A closure is a function that has access to its outer function’s variables even after the outer function has executed. It allows data encapsulation and state preservation.

---

# 🚀 Pro-Level One-Line Answer

> Closure is created when a function retains access to its lexical scope even after the parent function has returned.

# **7️⃣ What are Closures in JavaScript? (Detailed Explanation + Examples)**

---

# 🧠 What is a Closure?

> A closure is a function that remembers and can access variables from its outer (parent) function even after the outer function has finished executing.

In simple words:

👉 **Inner function + Access to outer function variables = Closure**

---

# 🔹 Basic Example

```js
function outer() {
  let count = 0;

  function inner() {
    count++;
    console.log(count);
  }

  return inner;
}

const counter = outer();
counter(); // 1
counter(); // 2
counter(); // 3
```

---

## 🧠 What’s Happening?

1️⃣ `outer()` runs
2️⃣ It returns `inner` function
3️⃣ `count` should normally disappear
4️⃣ BUT it doesn’t ❗
5️⃣ Because `inner` keeps reference to `count`

This remembering behavior = **Closure**

---

# 🔥 Why Closures Are Important?

Closures help in:

* Data privacy
* Maintaining state
* Creating function factories
* Implementing counters
* React hooks understanding
* Callbacks & async behavior

---

# 🔹 Real-World Example – Private Variable

```js
function createBankAccount(initialBalance) {
  let balance = initialBalance;

  return {
    deposit: function(amount) {
      balance += amount;
      console.log("Balance:", balance);
    },
    withdraw: function(amount) {
      balance -= amount;
      console.log("Balance:", balance);
    }
  };
}

const account = createBankAccount(1000);

account.deposit(500);   // 1500
account.withdraw(200);  // 1300
```

👉 `balance` cannot be accessed directly
👉 It is private
👉 Only accessible via closure functions

---

# 🔹 Closure with setTimeout (Common Interview Question)

```js
for (var i = 1; i <= 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 1000);
}
```

👉 Output:

```
4
4
4
```

Why?

Because `var` is function-scoped and all callbacks share same `i`.

---

## ✅ Fix Using let

```js
for (let i = 1; i <= 3; i++) {
  setTimeout(function() {
    console.log(i);
  }, 1000);
}
```

Output:

```
1
2
3
```

Because `let` creates new block scope for each loop iteration.

---

# 🔥 Closure Behind the Scenes

When a function is created:

It stores:

* Its code
* Its lexical environment (outer variables)

This stored environment = **Closure**

---

# 🔹 Visual Understanding

```
Outer Function
   ↓
Inner Function
   ↓
Access to Outer Variables
```

Even after outer execution ends.

---
