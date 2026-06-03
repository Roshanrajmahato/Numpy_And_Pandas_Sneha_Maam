# 8. Perfect Interview Definition

> **var** is function-scoped, allows re-declaration and re-assignment, and is hoisted with `undefined`.
> **let** is block-scoped, allows re-assignment but not re-declaration, and stays in Temporal Dead Zone before initialization.
> **const** is block-scoped, cannot be re-assigned or re-declared, but object  properties can be modified.

---

# 1. Basic Overview

| Feature                | var                                | let          | const        |
| ---------------------- | ---------------------------------- | ------------ | ------------ |
| Scope                  | Function scoped                    | Block scoped | Block scoped |
| Re-declaration         | Allowed                            | Not allowed  | Not allowed  |
| Re-assignment          | Allowed                            | Allowed      | Not allowed  |
| Hoisting               | Yes (initialized with `undefined`) | Yes (TDZ)    | Yes (TDZ)    |
| Global object property | Yes                                | No           | No           |

---

# 2. Theory Explanation

## A. `var`

* Introduced in **ES5 (old JavaScript)**
* Function-scoped, not block-scoped
* Can be **re-declared and re-assigned**
* Hoisted with default value `undefined`

### Example

```js
var x = 10;
var x = 20;   // re-declaration allowed
x = 30;       // re-assignment allowed
console.log(x);   // 30
```

### Scope Problem with var

```js
if (true) {
    var a = 100;
}
console.log(a);   // 100 → because var is NOT block scoped
```

This behavior created many bugs → hence `let` and `const` were introduced.

---

## B. `let`

* Introduced in **ES6**
* Block-scoped
* Cannot be re-declared in same scope
* Can be re-assigned
* Hoisted but inside **Temporal Dead Zone (TDZ)**

### Example

```js
let x = 10;
x = 20;      // allowed
// let x = 30;   // ERROR: Identifier 'x' has already been declared
```

### Block Scope

```js
if (true) {
    let y = 50;
}
// console.log(y);   // ERROR → y is not defined
```

---

## C. `const`

* Block-scoped like `let`
* Cannot be re-declared
* Cannot be re-assigned
* MUST be initialized at declaration time

### Example

```js
const a = 10;
// a = 20;      // ERROR: Assignment to constant variable
// const a = 30; // ERROR: already declared
```

### Important: Objects with const CAN be modified

```js
const user = {
    name: "Roshan"
};

user.name = "Rahul";   // allowed
console.log(user.name);   // Rahul
```

👉 `const` does NOT make object immutable.
It only prevents **reassignment of reference**.

```js
user = {};   // ERROR
```

---

# 3. Internal Working (Hoisting + TDZ)

## Hoisting Behavior

### var

```js
console.log(a);  // undefined
var a = 10;
```

Internally:

```js
var a;
console.log(a);
a = 10;
```

---

### let & const (Temporal Dead Zone)

```js
console.log(b);   // ERROR
let b = 20;
```

* `b` is hoisted
* But not initialized → stays in **TDZ**
* Access before declaration → ReferenceError

Same with `const`.

---

# 4. Key Differences with Examples

## Re-declaration

```js
var a = 10;
var a = 20;   // allowed

let b = 10;
// let b = 20;  // ERROR

const c = 10;
// const c = 20; // ERROR
```

---

## Re-assignment

```js
var x = 10;
x = 20;   // allowed

let y = 10;
y = 20;   // allowed

const z = 10;
z = 20;   // ERROR
```

---

## Block Scope Difference

```js
{
    var a = 10;
    let b = 20;
    const c = 30;
}

console.log(a); // 10
// console.log(b); // error
// console.log(c); // error
```

---

# 5. Edge Cases (Very Important for Interviews)

## 1. Loop with var vs let

### Using var

```js
for (var i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}
// Output: 4 4 4
```

Reason:
`var` is function-scoped → same `i` reference

### Using let

```js
for (let i = 1; i <= 3; i++) {
    setTimeout(() => {
        console.log(i);
    }, 1000);
}
// Output: 1 2 3
```

👉 Each iteration gets new block scope.

---

## 2. const with Arrays

```js
const arr = [1,2,3];
arr.push(4);   // allowed
console.log(arr); // [1,2,3,4]

arr = [5,6];   // ERROR
```

---

## 3. Must Initialize const

```js
const a;   // ERROR
```

---

## 4. Global Object Behavior

```js
var a = 10;
let b = 20;

console.log(window.a); // 10
console.log(window.b); // undefined
```

👉 `var` attaches to global object
👉 `let/const` do NOT

---

# 6. When to Use What (Best Practices)

✅ Use `const` → by default
✅ Use `let` → when value will change
❌ Avoid `var` → outdated & buggy

---

# 7. Interview Points (Short Answers)

### Q1. Main difference?

* `var` → function scope
* `let/const` → block scope

### Q2. Hoisting difference?

* `var` → hoisted with `undefined`
* `let/const` → hoisted in TDZ

### Q3. Re-declaration?

* `var` → allowed
* `let/const` → not allowed

### Q4. Re-assignment?

* `var/let` → allowed
* `const` → not allowed

### Q5. Which to use?

* Prefer → `const`
* Then → `let`
* Avoid → `var`

---

