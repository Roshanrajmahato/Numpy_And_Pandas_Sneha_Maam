
# 14. Perfect Interview Definition

> Event Listener is a DOM method that registers a function to be executed when a specific event occurs on an element. It supports multiple handlers, event propagation, and better separation of concerns compared to traditional event handling.

---

# 1. What is Event Listener?

👉 **Event Listener is a method that waits for an event to occur on an HTML element and then executes a function.**

It allows JavaScript to respond to user actions like:

* click
* keypress
* mouseover
* submit
* load

---

## Definition (Interview)

> Event Listener is a mechanism that attaches a function to an element which gets executed when a specific event occurs.

---

# 2. Syntax

```js
element.addEventListener(event, function, useCapture);
```

* event → "click", "keyup"
* function → handler
* useCapture → true/false (optional)

---

# 3. Basic Example

```html
<button id="btn">Click</button>

<script>
let b = document.getElementById("btn");

b.addEventListener("click", function(){
  alert("Clicked");
});
</script>
```

---

# 4. Why Use addEventListener?

### Better than onclick

✔ Multiple events allowed
✔ Separation of HTML & JS
✔ More control
✔ Bubbling/capturing

---

# 5. Multiple Listeners

```js
btn.addEventListener("click", fn1);
btn.addEventListener("click", fn2);
```

👉 Both will execute

---

# 6. Event Object

```js
btn.addEventListener("click", function(e){

 console.log(e.target);
 console.log(e.type);

});
```

### Event Object Contains

* target
* type
* clientX, clientY
* keyCode

---

# 7. Remove Event Listener

```js
function test(){}

btn.addEventListener("click", test);

btn.removeEventListener("click", test);
```

👉 Function reference must be same

---

# 8. Event Propagation

## 1. Bubbling (default)

Child → Parent

## 2. Capturing

Parent → Child

```js
addEventListener("click", fn, true); // capture
```

---

# 9. Prevent Default

```js
form.addEventListener("submit", e=>{
 e.preventDefault();
});
```

---

# 10. Real Example

```html
<p id="p">Hello</p>
<button id="b">Red</button>

<script>
let p=document.getElementById("p");
let b=document.getElementById("b");

b.addEventListener("click", ()=>{
 p.style.color="red";
});
</script>
```

---

# 11. Interview Questions

### Q1. What is Event Listener?

> It attaches a function to an event on an element.

---

### Q2. Difference onclick vs addEventListener?

* onclick → one handler
* addEventListener → many

---

### Q3. What is event object?

👉 Gives info about event

---

### Q4. Bubbling vs Capturing?

* Bubble → child to parent
* Capture → parent to child

---

### Q5. How remove event?

👉 removeEventListener

---

# 12. Output Questions

### 1️⃣

```js
btn.onclick=fn1;
btn.onclick=fn2;
```

👉 only fn2

---

### 2️⃣

```js
addEventListener("click",fn1);
addEventListener("click",fn2);
```

👉 both

---

# 13. Best Practices

* Use addEventListener
* Avoid inline events
* Use event delegation
* remove when not needed

---

---
