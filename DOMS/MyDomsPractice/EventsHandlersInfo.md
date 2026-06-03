# 🔥 1️⃣ Simple Example – Log the Event Object

```html
<button id="btn">Click Me</button>

<script>
const btn = document.getElementById("btn");

btn.addEventListener("click", function(event) {
  console.log(event);
});
</script>
```

# 🔥 2️⃣ Most Important Properties Inside Event Object

```html
<button id="btn">Click Me</button>

<script>
const btn = document.getElementById("btn");

btn.addEventListener("click", function(event) {
  console.log("Event Type:", event.type);
  console.log("Target Element:", event.target);
  console.log("Mouse X:", event.clientX);
  console.log("Mouse Y:", event.clientY);
});
</script>
```

---

## 🧠 Important Event Properties

| Property                  | Meaning                              |
| ------------------------- | ------------------------------------ |
| `event.type`              | Type of event (click, keyup, etc.)   |
| `event.target`            | Element that triggered event         |
| `event.currentTarget`     | Element that listener is attached to |
| `event.clientX`           | Mouse X position                     |
| `event.clientY`           | Mouse Y position                     |
| `event.key`               | Pressed key (keyboard event)         |
| `event.preventDefault()`  | Stop default action                  |
| `event.stopPropagation()` | Stop bubbling                        |

---

# 🔥 3️⃣ Keyboard Event Example

```html
<input type="text" id="inputBox" placeholder="Press key">

<script>
const input = document.getElementById("inputBox");

input.addEventListener("keydown", function(event) {
  console.log(event);
  console.log("Key Pressed:", event.key);
  console.log("Key Code:", event.code);
});
</script>
```

When you press "A":

```
Key Pressed: a
Key Code: KeyA
```

---

# 🔥 4️⃣ Form Event Example

```html
<form id="myForm">
  <input type="text">
  <button type="submit">Submit</button>
</form>

<script>
const form = document.getElementById("myForm");

form.addEventListener("submit", function(event) {
  console.log(event);
  event.preventDefault();
});
</script>
```

You’ll see:

```
SubmitEvent { type: 'submit', target: form#myForm, ... }
```

---

# 🔥 5️⃣ Mouse Move Event (See Live Coordinates)

```html
<div style="height:200px; background:lightgray;" id="box">
  Move mouse here
</div>

<script>
const box = document.getElementById("box");

box.addEventListener("mousemove", function(event) {
  console.log("X:", event.clientX, "Y:", event.clientY);
});
</script>
```

Now move mouse → You’ll see live coordinates 🔥

---

# 🔥 What Actually Is `event`?

It is an object created automatically by browser.

Internally something like:

```javascript
{
  type: "click",
  target: <button>,
  currentTarget: <button>,
  timeStamp: 123456,
  clientX: 200,
  clientY: 150,
  ...
}
```
