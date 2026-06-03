# 🌐 DOM Selectors (Element Selectors) — Complete Guide

## 🔷 What is DOM Selector?

**DOM Selector** is used to **select HTML elements** using JavaScript so we can:

* Change text ✏️
* Change style 🎨
* Add events 🖱️
* Modify HTML dynamically 🔄

Example:

```html
<h1 id="title">Hello</h1>
```

```javascript
const ele = document.getElementById("title");
ele.innerHTML = "Welcome";
```

---

# 📌 Types of DOM Selectors

There are **5 main DOM selectors** you must know:

1. `getElementById()`
2. `getElementsByClassName()`
3. `getElementsByTagName()`
4. `querySelector()`
5. `querySelectorAll()`

---

# 1️⃣ getElementById()

## 🔹 Definition

Selects element using **id**.

## 🔹 Syntax

```javascript
document.getElementById("id_name");
```

## 🔹 Example

```html
<h1 id="heading">Hello World</h1>

<script>
const element = document.getElementById("heading");

element.style.color = "red";
</script>
```

## 🔹 Returns

✅ **Single element**

## 🔹 Notes

* ID must be **unique**
* Very **fast**

---

# 2️⃣ getElementsByClassName()

## 🔹 Definition

Selects elements using **class name**.

## 🔹 Syntax

```javascript
document.getElementsByClassName("class_name");
```

## 🔹 Example

```html
<p class="text">One</p>
<p class="text">Two</p>

<script>
const elements = document.getElementsByClassName("text");

elements[0].style.color = "blue";
elements[1].style.color = "green";
</script>
```

## 🔹 Returns

✅ **HTMLCollection** (Array-like)

Access using:

```javascript
elements[0]
elements[1]
```

---

# 3️⃣ getElementsByTagName()

## 🔹 Definition

Selects elements using **tag name**.

## 🔹 Syntax

```javascript
document.getElementsByTagName("tag");
```

## 🔹 Example

```html
<p>Paragraph 1</p>
<p>Paragraph 2</p>

<script>
const elements = document.getElementsByTagName("p");

elements[0].style.color = "red";
</script>
```

## 🔹 Returns

✅ **HTMLCollection**

---

# 4️⃣ querySelector() ⭐ (Most Important)

## 🔹 Definition

Selects **first element** that matches **CSS selector**.

## 🔹 Syntax

```javascript
document.querySelector("selector");
```

---

## 🔹 Select by ID

```javascript
document.querySelector("#id");
```

Example:

```html
<h1 id="title">Hello</h1>

<script>
const element = document.querySelector("#title");
element.style.color = "red";
</script>
```

---

## 🔹 Select by Class

```javascript
document.querySelector(".class");
```

Example:

```html
<p class="text">Paragraph</p>

<script>
const element = document.querySelector(".text");
element.style.fontSize = "25px";
</script>
```

---

## 🔹 Select by Tag

```javascript
document.querySelector("p");
```

---

## 🔹 Select Nested Elements

```javascript
document.querySelector("div p");
```

Example:

```html
<div>
   <p>Hello</p>
</div>
```

Selects:

```javascript
document.querySelector("div p");
```

---

# 5️⃣ querySelectorAll()

## 🔹 Definition

Selects **all matching elements**.

## 🔹 Syntax

```javascript
document.querySelectorAll("selector");
```

## 🔹 Example

```html
<p class="item">One</p>
<p class="item">Two</p>

<script>
const elements = document.querySelectorAll(".item");

elements.forEach(function(el) {
    el.style.color = "green";
});
</script>
```

## 🔹 Returns

✅ **NodeList**

---

# 📌 HTMLCollection vs NodeList

Very important concept ⚠️

| Feature      | HTMLCollection      | NodeList         |
| ------------ | ------------------- | ---------------- |
| Returned by  | getElements methods | querySelectorAll |
| Live         | ✅ Yes               | ❌ No             |
| forEach()    | ❌ No                | ✅ Yes            |
| Index Access | ✅ Yes               | ✅ Yes            |

---

# 📌 Difference Between querySelector & querySelectorAll

| Feature           | querySelector | querySelectorAll |
| ----------------- | ------------- | ---------------- |
| Returns           | First element | All elements     |
| Type              | Element       | NodeList         |
| Multiple Elements | ❌ No          | ✅ Yes            |

---

# 📌 Selecting Multiple Ways (CSS Selectors)

These work inside `querySelector`.

## ID

```javascript
"#id"
```

## Class

```javascript
".class"
```

## Tag

```javascript
"p"
```

## Attribute

```javascript
"input[type='text']"
```

## Multiple Classes

```javascript
".box.red"
```

## Child Selector

```javascript
"div > p"
```

## Descendant Selector

```javascript
"div p"
```

---

# 📌 Looping Through Elements

## Using for loop

```javascript
const items = document.getElementsByClassName("item");

for (let i = 0; i < items.length; i++) {
    items[i].style.color = "blue";
}
```

---

## Using forEach (NodeList)

```javascript
const items = document.querySelectorAll(".item");

items.forEach(function(el) {
    el.style.color = "red";
});
```

---

# 📌 Changing Content

```javascript
element.innerHTML = "Hello";
element.textContent = "Hello";
```

Difference:

| innerHTML  | textContent     |
| ---------- | --------------- |
| Reads HTML | Reads text only |
| Slower     | Faster          |

---

# 📌 Changing Style

```javascript
element.style.color = "red";
element.style.backgroundColor = "yellow";
element.style.fontSize = "20px";
```

---

# 📌 Adding Classes

```javascript
element.classList.add("active");
element.classList.remove("active");
element.classList.toggle("active");
```

---

# 📌 Accessing Form Elements

```javascript
const input = document.querySelector("#name");

console.log(input.value);
```

---

# 📌 Selecting Parent, Child & Siblings

## Parent

```javascript
element.parentElement
```

## Children

```javascript
element.children
```

## First Child

```javascript
element.firstElementChild
```

## Last Child

```javascript
element.lastElementChild
```

## Next Element

```javascript
element.nextElementSibling
```

## Previous Element

```javascript
element.previousElementSibling
```

---

# 📌 Real Example (Mini Project)

```html
<!DOCTYPE html>
<html>
<body>

<h1 id="title">DOM Practice</h1>

<p class="text">Paragraph 1</p>
<p class="text">Paragraph 2</p>

<button id="btn">Click Me</button>

<script>

const title = document.getElementById("title");
const texts = document.querySelectorAll(".text");
const btn = document.querySelector("#btn");

btn.addEventListener("click", function() {

    title.style.color = "blue";

    texts.forEach(function(p) {
        p.style.backgroundColor = "yellow";
    });

});

</script>

</body>
</html>
```

---

# 📌 Most Important Selectors (Interview Focus) ⭐

Must remember:

* `getElementById()`
* `querySelector()`
* `querySelectorAll()`
* `classList`
* `children`
* `parentElement`

These are asked very often.

---

# 📌 Quick Revision Summary 🧠

| Method                 | Returns        | Use          |
| ---------------------- | -------------- | ------------ |
| getElementById         | Element        | ID           |
| getElementsByClassName | HTMLCollection | Class        |
| getElementsByTagName   | HTMLCollection | Tag          |
| querySelector          | First Element  | CSS selector |
| querySelectorAll       | NodeList       | All matches  |

---

# If you're learning DOM seriously

Next topics you should study:

1. **DOM Events**
2. **addEventListener()**
3. **Event Types (click, dblclick, mouseenter)**
4. **DOM Manipulation**
5. **Event Delegation**

I can also create:
✅ Practice Questions
✅ Interview Questions
✅ DOM Cheat Sheet
✅ DOM Mini Projects

Just tell me 👍
