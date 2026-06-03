
# 14. Perfect Interview Definition

> DOM is an object-oriented representation of the HTML document where every element becomes a node. JavaScript uses DOM methods like getElementById, querySelector, createElement, and addEventListener to dynamically manipulate content, style, and structure of the webpage.

---

---

# 1. What is DOM?

👉 **DOM = Document Object Model**

> DOM is a programming interface that represents the HTML document as a tree of objects so that JavaScript can access, modify, and manipulate the webpage dynamically.

### Simple Meaning

HTML → Converted into Objects
JavaScript → Can read/change those objects

---

# 2. DOM Structure

Example HTML:

```html
<html>
 <body>
   <h1>Hello</h1>
   <p>Hi</p>
 </body>
</html>
```

👉 Browser converts this into a **DOM Tree**

* document

  * html

    * body

      * h1
      * p

Each element → Node/Object

---

# 3. Why DOM is Needed?

* Change HTML content
* Change CSS
* Handle events
* Create elements
* Build dynamic websites

---

# 4. DOM Methods (Most Important)

DOM methods are used to:

1. Select elements
2. Modify elements
3. Create/delete elements
4. Handle attributes
5. Event handling

---

## A. Selecting Elements

### 1. getElementById()

```js
let a = document.getElementById("demo");
```

👉 Returns single element

---

### 2. getElementsByClassName()

```js
document.getElementsByClassName("box");
```

👉 Returns HTMLCollection

---

### 3. getElementsByTagName()

```js
document.getElementsByTagName("p");
```

---

### 4. querySelector()

```js
document.querySelector(".box");
```

👉 First match

---

### 5. querySelectorAll()

```js
document.querySelectorAll(".box");
```

👉 NodeList

---

# 5. Changing Content

### innerHTML

```js
el.innerHTML = "Hello";
```

### innerText

```js
el.innerText = "Hi";
```

### textContent

```js
el.textContent = "Hi";
```

👉 Difference:

* innerHTML → parses HTML
* innerText → visible text
* textContent → raw text

---

# 6. Changing Style

```js
el.style.color = "red";
el.style.background = "yellow";
```

---

# 7. Attributes Methods

### getAttribute()

```js
el.getAttribute("id");
```

### setAttribute()

```js
el.setAttribute("class","box");
```

### removeAttribute()

```js
el.removeAttribute("title");
```

---

# 8. Creating Elements

```js
let div = document.createElement("div");

div.innerText = "Hello";

document.body.appendChild(div);
```

---

### remove element

```js
el.remove();
```

---

# 9. Event Handling

```js
btn.addEventListener("click", function(){
  alert("clicked");
});
```

---

# 10. DOM Properties

* parentNode
* children
* firstChild
* lastChild
* nextElementSibling
* previousElementSibling

---

# 11. Real Example

```html
<p id="p1">Hello</p>
<button onclick="change()">Click</button>

<script>
function change(){
 document.getElementById("p1").innerText="Changed";
}
</script>
```

---

# 12. Interview Questions

### Q1. What is DOM?

> DOM is object representation of HTML that allows JS to manipulate page.

---

### Q2. Difference HTMLCollection vs NodeList?

| HTMLCollection | NodeList          |
| -------------- | ----------------- |
| Live           | Static            |
| No forEach     | forEach available |

---

### Q3. innerHTML vs innerText?

* innerHTML → reads tags
* innerText → only text

---

### Q4. querySelector vs getElementById?

* querySelector → CSS selector
* getElementById → faster

---

### Q5. createElement use?

👉 To add dynamic elements.

---

# 13. Output Questions

### 1️⃣

```js
document.querySelector("#a")
```

👉 first element with id a

---

### 2️⃣

```js
el.innerHTML="<b>hi</b>"
```

👉 bold hi

---

### 3️⃣

```js
el.innerText="<b>hi</b>"
```

👉 shows <b>hi</b>

---

If you want Roshan, I can give:

👉 DOM traversal diagram
👉 mini project (todo list)
👉 event delegation concept

Tell me 👍
