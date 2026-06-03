# 🔹 What is a Function in JavaScript?

A **function** is a reusable block of code designed to perform a specific task.

It helps:

* Avoid repetition
* Improve readability
* Organize logic

---
## Type Of Functions

* 1️⃣ Named Function (Function Declaration)
* 2️⃣ Anonymous Function
* 3️⃣ Arrow Function (ES6)

# 1️⃣ Named Function (Function Declaration)

## ✅ Definition:

A function that has a name.

### ✔ Features:

* Has a function name
* Can be called before declaration (hoisting works)
* Mostly used for reusable logic

### 🧠 Syntax:

```javascript
function functionName(parameters) {
   // code
}
```

---

## 🔥 5 Examples of Named Functions

### 1️⃣ Simple Greeting

```javascript
function greet(name) {
  return "Hello " + name;
}
console.log(greet("Roshan"));
```

---

### 2️⃣ Addition

```javascript
function add(a, b) {
  return a + b;
}
console.log(add(10, 20));
```

---

### 3️⃣ Even or Odd

```javascript
function isEven(num) {
  return num % 2 === 0;
}
console.log(isEven(4));
```

---

### 4️⃣ Calculate Area

```javascript
function areaOfRectangle(length, width) {
  return length * width;
}
console.log(areaOfRectangle(5, 3));
```

---

### 5️⃣ Default Parameter

```javascript
function welcome(name = "Guest") {
  return "Welcome " + name;
}
console.log(welcome());
```

---

# 2️⃣ Anonymous Function

## ✅ Definition:

A function **without a name**.

Used mostly:

* Inside variables
* Inside callbacks
* Inside event listeners

### 🧠 Syntax:

```javascript
const variableName = function(parameters) {
   // code
};
```

---

## 🔥 5 Examples of Anonymous Functions

### 1️⃣ Stored in Variable

```javascript
const greet = function(name) {
  return "Hello " + name;
};
console.log(greet("Roshan"));
```

---

### 2️⃣ Inside setTimeout (Asynchronous Example)

```javascript
setTimeout(function() {
  console.log("Executed after 2 seconds");
}, 2000);
```

---

### 3️⃣ Array map()

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(function(num) {
  return num * 2;
});
console.log(doubled);
```

---

### 4️⃣ Event Listener

```javascript
document.addEventListener("click", function() {
  console.log("Document clicked");
});
```

---

### 5️⃣ Filter Example

```javascript
const nums = [10, 15, 20, 25];
const result = nums.filter(function(n) {
  return n > 15;
});
console.log(result);
```

---

# 3️⃣ Arrow Function (ES6)

Introduced in **ES6 (2015)**.

## ✅ Definition:

A shorter way to write functions using `=>`

### ✔ Features:

* Short syntax
* No own `this`
* Cannot use as constructor
* Not hoisted like named function

### 🧠 Syntax:

```javascript
const functionName = (parameters) => {
   // code
};
```

---

## 🔥 5 Examples of Arrow Functions

### 1️⃣ Simple Arrow

```javascript
const greet = (name) => {
  return "Hello " + name;
};
console.log(greet("Roshan"));
```

---

### 2️⃣ Short One-Line Arrow

```javascript
const add = (a, b) => a + b;
console.log(add(5, 7));
```

---

### 3️⃣ Square Number

```javascript
const square = num => num * num;
console.log(square(6));
```

---

### 4️⃣ Array map()

```javascript
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);
console.log(doubled);
```

---

### 5️⃣ setTimeout with Arrow

```javascript
setTimeout(() => {
  console.log("Arrow function executed");
}, 1000);
```











Here is a **complete list of common JavaScript Event Names** grouped by category. This will help you while learning **DOM Events and Event Listeners** 👍

---

# 🧠 All Common JavaScript Event Names
