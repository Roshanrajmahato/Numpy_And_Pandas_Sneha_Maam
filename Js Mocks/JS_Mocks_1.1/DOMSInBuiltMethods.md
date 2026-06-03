
# 14. Perfect Interview Definition

> JavaScript accesses HTML elements using DOM methods like getElementById and querySelector, and manipulates them using properties such as innerHTML, innerText, style, classList, and attribute methods to create dynamic webpages.

---

# 1. Introduction

👉 JavaScript interacts with HTML through the **DOM (Document Object Model)**.

Using DOM we can:

* Access elements
* Change content
* Change style
* Add/remove elements
* Handle events

---

# 2. Accessing HTML Elements

## A. By ID

```js
let el = document.getElementById("demo");
```

* Returns single element
* Fastest method

---

## B. By Class

```js
let el = document.getElementsByClassName("box");
```

* Returns HTMLCollection (array-like)

---

## C. By Tag

```js
let p = document.getElementsByTagName("p");
```

---

## D. querySelector (Most Used)

```js
let el = document.querySelector(".box");
```

👉 First matching element

---

## E. querySelectorAll

```js
let el = document.querySelectorAll(".box");
```

👉 Returns NodeList

---

# 3. Manipulating Content

## A. innerHTML

```js
el.innerHTML = "<b>Hello</b>";
```

* Can insert HTML tags

---

## B. innerText

```js
el.innerText = "Hello";
```

* Only visible text

---

## C. textContent

```js
el.textContent = "Hello";
```

* Raw text (faster)

---

# 4. Manipulating Style

```js
el.style.color = "red";
el.style.fontSize = "20px";
```

### Add Class

```js
el.classList.add("active");
el.classList.remove("box");
el.classList.toggle("show");
```

---

# 5. Manipulating Attributes

```js
el.setAttribute("title","hello");

el.getAttribute("id");

el.removeAttribute("class");
```

---

# 6. Creating Elements

```js
let div = document.createElement("div");

div.innerText = "New Div";

document.body.appendChild(div);
```

---

## Insert at Specific Position

```js
parent.appendChild(div);

parent.prepend(div);

parent.before(div);

parent.after(div);
```

---

# 7. Removing Elements

```js
el.remove();
```

---

# 8. Event Handling

```js
btn.addEventListener("click", function(){
   el.innerText="Clicked";
});
```

---

# 9. Real Example

```html
<p id="p1">Hello</p>

<button id="btn">Change</button>

<script>
let p = document.getElementById("p1");
let btn = document.getElementById("btn");

btn.addEventListener("click", ()=>{
   p.innerText="Roshan";
   p.style.color="red";
});
</script>
```

---

# 10. Difference Concepts

## HTMLCollection vs NodeList

| HTMLCollection | NodeList |
| -------------- | -------- |
| Live           | Static   |
| No forEach     | forEach  |

---

## innerHTML vs innerText

| innerHTML   | innerText  |
| ----------- | ---------- |
| Parses tags | plain text |

---

# 11. Best Practices

* Use querySelector
* Avoid innerHTML for security
* Use classList
* Use event listeners

---

# 12. Interview Questions

### Q1. How to access element?

* getElementById
* querySelector

---

### Q2. Change content?

* innerHTML
* innerText

---

### Q3. Change CSS?

```js
el.style.color
```

---

### Q4. Create element?

```js
createElement + appendChild
```

---

### Q5. Difference innerHTML vs textContent?

* innerHTML → HTML
* textContent → text only

---

# 13. Output Questions

### 1️⃣

```js
el.innerHTML="<b>Hi</b>";
```

👉 bold Hi

---

### 2️⃣

```js
el.innerText="<b>Hi</b>";
```

👉 shows <b>Hi</b>

---

### 3️⃣

```js
querySelector(".a")
```

👉 first match

---

If you want Roshan, I can give:

👉 Mini project (theme changer)
👉 Form validation
👉 Todo app DOM

Tell me 👍
