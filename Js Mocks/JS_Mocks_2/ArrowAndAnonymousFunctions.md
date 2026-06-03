
# 9. Perfect Interview Answer

> Anonymous function is a function without a name that has its own `this`, `arguments`, and can be used as constructor.
> Arrow function is an ES6 function with shorter syntax, lexical `this`, no `arguments`, no prototype, and cannot be used as constructor.

---

# 1. Basic Meaning

### Anonymous Function

👉 A function **without a name** is called an anonymous function.

```js
function() {
   console.log("Hello");
}
```

Usually used as:

* function expression
* callback
* IIFE

---

### Arrow Function

👉 Arrow function is a **short syntax function introduced in ES6** using `=>`.

```js
let add = (a,b) => a + b;
```

Arrow function may be:

* anonymous
* or assigned to variable

---

# 2. Core Differences

| Feature          | Anonymous Function | Arrow Function |
| ---------------- | ------------------ | -------------- |
| Syntax           | function() {}      | () => {}       |
| this binding     | Own this           | Lexical this   |
| arguments object | Available          | Not available  |
| constructor      | Can be used        | Cannot be used |
| Hoisting         | Depends            | Not hoisted    |
| prototype        | Has prototype      | No prototype   |

---

# 3. Detailed Explanation

---

## A. Syntax Difference

### Anonymous

```js
let a = function(x,y){
   return x+y;
};
```

### Arrow

```js
let a = (x,y) => x+y;
```

---

## B. this Keyword (MOST IMPORTANT)

### Anonymous Function → Own this

```js
let obj = {
  name: "Roshan",
  show: function(){
    console.log(this.name);
  }
};

obj.show();   // Roshan
```

---

### Arrow Function → Lexical this

```js
let obj = {
  name: "Roshan",
  show: () => {
    console.log(this.name);
  }
};

obj.show();   // undefined
```

👉 Arrow does NOT have its own `this`
👉 Takes `this` from parent scope

---

## C. arguments Object

### Anonymous

```js
let test = function(){
  console.log(arguments);
};

test(1,2,3);   // works
```

---

### Arrow

```js
let test = () => {
  console.log(arguments);
};

test(1,2);   // ERROR
```

👉 Arrow has NO arguments object
Use rest:

```js
let test = (...a) => console.log(a);
```

---

## D. Constructor Usage

### Anonymous

```js
let Test = function(){
 this.x = 10;
};

let t = new Test();   // works
```

---

### Arrow

```js
let Test = () => {
 this.x = 10;
};

let t = new Test();  // ERROR
```

👉 Arrow cannot be constructor.

---

## E. Hoisting

### Anonymous (function expression)

```js
// test(); // ERROR

let test = function(){};
```

### Arrow

```js
// test(); // ERROR

let test = () => {};
```

👉 Both NOT hoisted.

---

## F. prototype

```js
function A(){}
console.log(A.prototype); // exists

let B = () => {};
console.log(B.prototype); // undefined
```

---

# 4. When to Use What

### Use Arrow When:

* Need lexical this
* Short callback
* map/filter/reduce
* React, modern JS

### Use Anonymous When:

* Need own this
* Need arguments
* Need constructor
* Need prototype

---

# 5. Real Example Difference

## setTimeout Case

### Anonymous

```js
let obj = {
  name:"Roshan",
  show:function(){
    setTimeout(function(){
      console.log(this.name);
    },1000);
  }
};

obj.show(); // undefined
```

---

### Arrow Fix

```js
let obj = {
  name:"Roshan",
  show:function(){
    setTimeout(()=>{
      console.log(this.name);
    },1000);
  }
};

obj.show(); // Roshan
```

👉 Arrow solved this issue.

---

# 6. Edge Cases

## 1. Returning Object

```js
let a = () => { name:"roshan" };
console.log(a());   // undefined
```

Correct:

```js
let a = () => ({ name:"roshan" });
```

---

## 2. Single Parameter

```js
x => x*x
```

---

## 3. No Parameter

```js
() => 10
```

---

# 7. Interview Questions

### Q1. Main difference?

> Arrow has lexical this, anonymous has own this.

---

### Q2. Can arrow be constructor?

❌ No

---

### Q3. arguments object?

* Anonymous → yes
* Arrow → no

---

### Q4. Which is better?

* For callback → Arrow
* For object method → Normal/Anonymous

---

### Q5. Hoisting?

* Both not hoisted when stored in variable.

---

# 8. Output Questions

### 1️⃣

```js
let obj={
 a:10,
 b:()=>{
   console.log(this.a);
 }
};
obj.b();
```

👉 undefined

---

### 2️⃣

```js
let obj={
 a:10,
 b:function(){
   console.log(this.a);
 }
};
obj.b();
```

👉 10

---

### 3️⃣

```js
let a = () => {
 return
 10;
};
console.log(a());
```

👉 undefined

---
