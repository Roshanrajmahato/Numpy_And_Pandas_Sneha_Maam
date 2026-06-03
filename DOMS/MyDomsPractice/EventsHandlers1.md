# 📘 What is Event Handling in JavaScript?

## 🔹 Definition

**Event Handling** is the process of detecting user actions (events) and responding to them using JavaScript functions.

An **event** is something that happens in the browser.


## 🖱️ Mouse Events

Used when working with mouse actions.

* `click` → Single click
* `dblclick` → Double click
* `mousedown` → Mouse button pressed
* `mouseup` → Mouse button released
* `mouseenter` → Mouse enters element
* `mouseleave` → Mouse leaves element
* `mouseover` → Mouse moves over element
* `mouseout` → Mouse moves out
* `mousemove` → Mouse moves
* `contextmenu` → Right click

Example:

```javascript
btn.addEventListener("click", function() {
   console.log("Button Clicked");
});
```

---

## ⌨️ Keyboard Events

Used when keyboard keys are pressed.

* `keydown` → Key pressed down
* `keyup` → Key released
* `keypress` → Key pressed (older, mostly deprecated)

Example:

```javascript
document.addEventListener("keydown", function() {
   console.log("Key Pressed");
});
```

---

## 📝 Form Events

Used with form elements like input, select, textarea.

* `submit` → Form submitted
* `change` → Value changed
* `input` → Input value changed
* `focus` → Element focused
* `blur` → Element lost focus
* `reset` → Form reset
* `select` → Text selected

Example:

```javascript
form.addEventListener("submit", function() {
   console.log("Form Submitted");
});
```

---

## 📄 Window Events

Used for browser window actions.

* `load` → Page fully loaded
* `DOMContentLoaded` → HTML loaded
* `resize` → Window resized
* `scroll` → Page scrolled
* `unload` → Page closed
* `beforeunload` → Before leaving page

Example:

```javascript
window.addEventListener("load", function() {
   console.log("Page Loaded");
});
```

✅ **Event Handler**

---

# 🧠 Real-Life Example of Event Handling

Imagine:

🏠 **Doorbell System**

* You press the **doorbell button** → Event
* Bell rings → Event Handler
* Person opens door → Response

In JavaScript:

* User clicks button → Event
* JavaScript function runs → Event Handler
* Page updates → Response

### Example 1:

```html
<button onclick="ringBell()">Press Bell</button>

<script>
function ringBell() {
   alert("Someone is at the door!");
}
</script>
```

Here:

* Click → Event
* `ringBell()` → Event Handler

### Example 2 : 

```html
<h2 onmouseenter="changeText()">
Hover Here
</h2>

<script>
function changeText() {
   console.log("Mouse Entered");
}
</script>
```

### Example 3 :

```html
<button onclick="showMessage()">
Click Me
</button>

<script>
function showMessage() {
   alert("Button Clicked");
}
</script>
```
### Example 4 :

```html
<input onkeydown="keyPressed(event)" placeholder="Type something">

<script>
function keyPressed(event) {
   console.log(event.key);
}
</script>
```
### Example 5 :

```html
<button onclick="runArrow()">
Run Arrow
</button>

<script>
const runArrow = () => {
   console.log("Arrow Function Called");
};
</script>
```
---

# 🔹 3 Methods of Event Handling

1️⃣ Inline Event Handling
2️⃣ addEventListener()
3️⃣ Property Method

## ✅ Example 1 —  Named Function in addEventListener()

```html
<script>
const btn = document.getElementById("btn1");

btn.addEventListener("click", showClick );

function showClick() {
   console.log("Clicked");
}
</script>
```

---

## ✅ Example 2 — Anonymous Function in addEventListener()

```html
<script>
btn.addEventListener( "dblclick", function() {
      console.log("Double Clicked");
   }
);
</script>
```

---

## ✅ Example 3 — Arrow Function in addEventListener()

```html
<script>
btn.addEventListener( "mouseenter",() => {
      console.log("Mouse Entered");
   }
);
</script>
```
