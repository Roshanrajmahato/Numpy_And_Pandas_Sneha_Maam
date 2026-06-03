
# 14. Perfect Definition

> ES6 introduced modern features like let/const for block scope, arrow functions for concise syntax, template literals for string interpolation, destructuring for easy extraction, modules for code splitting, and async/await for better async handling.


---

# 1. let and const

## let

* Block scoped
* Can be reassigned
* No hoisting access

```js
let a = 10;
a = 20;
```

## const

* Block scoped
* Cannot be reassigned

```js
const x = 5;
x = 6; ❌ error
```

### Interview

* var → function scope
* let/const → block scope
* const for constant reference

---

# 2. Arrow Function

```js
const add = (a,b)=> a+b;
```

### Features

* Short syntax
* No this binding
* No arguments object

### Interview

* Cannot use as constructor
* this comes from parent

---

# 3. Template Literals

```js
let name="Roshan";
console.log(`Hello ${name}`);
```

✔ Multiline
✔ Expression support

---

# 4. Default Parameter

```js
function add(a=5,b=10){
 return a+b;
}
```

---

# 5. Rest Parameter

```js
function sum(...a){
 return a.reduce((x,y)=>x+y);
}
```

👉 Converts to array

---

# 6. Destructuring

## Array

```js
let [a,b]=[10,20];
```

## Object

```js
let {name,age}=obj;
```

---

# 7. Modules – Export / Import

## file1.js

```js
export const a=10;

export function test(){}
```

## file2.js

```js
import {a,test} from './file1.js';
```

### Default Export

```js
export default app;
import app from './file';
```

---

# 8. Async / Await

```js
async function load(){

 let r = await fetch("api");
 let d = await r.json();

}
```

✔ Cleaner than then

---

# 9. Promise.all()

```js
Promise.all([p1,p2])
.then(res=>console.log(res));
```

* Wait all
* If one fail → fail

---

# 10. String Methods

```js
includes()
startsWith()
endsWith()
repeat()
```

---

# 11. Other ES6 Features

* Spread
* Map/Set
* Classes

---

# 12. Interview Questions

### Q1. let vs var?

* block vs function

### Q2. Arrow this?

* lexical this

### Q3. Rest vs Spread?

* rest → parameter
* spread → expand

### Q4. Promise.all?

* all success

---

# 13. Output

```js
let a=5;
{
 let a=10;
}
console.log(a); //5
```

---
