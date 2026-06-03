
# 12. Perfect Interview Definition

> The ternary operator (`? :`) is a conditional operator used as a shorthand for if–else. It evaluates a condition and returns one of two expressions, making code concise and suitable for simple decision-making.

---

# 1. What is Ternary Operator?

👉 **Ternary Operator is a shorthand of if–else condition.**

It is the only operator in JavaScript that takes **3 operands**, therefore called *ternary*.

---

## Syntax

```js
condition ? expression1 : expression2;
```

* If condition = true → expression1 executes
* If condition = false → expression2 executes

---

# 2. Basic Example

## Using if–else

```js
let age = 20;
let result;

if(age >= 18){
  result = "Adult";
}
else{
  result = "Minor";
}
```

## Same using Ternary

```js
let result = age >= 18 ? "Adult" : "Minor";
```

👉 Short + clean + readable

---

# 3. How It Works (Internal)

1. Condition evaluated
2. Converted to Boolean
3. First value if true
4. Second if false

---

# 4. Multiple Examples

### 1️⃣ Check Even Odd

```js
let n = 10;
let r = n % 2 == 0 ? "Even" : "Odd";
```

---

### 2️⃣ Login Check

```js
let isLogin = true;

let msg = isLogin ? "Welcome" : "Please Login";
```

---

### 3️⃣ Function Return

```js
function check(a){
 return a>0 ? "Positive" : "Negative";
}
```

---

# 5. Nested Ternary

```js
let num = 0;

let r = num > 0 ? "Positive"
       : num < 0 ? "Negative"
       : "Zero";
```

👉 Works like else-if ladder

---

# 6. Ternary vs if–else

| Ternary            | if–else          |
| ------------------ | ---------------- |
| Short              | Long             |
| Expression         | Statement        |
| Returnable         | Not directly     |
| Readable for small | Hard for complex |

---

# 7. Where to Use

* Variable assignment
* JSX (React)
* Short conditions
* Return statements

---

# 8. Where NOT to Use

❌ Complex logic
❌ Many nested conditions
❌ Multiple statements

---

# 9. Interview Questions

### Q1. What is ternary operator?

> It is shorthand of if–else using ? :

---

### Q2. Syntax?

```js
condition ? truePart : falsePart
```

---

### Q3. Can we nest?

👉 Yes

---

### Q4. Difference from if else?

* Ternary is expression
* if else is statement

---

### Q5. Can we execute function?

```js
age>18 ? vote() : noVote();
```

👉 Yes

---

# 10. Output Questions

### 1️⃣

```js
5>3 ? console.log("A") : console.log("B");
```

👉 A

---

### 2️⃣

```js
let x = 0 ? "A" : "B";
```

👉 B

---

### 3️⃣

```js
let y = "" ? 1 : 2;
```

👉 2  ("" is falsy)

---

# 11. Falsy Values in Ternary

* 0
* ""
* null
* undefined
* NaN
* false

---
