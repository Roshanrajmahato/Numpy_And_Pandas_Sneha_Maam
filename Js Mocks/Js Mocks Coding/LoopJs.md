Loops in JavaScript are used to repeat a block of code multiple times. They’re fundamental when working with arrays, objects, or any repetitive task.

Here are the main types of loops in JavaScript:

---

### 1. **for loop**

Used when you know how many times you want to loop.

```javascript
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

**How it works:**

* `let i = 0` → start
* `i < 5` → condition
* `i++` → increment

---

### 2. **while loop**

Runs as long as the condition is true.

```javascript
let i = 0;

while (i < 5) {
  console.log(i);
  i++;
}
```

---

### 3. **do...while loop**

Runs **at least once**, then checks the condition.

```javascript
let i = 0;

do {
  console.log(i);
  i++;
} while (i < 5);
```

---

### 4. **for...of loop**

Used for iterating over **iterables** (arrays, strings, etc.).

```javascript
const arr = [10, 20, 30];

for (let value of arr) {
  console.log(value);
}
```

---

### 5. **for...in loop**

Used for iterating over **object properties**.

```javascript
const obj = { name: "John", age: 25 };

for (let key in obj) {
  console.log(key, obj[key]);
}
```

---

### 6. **Array methods (modern alternative)**

Instead of loops, you often use methods like `forEach`, `map`, etc.

```javascript
const arr = [1, 2, 3];

arr.forEach(num => {
  console.log(num);
});
```

---

### Quick comparison

| Loop Type    | Best Use Case              |
| ------------ | -------------------------- |
| `for`        | Known number of iterations |
| `while`      | Unknown iterations         |
| `do...while` | Must run at least once     |
| `for...of`   | Arrays / iterable values   |
| `for...in`   | Object keys                |

---

If you want, I can give you practice problems or show real-world examples (like looping through APIs or DOM elements).
