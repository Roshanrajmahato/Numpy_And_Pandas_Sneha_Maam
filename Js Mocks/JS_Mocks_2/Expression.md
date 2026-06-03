
# 11. Perfect Interview Definition

> An Expression in JavaScript is any valid code that returns a value, such as arithmetic, logical, relational, or function expressions.
> Conditions are decision-making structures like if, if-else, switch, and ternary that execute code based on truthy or falsy evaluation.

# 1. What is an Expression in JavaScript?

👉 **Expression = Any valid unit of code that produces a value**

* It can be:

  * a literal
  * variable
  * operator combination
  * function call

### Examples

```js
10 + 20          // expression → gives 30
"Hello" + "JS"   // → "HelloJS"
a > b            // → true/false
x = 5            // → 5
```

---

## 1.1 Types of Expressions

### A. Arithmetic Expressions

```js
10 + 5
a * b
x - y
```

Operators: `+ - * / % **`

---

### B. Relational / Comparison Expressions

```js
10 > 5
a <= b
x == y
```

Return → Boolean

---

### C. Logical Expressions

```js
a && b
x || y
!z
```

---

### D. Assignment Expressions

```js
x = 10
x += 5
y *= 2
```

---

### E. Function Expressions

```js
let add = function(a,b){
   return a+b;
}
```

---

### F. Conditional (Ternary) Expression

```js
let result = age >= 18 ? "Adult" : "Minor";
```

---

### G. Object / Array Expressions

```js
[1,2,3]
{ name: "Roshan" }
```

---

# 2. What are Conditions in JavaScript?

👉 Conditions allow program to take decisions based on expressions.

Main conditional statements:

1. if
2. if-else
3. else if ladder
4. switch
5. ternary operator

---

# 3. Conditional Statements (Detailed)

---

## A. if Statement

```js
if (condition) {
   // code
}
```

### Example

```js
let age = 20;

if (age >= 18) {
   console.log("Eligible");
}
```

---

## B. if-else

```js
if (age >= 18) {
   console.log("Adult");
} else {
   console.log("Minor");
}
```

---

## C. else if ladder

```js
let marks = 85;

if (marks >= 90) {
   console.log("A+");
}
else if (marks >= 80) {
   console.log("A");
}
else {
   console.log("B");
}
```

---

## D. switch statement

```js
let day = 2;

switch(day) {
  case 1:
    console.log("Mon");
    break;

  case 2:
    console.log("Tue");
    break;

  default:
    console.log("Invalid");
}
```

👉 Faster than multiple else-if in many cases.

---

## E. Ternary Operator

```js
let result = age >= 18 ? "Adult" : "Minor";
```

---

# 4. Truthy and Falsy Values (Very Important)

## Falsy Values

* false
* 0
* ""
* null
* undefined
* NaN

Everything else → Truthy

### Example

```js
if (0) console.log("Hello");   // not run

if (" ") console.log("Hi");    // run → space is truthy
```

---

# 5. Short Circuit Evaluation

```js
false && console.log("Hello");  // not execute
true || console.log("Hello");   // not execute
```

---

# 6. Difference: == vs ===

```js
5 == "5"   // true  → value check
5 === "5"  // false → value + type
```

👉 Always prefer ===

---

# 7. Nested Conditions

```js
if (age >= 18) {
   if (hasID) {
      console.log("Allowed");
   }
}
```

---

# 8. Edge Cases (Interview Tricky)

## 1. Assignment inside if

```js
let a = 5;

if (a = 10) {
   console.log(a);   // 10 😮
}
```

👉 Assignment returns value → truthy

---

## 2. Empty array is truthy

```js
if ([]) console.log("Yes");   // Yes
```

---

## 3. String "0" is truthy

```js
if ("0") console.log("True");  // True
```

---

## 4. switch uses === internally

```js
switch(5) {
 case "5":
   // not match
}
```

---

# 9. Interview Questions

### Q1. What is expression?

> Expression is a piece of code that produces a value.

---

### Q2. Difference between statement and expression?

| Expression               | Statement               |
| ------------------------ | ----------------------- |
| Returns value            | Performs action         |
| Can be part of statement | Cannot be used as value |

Example:

```js
5 + 3   // expression
if(x>5) // statement
```

---

### Q3. == vs === ?

* == → value
* === → value + type

---

### Q4. What are falsy values?

6 values →
false, 0, "", null, undefined, NaN

---

### Q5. switch vs if-else?

* switch → exact match
* if → range conditions
* switch uses ===

---

### Q6. What is ternary operator?

```js
condition ? exp1 : exp2
```

---

# 10. Output Questions

### 1️⃣

```js
if ("") console.log("A");
else console.log("B");
```

👉 B

---

### 2️⃣

```js
console.log(5 == "5");   // true
console.log(5 === "5");  // false
```

---

### 3️⃣

```js
if ([]){
  console.log("Hello");
}
```

👉 Hello

---

### 4️⃣

```js
if (null || 0 || "hi") {
  console.log("Yes");
}
```

👉 Yes

---
