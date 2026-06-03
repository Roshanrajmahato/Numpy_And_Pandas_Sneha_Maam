

# 9. Perfect Interview Definition

> JavaScript data types are divided into Primitive and Non-Primitive types.
> Primitive types (String, Number, Boolean, Null, Undefined, Symbol, BigInt) store single immutable values.
> Non-Primitive types like Object and Array store values by reference and are mutable.

---

# 1. What are Data Types in JavaScript?

👉 **Data types define what kind of value a variable can hold.**

JavaScript is a **dynamically typed language**, meaning:

* You don’t need to specify type explicitly.
* Type is decided at runtime.

```js
let a = 10;       // number
a = "hello";      // string → allowed
```

---

# 2. Types of Data Types in JavaScript

JavaScript has **2 categories**

## A. Primitive Data Types (7)

1. String
2. Number
3. Boolean
4. Undefined
5. Null
6. Symbol (ES6)
7. BigInt (ES11)

## B. Non-Primitive (Reference) Types

8. Object

   * Object
   * Array
   * Function
   * Date
   * RegExp

---

# 3. Primitive Data Types (Detailed)

## 1. String

* Sequence of characters
* Immutable
* Can be written in 3 ways

```js
let a = "Hello";
let b = 'World';
let c = `Hello ${a}`;   // template literal
```

### Important Points

* Strings are immutable
* Methods return new string

```js
let s = "hello";
s.toUpperCase();
console.log(s);   // hello (not changed)
```

---

## 2. Number

* Only ONE type for all numbers
* No int, float separately
* Range: ±(2⁵³−1)

```js
let a = 10;
let b = 10.5;
let c = -20;
```

Special values:

```js
Infinity
-Infinity
NaN
```

```js
console.log(10 / 0);     // Infinity
console.log("a" * 2);    // NaN
```

---

## 3. Boolean

```js
let isTrue = true;
let isFalse = false;
```

Used in conditions:

```js
if (true) { }
```

---

## 4. Undefined

* Variable declared but not assigned

```js
let x;
console.log(x);   // undefined
```

---

## 5. Null

* Intentional empty value
* Object type bug (famous JS mistake)

```js
let a = null;
console.log(typeof a);   // object 😮 (language bug)
```

---

## 6. Symbol (ES6)

* Unique and immutable

```js
let s1 = Symbol("id");
let s2 = Symbol("id");

console.log(s1 === s2);   // false
```

Used in:

* object keys
* uniqueness
* libraries/frameworks

---

## 7. BigInt (ES11)

* For very large numbers

```js
let a = 1234567890123456789012345n;
let b = BigInt(100);
```

Cannot mix with normal number:

```js
// 10n + 5 → ERROR
```

---

# 4. Non-Primitive (Reference Types)

## 1. Object

```js
let user = {
  name: "Roshan",
  age: 22
};
```

## 2. Array

```js
let arr = [1,2,3];
```

## 3. Function

```js
function test() {}
```

---

# 5. typeof Operator (Very Important)

```js
typeof "hello"   // string
typeof 10        // number
typeof true      // boolean
typeof undefined // undefined
typeof null      // object (bug)
typeof {}        // object
typeof []        // object
typeof function(){} // function
```

---

# 6. Primitive vs Reference (Most Important)

| Primitive       | Reference           |
| --------------- | ------------------- |
| Stored by value | Stored by reference |
| Immutable       | Mutable             |
| Copied by value | Copied by address   |

### Example

```js
let a = 10;
let b = a;
b = 20;

console.log(a); // 10
```

### Reference Example

```js
let obj1 = { x: 10 };
let obj2 = obj1;

obj2.x = 20;

console.log(obj1.x); // 20
```

👉 Same memory reference!

---

# 7. Tricky / Edge Cases

## 1. null vs undefined

```js
null == undefined   // true
null === undefined  // false
```

## 2. NaN behavior

```js
NaN == NaN   // false
isNaN(NaN)   // true
```

---

## 3. Array is object

```js
typeof []  // object
Array.isArray([]) // true
```

---

## 4. Number precision issue

```js
0.1 + 0.2 === 0.3   // false 😮
```

Reason: floating point precision

---

# 8. Interview Questions & Answers

### Q1. How many data types in JS?

7 Primitive + 1 Non-primitive (Object)

---

### Q2. Difference between null and undefined?

| null              | undefined        |
| ----------------- | ---------------- |
| Intentional empty | Uninitialized    |
| type → object     | type → undefined |

---

### Q3. Why typeof null is object?

👉 Historical bug in JavaScript
👉 Cannot be fixed due to backward compatibility

---

### Q4. Is array primitive?

❌ No, it is object type.

---

### Q5. What is Symbol?

👉 Unique identifier, mostly used for object keys.

---

### Q6. What is BigInt?

👉 For numbers > 2⁵³−1

---

### Q7. Primitive vs Reference?

* Primitive → value copy
* Reference → address copy


# 10. Output Based Questions (Must Practice)

### 1️⃣

```js
console.log(typeof null);
```

👉 object

### 2️⃣

```js
console.log(typeof NaN);
```

👉 number

### 3️⃣

```js
console.log([] == []);
```

👉 false

### 4️⃣

```js
console.log(null == undefined);
```

👉 true

---

If you want Roshan, I can give you:

👉 20 MCQs
👉 Output prediction set
👉 Viva short answers for exams

Tell me 👍
