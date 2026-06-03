
# 21. Perfect Interview Definition

> Functions in JavaScript are reusable blocks of code that can be declared, assigned to variables, passed as arguments, or returned from other functions. JavaScript supports multiple types like declaration, expression, arrow, callback, higher-order, and async functions, making it a first-class functional language.

# 1. What is a Function in JavaScript?

👉 **A function is a reusable block of code designed to perform a specific task.**

### Why use functions?

* Code reusability
* Modular programming
* Easy debugging
* Avoid repetition
* Better readability

---

### Basic Syntax

```js
function functionName(parameters) {
    // code
}
```

### Example

```js
function add(a, b) {
   return a + b;
}

console.log(add(5,10));   // 15
```

---

# 2. Function Terminology

* Function Declaration
* Function Definition
* Function Call / Invocation
* Parameters vs Arguments
* Return statement

```js
function greet(name) {     // parameter
   return "Hello " + name;
}

greet("Roshan");           // argument
```

---

# 3. Types of Functions in JavaScript

## A. Based on Definition Style

1. Function Declaration
2. Function Expression
3. Arrow Function
4. Anonymous Function
5. Named Function Expression
6. IIFE
7. Callback Function
8. Higher Order Function
9. Generator Function
10. Async Function

---

# 4. Function Declaration

```js
function sayHello() {
   console.log("Hello");
}
```

### Features

* Hoisted
* Can be called before declaration

```js
test();

function test(){
  console.log("Hi");
}
```

---

# 5. Function Expression

```js
let add = function(a,b){
   return a+b;
};
```

* Not hoisted
* Treated as variable

```js
// add(); // ERROR
```

---

# 6. Arrow Function (ES6)

```js
let add = (a,b) => a+b;
```

### Features

* Short syntax
* No own `this`
* No arguments object
* Cannot be used as constructor

---

# 7. Anonymous Function

Function without name

```js
setTimeout(function(){
   console.log("Hello");
},1000);
```

---

# 8. IIFE (Immediately Invoked)

```js
(function(){
   console.log("Run immediately");
})();
```

👉 Used for data privacy.

---

# 9. Callback Function

Function passed as argument

```js
function show(result){
  console.log(result);
}

function add(a,b, cb){
  cb(a+b);
}

add(5,6, show);
```

---

# 10. Higher Order Function

👉 Function that takes function OR returns function

```js
function outer(){
  return function(){
     console.log("inner");
  }
}
```

---

# 11. Generator Function

```js
function* gen(){
 yield 1;
 yield 2;
}
```

---

# 12. Async Function

```js
async function getData(){
   return "data";
}
```

---

# 13. Parameters Types

## Default Parameter

```js
function add(a=0,b=0){
 return a+b;
}
```

## Rest Parameter

```js
function sum(...a){
 console.log(a);
}
```

---

# 14. Arguments Object

```js
function test(){
 console.log(arguments);
}
```

👉 Not available in arrow function.

---

# 15. First Class Functions

👉 Functions can be:

* assigned to variable
* passed as argument
* returned from function

---

# 16. Scope in Functions

* Global scope
* Local scope
* Lexical scope
* Closure

```js
function outer(){
 let a=10;

 function inner(){
   console.log(a); // closure
 }
}
```

---

# 17. this keyword in Functions

### Normal Function

```js
function test(){
 console.log(this);
}
```

### Arrow Function

👉 No own this
👉 Takes parent this

---

# 18. Difference Between Function Types

| Feature     | Normal | Arrow   |
| ----------- | ------ | ------- |
| this        | own    | lexical |
| arguments   | yes    | no      |
| constructor | yes    | no      |
| hoisting    | yes    | no      |

---

# 19. Interview Questions

### Q1. What is function?

> Function is reusable block of code that performs specific task.

---

### Q2. Difference declaration vs expression?

| Declaration     | Expression  |
| --------------- | ----------- |
| Hoisted         | Not hoisted |
| Can call before | Cannot      |

---

### Q3. What is arrow function?

> Short syntax function without own this.

---

### Q4. What is callback?

> Function passed as argument to another function.

---

### Q5. What is HOF?

> Function that takes or returns function.

---

### Q6. What is IIFE?

> Function executed immediately.

---

### Q7. What is closure?

> Inner function accessing outer variable.

---

# 20. Output Questions

### 1️⃣

```js
test();
function test(){
 console.log("A");
}
```

👉 A

---

### 2️⃣

```js
add();
let add = function(){};
```

👉 Error

---

### 3️⃣

```js
let a = () => {
 console.log(this);
};
a();
```

👉 window / lexical

---

### 4️⃣

```js
function x(){
 return
 {
   name:"roshan"
 }
}
console.log(x());
```

👉 undefined (automatic semicolon)
