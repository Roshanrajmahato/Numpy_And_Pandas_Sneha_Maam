 
# 14. Perfect Interview Definition

> Promise is a JavaScript object used to handle asynchronous operations. It represents a value that may be available now, later, or never. It has three states: pending, fulfilled, and rejected, and is consumed using then(), catch(), and finally() methods to avoid callback hell.

# 1. What is Promise?

👉 **Promise is an object that represents the future result of an asynchronous operation.**

### Simple Meaning

* Promise = “I will give you result later”
* Either:

  * Success → resolve
  * Failure → reject

---

## Real Life Example

You order food online:

* Pending → cooking
* Fulfilled → delivered
* Rejected → order cancelled

Same in JavaScript.

---

# 2. States of Promise

A Promise has **3 states**

1. Pending
2. Fulfilled (Resolved)
3. Rejected

---

# 3. Why Promise Needed?

Before Promise → callbacks → callback hell

```js
login(()=>{
   getData(()=>{
      showData(()=>{
      })
   })
})
```

👉 Promise solves this nesting problem.

---

# 4. Syntax of Promise

```js
let p = new Promise(function(resolve, reject){

   let success = true;

   if(success){
      resolve("Done");
   }
   else{
      reject("Error");
   }

});
```

---

# 5. How to Use Promise

## then() → for success

## catch() → for error

```js
p.then((res)=>{
   console.log(res);
})
.catch((err)=>{
   console.log(err);
});
```

---

# 6. Real Example

```js
function getData(){

 return new Promise((resolve,reject)=>{

   setTimeout(()=>{
      resolve("Data Loaded");
   },2000);

 });

}

getData().then(res=>{
 console.log(res);
});
```

---

# 7. Promise Chaining

```js
fetchData()
.then(a => a+1)
.then(b => b+1)
.then(c => console.log(c))
.catch(err=>console.log(err));
```

👉 No callback hell

---

# 8. Promise Methods

## 1. Promise.all()

* Wait for all promises
* If one fails → all fail

```js
Promise.all([p1,p2,p3])
.then()
.catch();
```

---

## 2. Promise.race()

* First finished wins

---

## 3. Promise.any()

* First success

---

## 4. Promise.allSettled()

* All results

---

# 9. Fetch API with Promise

```js
fetch("api")
.then(res=>res.json())
.then(data=>console.log(data))
.catch(err=>console.log(err));
```

---

# 10. Async Await (Based on Promise)

```js
async function load(){

 try{
   let r = await fetch("api");
 }
 catch(e){}

}
```

---

# 11. Interview Questions

### Q1. What is Promise?

> Promise is an object representing completion or failure of async task.

---

### Q2. States?

* Pending
* Fulfilled
* Rejected

---

### Q3. then vs catch?

* then → resolve
* catch → reject

---

### Q4. Promise.all vs race?

* all → wait all
* race → first

---

### Q5. Why Promise over callback?

* avoid callback hell
* better readability

---

# 12. Output Questions

### 1️⃣

```js
Promise.resolve(5)
.then(a=>a+5)
.then(console.log);
```

👉 10

---

### 2️⃣

```js
Promise.reject("err")
.catch(console.log);
```

👉 err

---

# 13. Internal Working

* Microtask queue
* then goes to microtask
* higher priority than setTimeout

---

