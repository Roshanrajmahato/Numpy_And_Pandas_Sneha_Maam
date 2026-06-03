
# 7. Perfect Interview Definition

> DOM methods differ based on selector type, return value, performance, and behavior. Methods like getElementById are fast but limited, while querySelector is flexible. HTMLCollection is live whereas NodeList is static. For content manipulation, innerHTML parses HTML while textContent handles plain text. Modern development prefers querySelector, classList, and append over older methods.

---

# 1. What are DOM Methods?

👉 DOM methods are built-in JavaScript functions used to:

* Select HTML elements
* Modify content
* Change style
* Add/remove elements
* Handle attributes & events

Different methods behave differently in terms of:

* Return type
* Speed
* Live vs Static
* Single vs Multiple elements

---

# 2. Most Important DOM Method Differences

---

## A. getElementById  vs querySelector

| Feature | getElementById | querySelector    |
| ------- | -------------- | ---------------- |
| Selects | Only by ID     | Any CSS selector |
| Returns | Single element | First match      |
| Speed   | Faster         | Slight slower    |
| Syntax  | Simple         | CSS style        |

### Example

```js
document.getElementById("box");
document.querySelector("#box");
```

👉 Interview Point

* getElementById is faster
* querySelector is flexible

---

## B. querySelector  vs querySelectorAll

| querySelector  | querySelectorAll |
| -------------- | ---------------- |
| First element  | All elements     |
| Single Node    | NodeList         |
| No loop needed | Loop needed      |

```js
let a = document.querySelector(".box");
let b = document.querySelectorAll(".box");
```

---

## C. HTMLCollection vs NodeList

| HTMLCollection                     | NodeList                     |
| ---------------------------------- | ---------------------------- |
| Live                               | Static                       |
| No forEach                         | forEach allowed              |
| Returned by getElementsByClassName | Returned by querySelectorAll |

```js
let a = document.getElementsByClassName("box"); // HTMLCollection
let b = document.querySelectorAll(".box");      // NodeList
```

👉 Interview Trap
HTMLCollection auto updates
NodeList does not

---

## D. innerHTML vs innerText vs textContent

| innerHTML     | innerText    | textContent |
| ------------- | ------------ | ----------- |
| Parses HTML   | Visible text | Raw text    |
| Slower        | Medium       | Fast        |
| Security risk | Safe         | Safe        |

```js
el.innerHTML="<b>Hi</b>";
el.innerText="<b>Hi</b>";
el.textContent="<b>Hi</b>";
```

Output

* innerHTML → bold Hi
* innerText → <b>Hi</b>

---

## E. appendChild vs append

| appendChild  | append      |
| ------------ | ----------- |
| Only Node    | Node + Text |
| Single       | Multiple    |
| Returns node | void        |

```js
parent.appendChild(div);
parent.append(div,"hello");
```

---

## F. remove vs removeChild

| remove | removeChild  |
| ------ | ------------ |
| Direct | Needs parent |
| Easy   | Old way      |

```js
el.remove();

parent.removeChild(el);
```

---

## G. setAttribute vs classList

| setAttribute | classList  |
| ------------ | ---------- |
| Overwrites   | Add/remove |
| Old          | Modern     |

```js
el.setAttribute("class","a");

el.classList.add("a");
```

---

# 3. Performance Differences

1. getElementById → fastest
2. querySelector → flexible
3. innerHTML → slow
4. textContent → fast

---

# 4. Real Example

```html
<div id="box" class="a">Hello</div>

<script>
let x = document.getElementById("box");
x.innerText="Hi";

x.classList.add("b");
</script>
```

---

# 5. Interview Questions

### Q1. querySelector vs getElementById?

* querySelector → CSS selector
* getElementById → only ID + fast

---

### Q2. HTMLCollection vs NodeList?

* Live vs Static
* forEach only in NodeList

---

### Q3. innerHTML vs textContent?

* HTML parse vs plain text

---

### Q4. append vs appendChild?

* append multiple
* appendChild single

---

### Q5. Best method to add class?

👉 classList (not setAttribute)

---

# 6. Output Based Questions

### 1️⃣

```js
innerHTML="<b>A</b>"
```

👉 bold A

---

### 2️⃣

```js
innerText="<b>A</b>"
```

👉 shows <b>A</b>

---

### 3️⃣

```js
getElementsByClassName
```

👉 HTMLCollection

---

## Final Interview Tips

* Prefer querySelector
* Avoid innerHTML
* Use classList
* Use addEventListener

---

If you want Roshan, I can give:

👉 MCQ from this topic
👉 Viva questions
👉 10 output predictions

Tell me 👍
