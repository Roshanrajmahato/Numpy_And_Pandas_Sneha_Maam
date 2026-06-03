# 14. Perfect Interview Definition

> Content can be hidden or shown in JavaScript using DOM manipulation like style.display, style.visibility, or classList methods. The best practice is using classList.toggle to maintain separation of concerns between CSS and JavaScript.

---

# 1. Introduction

👉 Showing and hiding content is one of the most common DOM manipulations.

Used in:

* Toggle menus
* Password show/hide
* Read more
* Tabs
* Modals

---

# 2. Ways to Hide/Show in JavaScript

### 1. Using style.display

### 2. Using style.visibility

### 3. Using classList

### 4. Using toggle()

---

# 3. Method 1 – style.display (Most Used)

## Example

```html
<p id="p">Hello World</p>

<button onclick="hide()">Hide</button>
<button onclick="show()">Show</button>

<script>
function hide(){
 document.getElementById("p").style.display="none";
}

function show(){
 document.getElementById("p").style.display="block";
}
</script>
```

👉 display:none → element removed from layout

---

# 4. Method 2 – visibility

```js
el.style.visibility="hidden";
el.style.visibility="visible";
```

👉 Space remains reserved

---

# 5. Method 3 – Using classList (Best Practice)

```html
<style>
.hide{
 display:none;
}
</style>

<p id="p">Hi</p>

<script>
let p=document.getElementById("p");

p.classList.add("hide");
p.classList.remove("hide");
</script>
```

👉 Separation of CSS + JS

---

# 6. Toggle Method

```js
p.classList.toggle("hide");
```

---

# 7. Single Button Toggle Example

```html
<p id="p">Hello</p>
<button onclick="test()">Toggle</button>

<script>
function test(){

 let p=document.getElementById("p");

 if(p.style.display=="none")
   p.style.display="block";
 else
   p.style.display="none";

}
</script>
```

---

# 8. Using querySelector

```js
document.querySelector("#p").style.display="none";
```

---

# 9. Difference display vs visibility

| display:none          | visibility:hidden |
| --------------------- | ----------------- |
| No space              | Space remains     |
| Removed from DOM flow | Only hidden       |

---

# 10. Real Use Case – Password

```js
if(input.type=="password")
 input.type="text";
else
 input.type="password";
```

---

# 11. Interview Questions

### Q1. How hide element?

* display:none
* visibility:hidden
* classList

---

### Q2. Best way?

👉 classList toggle

---

### Q3. Difference display vs visibility?

* display remove layout
* visibility keep space

---

### Q4. Toggle function?

```js
classList.toggle()
```

---

# 12. Output Questions

### 1️⃣

```js
style.display="none"
```

👉 element gone

---

### 2️⃣

```js
visibility="hidden"
```

👉 space remains

---

# 13. Best Practices

* Use classList
* Avoid inline style
* Use toggle
* Keep CSS separate

---

