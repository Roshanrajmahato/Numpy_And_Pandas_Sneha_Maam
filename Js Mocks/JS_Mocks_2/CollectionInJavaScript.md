# 10. Perfect Interview Definition

> Collection in JavaScript refers to data structures like Array and String that store multiple values. Arrays are mutable indexed collections, while Strings are immutable collections of characters. Both provide many built-in methods for searching, modifying, iterating, and transforming data.

# 1. What is Collection in JavaScript?

👉 **Collection = A group of multiple values stored in a single variable.**

In JavaScript the most used collections are:

1. **Array** – collection of multiple values
2. **String** – collection of characters

Both provide many **built-in methods** to manipulate data.

---

# 2. ARRAY (Collection of Values)

## 2.1 What is Array?

> Array is an ordered collection of elements stored by index.

### Example

```js
let arr = [10, 20, 30, 40];
```

* Index starts from 0
* Can store mixed data

```js
let a = [10, "Roshan", true];
```

---

## 2.2 Creating Array

```js
let a = [];
let b = new Array(1,2,3);
```

---

## 2.3 Access Elements

```js
arr[0]   // 10
arr.length
```

---

# 3. Built-in Methods of Array

## A. Add / Remove

### 1. push() – add at end

```js
arr.push(50);
```

### 2. pop() – remove from end

```js
arr.pop();
```

### 3. unshift() – add at start

```js
arr.unshift(5);
```

### 4. shift() – remove from start

```js
arr.shift();
```

---

## B. Searching

### 5. indexOf()

```js
arr.indexOf(20);
```

### 6. includes()

```js
arr.includes(30);   // true
```

---

## C. Modification

### 7. splice()

```js
arr.splice(1,1);   // delete
arr.splice(1,0,25); // insert
```

### 8. slice()

```js
arr.slice(1,3);
```

---

## D. Iteration

### 9. forEach()

```js
arr.forEach(v => console.log(v));
```

### 10. map()

```js
arr.map(v => v*2);
```

### 11. filter()

```js
arr.filter(v => v>20);
```

### 12. reduce()

```js
arr.reduce((a,b)=>a+b);
```

---

## E. Other Methods

13. concat()
14. join()
15. reverse()
16. sort()
17. find()
18. findIndex()

---

# 4. STRING (Collection of Characters)

## 4.1 What is String?

> String is sequence of characters enclosed in quotes.

```js
let s = "Roshan";
```

* Immutable
* Indexed

---

## 4.2 Creating String

```js
let a = "hello";
let b = new String("hi");
```

---

# 5. Built-in Methods of String

## A. Length

```js
s.length
```

---

## B. Case Methods

1. toUpperCase()
2. toLowerCase()

```js
s.toUpperCase();
```

---

## C. Search

3. indexOf()
4. lastIndexOf()
5. includes()

```js
s.includes("sh");
```

---

## D. Extract

6. slice()

```js
s.slice(1,4);
```

7. substring()
8. substr()

---

## E. Replace

9. replace()

```js
s.replace("R","M");
```

10. replaceAll()

---

## F. Split & Join

11. split()

```js
"hi bye".split(" ");
```

---

## G. Trim

12. trim()
13. trimStart()
14. trimEnd()

---

## H. Character

15. charAt()
16. charCodeAt()

---

# 6. Difference: Array vs String

| Array         | String            |
| ------------- | ----------------- |
| Mutable       | Immutable         |
| Any type      | Only characters   |
| Many elements | Sequence of chars |

---

# 7. Important Concepts

## 7.1 String Immutability

```js
let s="hi";
s[0]="H";
console.log(s); // hi
```

👉 Not changeable

---

## 7.2 Array is Mutable

```js
arr[0]=100;  // allowed
```

---

## 7.3 map vs forEach

* map → returns new array
* forEach → no return

---

# 8. Interview Questions

### Q1. What is array?

> Ordered collection of elements stored by index.

---

### Q2. String immutable?

👉 Yes

---

### Q3. Difference slice vs splice?

| slice              | splice           |
| ------------------ | ---------------- |
| no change original | changes original |

---

### Q4. map vs filter?

* map → transform
* filter → condition

---

### Q5. reduce use?

👉 To get single value.

---

# 9. Output Questions

### 1️⃣

```js
let a=[1,2,3];
a.push(4);
console.log(a);
```

👉 [1,2,3,4]

---

### 2️⃣

```js
console.log("hi".toUpperCase());
```

👉 HI

---

### 3️⃣

```js
let a=[1,2,3];
let b=a.slice(1);
console.log(b);
```

👉 [2,3]

---

### 4️⃣

```js
"hello".split("");
```

👉 ['h','e','l','l','o']

---

