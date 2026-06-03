
# 15. Perfect Interview Definition

> setTimeout executes a function once after a specified delay, while setInterval executes a function repeatedly at fixed intervals. Both are asynchronous Web API timers controlled using clearTimeout and clearInterval.

---

# 1. Basic Meaning

Both are used to execute JavaScript code **after some time delay**, but their behavior is different.

| setTimeout          | setInterval         |
| ------------------- | ------------------- |
| Executes ONCE       | Executes REPEATEDLY |
| After delay         | After every delay   |
| Needs manual recall | Auto repeat         |

---

# 2. Syntax

## setTimeout

```js
setTimeout(function, delay);
```

## setInterval

```js
setInterval(function, delay);
```

👉 delay in milliseconds (1000ms = 1 sec)

---

# 3. Example – setTimeout

```js
setTimeout(()=>{
  console.log("Hello");
}, 2000);
```

👉 Output after 2 seconds → Hello (only once)

---

# 4. Example – setInterval

```js
setInterval(()=>{
  console.log("Hi");
}, 2000);
```

👉 Output every 2 seconds → Hi Hi Hi…

---

# 5. Clearing Timers

## clearTimeout

```js
let id = setTimeout(fn,2000);

clearTimeout(id);
```

## clearInterval

```js
let id = setInterval(fn,2000);

clearInterval(id);
```

---

# 6. Internal Working

* Both are **Web APIs**
* Go to callback queue
* Execute after main stack empty
* Not exact time → minimum time

---

# 7. Key Differences

| Feature   | setTimeout   | setInterval    |
| --------- | ------------ | -------------- |
| Execution | Once         | Repeated       |
| Stop      | clearTimeout | clearInterval  |
| Use       | Delay task   | Repeating task |

---

# 8. Real Use Cases

### setTimeout

* Loader hide
* Delayed message
* Debounce

### setInterval

* Clock
* Slider
* Polling

---

# 9. Example – Digital Clock

```js
setInterval(()=>{
 let d = new Date();
 console.log(d.toLocaleTimeString());
},1000);
```

---

# 10. Trick Interview Question

### Q: Is timing exact?

👉 No

* Depends on event loop
* Minimum delay not exact

---

# 11. Nested Timeout instead of Interval

```js
function test(){
 console.log("hi");

 setTimeout(test,1000);
}
test();
```

👉 Better than interval sometimes

---

# 12. Interview Questions

### Q1. Difference?

> setTimeout runs once, setInterval runs repeatedly.

---

### Q2. How to stop?

* clearTimeout
* clearInterval

---

### Q3. Which better for animation?

👉 setInterval (but requestAnimationFrame best)

---

### Q4. Exact timing?

👉 No guarantee

---

# 13. Output Questions

### 1️⃣

```js
setTimeout(()=>console.log(1),0);
console.log(2);
```

👉 2 1

---

### 2️⃣

```js
setInterval(()=>console.log("a"),1000);
```

👉 infinite a

---

# 14. Common Mistakes

❌

```js
clearInterval(setInterval(fn,1000));
```

✔

```js
let id = setInterval(fn,1000);
clearInterval(id);
```

---
