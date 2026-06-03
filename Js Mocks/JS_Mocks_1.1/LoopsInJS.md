
# 14. Perfect Interview Definition

> Content can be hidden or shown in JavaScript using DOM manipulation like style.display, style.visibility, or classList methods. The best practice is using classList.toggle to maintain separation of concerns between CSS and JavaScript.

---

# 1. What are Loops in JavaScript?

👉 **Loops are used to execute a block of code repeatedly** until a given condition becomes false.

Without loops:

```js
console.log("Hello");
console.log("Hello");
console.log("Hello");
```

With loop:

```js
for(let i=1; i<=3; i++){
   console.log("Hello");
}
```

---

# 2. Types of Loops in JavaScript

## A. Traditional Loops

1. for
2. while
3. do-while

## B. Modern Loops

4. for…in
5. for…of
6. forEach (array method)

---

# 3. for Loop (Most Used)

### Syntax

```js
for(initialization; condition; increment/decrement) {
   // code
}
```

### Example

```js
for(let i = 1; i <= 5; i++) {
   console.log(i);
}
```

### Internal Working

1. Initialization → once
2. Condition check
3. Execute body
4. Increment
5. Repeat 2–4

---

## Infinite for loop

```js
for(;;){
  // infinite
}
```

---

# 4. while Loop

### Syntax

```js
while(condition) {
   // code
}
```

### Example

```js
let i = 1;

while(i <= 5) {
   console.log(i);
   i++;
}
```

👉 Use when number of iterations is NOT fixed.

---

# 5. do-while Loop

### Executes at least once

```js
let i = 1;

do {
  console.log(i);
  i++;
} while(i <= 5);
```

👉 Condition checked AFTER execution.

---

# 6. for…in Loop

Used to iterate over **object keys / array indexes**

```js
let user = {
  name: "Roshan",
  age: 22
};

for(let key in user) {
  console.log(key, user[key]);
}
```

### With Array

```js
let arr = [10,20,30];

for(let i in arr) {
  console.log(i);      // 0 1 2
}
```

---

# 7. for…of Loop

Used to iterate over **values** of iterable (array, string, map)

```js
let arr = [10,20,30];

for(let val of arr) {
  console.log(val);   // 10 20 30
}
```

---

# 8. forEach (Array Method)

```js
arr.forEach(function(val, index){
   console.log(val);
});
```

👉 Cannot use break/continue inside forEach.

---

# 9. break and continue

## break → exit loop

```js
for(let i=1;i<=5;i++){
  if(i==3) break;
  console.log(i);   // 1 2
}
```

## continue → skip iteration

```js
for(let i=1;i<=5;i++){
  if(i==3) continue;
  console.log(i);   // 1 2 4 5
}
```

---

# 10. Difference Between Loops

| Loop     | Use Case              |
| -------- | --------------------- |
| for      | when iterations known |
| while    | condition based       |
| do-while | run at least once     |
| for-in   | object keys           |
| for-of   | iterable values       |
| forEach  | array functional      |

---

# 11. Edge Cases & Tricky Concepts

## 1. var vs let in loop (Very Important)

### Using var

```js
for(var i=1;i<=3;i++){
 setTimeout(()=>console.log(i),1000);
}
// 4 4 4
```

### Using let

```js
for(let i=1;i<=3;i++){
 setTimeout(()=>console.log(i),1000);
}
// 1 2 3
```

👉 let creates block scope per iteration.

---

## 2. for-in on array (not recommended)

```js
for(let i in [10,20]){
 console.log(i);  // index not value
}
```

---

## 3. forEach cannot break

```js
arr.forEach(v=>{
 if(v==2) break;   // ERROR
});
```

---

## 4. Infinite while mistake

```js
let i=1;
while(i<=5){
  console.log(i);
}
// infinite (no i++)
```

---

# 12. Interview Questions

### Q1. Difference between for-in and for-of?

| for-in           | for-of         |
| ---------------- | -------------- |
| keys/index       | values         |
| objects + arrays | only iterables |
| slower           | faster         |

---

### Q2. Which loop is fastest?

👉 Traditional for loop usually fastest.

---

### Q3. Can we use break in forEach?

❌ No

---

### Q4. Difference while vs do-while?

* while → 0 or more times
* do-while → at least once

---

### Q5. Best loop for object?

👉 for-in

---

### Q6. Best loop for array values?

👉 for-of

---

# 13. Output Questions

### 1️⃣

```js
for(var i=0;i<3;i++){}
console.log(i);
```

👉 3

---

### 2️⃣

```js
for(let i=0;i<3;i++){}
console.log(i);
```

👉 Error (i not defined)

---

### 3️⃣

```js
let a=[1,2];
for(let x in a) console.log(x);
```

👉 0 1

---

### 4️⃣

```js
let a=[1,2];
for(let x of a) console.log(x);
```

👉 1 2

---


If you want Roshan, I can give:

👉 20 output based questions
👉 Programs: star patterns, arrays, objects
👉 viva short answers

Tell me 👍
