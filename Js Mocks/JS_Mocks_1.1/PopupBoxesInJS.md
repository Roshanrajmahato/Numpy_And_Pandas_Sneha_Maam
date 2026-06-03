
# 14. Perfect Interview Definition

> Popup boxes are built-in JavaScript dialog windows (alert, confirm, prompt) used to display messages, get confirmation, or take user input. They are synchronous and block page execution until user responds.

---

# 1. What is Popup Box in JavaScript?

👉 **Popup boxes are built-in browser dialog windows used to interact with the user.**

They are part of the **Browser Object Model (BOM)** and are provided by the `window` object.

### Uses

* Show messages
* Take user input
* Get confirmation
* Debugging

---

# 2. Types of Popup Boxes

JavaScript provides **3 popup boxes**

1. alert()
2. confirm()
3. prompt()

---

# 3. alert() – Message Box

### Purpose

👉 Display a simple message to the user.

### Syntax

```js
alert("message");
```

### Example

```js
alert("Welcome Roshan");
```

### Features

* Only OK button
* No return value
* Stops execution until closed (blocking)

---

# 4. confirm() – Yes/No Box

### Purpose

👉 Get confirmation from user.

### Syntax

```js
confirm("message");
```

### Returns

* true → OK
* false → Cancel

### Example

```js
let result = confirm("Are you sure?");

if(result){
  alert("User clicked OK");
}else{
  alert("User clicked Cancel");
}
```

---

# 5. prompt() – Input Box

### Purpose

👉 Take input from user.

### Syntax

```js
prompt("message", "default");
```

### Returns

* String value
* null if cancel

### Example

```js
let name = prompt("Enter your name");

alert("Hello " + name);
```

---

# 6. Internal Working

* These are methods of `window` object
* Browser controlled
* Execution is paused (synchronous)
* Not customizable with CSS

---

# 7. Characteristics

* Modal dialogs
* Block page interaction
* Simple UI
* Not recommended for modern UX

---

# 8. Difference Between Them

| Feature | alert     | confirm    | prompt      |
| ------- | --------- | ---------- | ----------- |
| Buttons | OK        | OK/Cancel  | OK/Cancel   |
| Input   | No        | No         | Yes         |
| Return  | undefined | true/false | string/null |

---

# 9. Real Example

```js
function deleteData(){

 let c = confirm("Delete record?");

 if(c){
   alert("Deleted");
 }else{
   alert("Cancelled");
 }

}
```

---

# 10. Limitations

* Cannot style
* Browser dependent
* Blocks execution
* Poor UX
* Not async

👉 Modern apps use:

* custom modal
* sweetalert
* bootstrap modal

---

# 11. Edge Cases

## 1. User pressed Cancel in prompt

```js
let a = prompt("Enter");

console.log(a); // null
```

---

## 2. Empty input

```js
prompt("Enter"); // ""  (not null)
```

---

## 3. Type issue

```js
let age = prompt("age");
console.log(typeof age); // string
```

👉 Need parseInt()

---

# 12. Interview Questions

### Q1. What are popup boxes?

> Built-in dialog windows to interact with user.

---

### Q2. Types?

* alert
* confirm
* prompt

---

### Q3. Return values?

* alert → undefined
* confirm → boolean
* prompt → string/null

---

### Q4. Are they synchronous?

👉 Yes, block execution.

---

### Q5. Why not used in real projects?

* No styling
* bad UX
* blocking

---

# 13. Output Questions

### 1️⃣

```js
console.log(alert("hi"));
```

👉 undefined

---

### 2️⃣

```js
console.log(confirm("ok?"));
```

👉 true/false

---

### 3️⃣

```js
let a = prompt("age");
console.log(typeof a);
```

👉 string

---

# 15. Modern Alternative

Instead of popup:

* HTML modal
* SweetAlert
* Bootstrap dialog

---

If you want Roshan, I can give:

👉 Custom popup using HTML/CSS/JS
👉 SweetAlert example
👉 Form validation using prompt

Tell me 👍
