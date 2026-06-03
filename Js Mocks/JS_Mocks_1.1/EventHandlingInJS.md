# 15. Perfect Interview Definition

> Event handling is a mechanism in JavaScript that allows executing code in response to user or browser actions like click, keypress, or submit. It is implemented using addEventListener which provides better control, multiple handlers, and event propagation features.

---

# 1. What is Event Handling?

👉 **Event Handling is the process of executing JavaScript code when some action happens on a webpage.**

### Event = Action performed by user or browser

Examples:

* Click
* Key press
* Mouse move
* Form submit
* Page load

---

# 2. What is an Event Handler?

👉 An **event handler** is a JavaScript function that runs when an event occurs.

---

# 3. Ways of Event Handling

There are **3 ways**:

1. Inline event
2. Traditional event
3. addEventListener (Modern)

---

# 4. 1st Way – Inline Event

```html
<button onclick="show()">Click</button>

<script>
function show(){
 alert("Hello");
}
</script>
```

❌ Not recommended

* Mixes HTML + JS

---

# 5. 2nd Way – Traditional

```html
<button id="btn">Click</button>

<script>
let b = document.getElementById("btn");

b.onclick = function(){
 alert("Hi");
};
</script>
```

❌ Only one event allowed

---

# 6. 3rd Way – addEventListener (Best)

```js
btn.addEventListener("click", function(){
 alert("Hello");
});
```

✔ Multiple events
✔ Separation of code
✔ Best practice

---

# 7. Event Object

```js
btn.addEventListener("click", function(e){
 console.log(e.target);
});
```

👉 e contains:

* type
* target
* clientX
* keyCode

---

# 8. Types of Events

## Mouse Events

* click
* dblclick
* mouseover
* mouseout

## Keyboard

* keydown
* keyup

## Form

* submit
* change
* focus

## Window

* load
* resize

---

# 9. Event Flow

### 1. Capturing

### 2. Target

### 3. Bubbling

```js
addEventListener("click",fn,true); // capturing
```

---

# 10. Real Example – Color Change

```html
<p id="p">Hello</p>
<button id="b">Red</button>

<script>
let p = document.getElementById("p");
let b = document.getElementById("b");

b.addEventListener("click", ()=>{
  p.style.color="red";
});
</script>
```

---

# 11. Remove Event

```js
function test(){}

btn.addEventListener("click",test);

btn.removeEventListener("click",test);
```

---

# 12. Prevent Default

```js
form.addEventListener("submit", e=>{
 e.preventDefault();
});
```

---

# 13. Interview Questions

### Q1. What is Event Handling?

> Executing JS code in response to user actions.

---

### Q2. Best method?

👉 addEventListener

---

### Q3. Difference onclick vs addEventListener?

* onclick → one event
* addEventListener → many

---

### Q4. What is event object?

👉 Contains info about event

---

### Q5. Bubbling vs Capturing?

* Bubble → child → parent
* Capture → parent → child

---

# 14. Output Questions

### 1️⃣

```js
btn.onclick=fn1;
btn.onclick=fn2;
```

👉 only fn2 works

---

### 2️⃣

```js
addEventListener("click",fn1);
addEventListener("click",fn2);
```

👉 both work

---


# 16. Important Lines to Say

* Event driven programming
* addEventListener best
* event object
* bubbling & capturing

---

If you want Roshan, I can give:

👉 Event delegation
👉 Todo app using events
👉 MCQ set

Tell me 👍
