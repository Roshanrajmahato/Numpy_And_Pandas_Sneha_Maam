# 🔥 1️⃣ Method 1: Inline Event Handling (Inside HTML)

### ✅ Uses → Named Function (Required because HTML calls by name)

### 📌 Example 1 – Mouse Event (onclick)

```html
<h1 onclick="changeText(event)">Click Me</h1>

<script>
function changeText(event) {
   event.target.innerHTML = "You clicked me!";
}
</script>
```

### 🔍 Why Named Function?

Because HTML needs a function name to call.

---

### 📌 Example 2 – Keyboard Event (onkeydown)

```html
<input type="text" onkeydown="showKey(event)" placeholder="Press any key">

<script>
function showKey(event) {
   console.log("Key pressed: " + event.key);
}
</script>
```

---

# 🔥 2️⃣ Method 2: addEventListener() (Most Recommended ✅)

✔ Multiple events allowed
✔ Cleaner separation of HTML & JS
✔ Best practice in real projects

---

## 🖱 Mouse Event – dblclick (Arrow Function)

```html
<h2 id="head">Double Click Me</h2>

<script>
const headEle = document.getElementById("head");

headEle.addEventListener("dblclick", () => {
   headEle.textContent = "You double clicked!";
});
</script>
```

---

## ⌨ Keyboard Event – keyup (Anonymous Function)

```html
<input type="text" id="inputBox" placeholder="Type something">

<script>
const input = document.getElementById("inputBox");

input.addEventListener("keyup", function(event) {
   console.log("You typed: " + event.target.value);
});
</script>
```

---

## 📄 Form Event – submit (Named Function)

```html
<form id="myForm">
   <input type="text" required>
   <button type="submit">Submit</button>
</form>

<script>
const form = document.getElementById("myForm");

form.addEventListener("submit", handleSubmit);

function handleSubmit(event) {
   event.preventDefault();
   alert("Form Submitted!");
}
</script>
```

---

# 🔥 3️⃣ Method 3: Property Method

Assign function directly to element property.

---

## 🖱 Mouse Event – onclick (Arrow Function)

```html
<button id="btn">Click Once</button>

<script>
const btn = document.getElementById("btn");

btn.onclick = () => {
   btn.innerHTML = "Clicked!";
};
</script>
```

---

## 🎯 Focus Event – onfocus & onblur (Anonymous Function)

```html
<input type="text" id="focusInput" placeholder="Focus here">

<script>
const focusInput = document.getElementById("focusInput");

focusInput.onfocus = function() {
   focusInput.style.backgroundColor = "lightgreen";
};

focusInput.onblur = function() {
   focusInput.style.backgroundColor = "white";
};
</script>
```

---

# 🔥 4️⃣ Window Events

## 🖥 onload (Named Function)

```html
<script>
window.onload = pageLoaded;

function pageLoaded() {
   console.log("Page Fully Loaded");
}
</script>
```

---

## 🖥 onscroll (Arrow Function)

```html
<script>
window.onscroll = () => {
   console.log("Scrolling...");
};
</script>
```

## Real-World: Dark Mode Toggle Button

```html
<style>
.dark {
  background-color: black;
  color: white;
}
</style>
<button id="toggleBtn">Toggle Dark Mode</button>

<script>
const btn = document.getElementById("toggleBtn");

btn.onclick = () => {
  document.body.classList.toggle("dark");
};
</script>
```


