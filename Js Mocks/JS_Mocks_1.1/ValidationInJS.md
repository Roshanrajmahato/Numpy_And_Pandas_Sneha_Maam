
# 14. Perfect Interview Definition

> Validation in JavaScript is the process of verifying user input on the client side to ensure data correctness, format, and completeness before submission, using conditions, regular expressions, and DOM methods.

---

# 1. What is Validation?

👉 **Validation is the process of checking user input to ensure it is correct, complete, and in proper format before sending to server.**

### Purpose

* Prevent wrong data
* Improve security
* Better user experience
* Reduce server load

---

# 2. Types of Validation

## A. Client Side Validation

* Done in browser using JavaScript
* Fast
* Reduces server requests

## B. Server Side Validation

* Done on server
* More secure
* Mandatory even if client validation exists

---

# 3. What Can We Validate?

* Empty fields
* Email format
* Phone number
* Password strength
* Length
* Number range

---

# 4. Basic Validation Example

```html
<form onsubmit="return check()">

<input id="name">
<button>Submit</button>

</form>

<script>
function check(){

 let n = document.getElementById("name").value;

 if(n == ""){
   alert("Name required");
   return false;
 }

 return true;
}
</script>
```

👉 return false → form stop

---

# 5. Email Validation (Regex)

```js
let email = document.getElementById("e").value;

let pattern = /^[a-zA-Z0-9._]+@[a-z]+\.[a-z]{2,}$/;

if(!pattern.test(email)){
 alert("Invalid Email");
}
```

---

# 6. Number Validation

```js
let age = document.getElementById("age").value;

if(isNaN(age)){
 alert("Only number");
}
```

---

# 7. Password Validation

```js
if(pass.length < 6){
 alert("Min 6 char");
}
```

---

# 8. Real Example – Complete Form

```html
<form onsubmit="return validate()">

Name: <input id="n"><br>
Email: <input id="e"><br>

<button>Submit</button>

</form>

<script>
function validate(){

 let n = n.value;
 let e = e.value;

 if(n=="" || e==""){
   alert("All required");
   return false;
 }

 return true;
}
</script>
```

---

# 9. HTML5 + JS Validation

* required
* minlength
* pattern
* type="email"

```html
<input required minlength="3">
```

---

# 10. Prevent Default Method

```js
form.addEventListener("submit", e=>{
 e.preventDefault();
});
```

---

# 11. Interview Questions

### Q1. What is validation?

> Checking user input before processing.

---

### Q2. Types?

* Client
* Server

---

### Q3. Why needed?

* Security
* Correct data

---

### Q4. How stop form?

👉 return false / preventDefault

---

### Q5. Email validation?

👉 regex

---

# 12. Output Questions

### 1️⃣

```js
"" == false
```

👉 true → dangerous

---

### 2️⃣

```js
isNaN("10")
```

👉 false

---

# 13. Best Practices

* Both client + server
* Use regex
* Show proper message
* Don’t rely only on JS

---

# 15. Important Lines to Say

* Client validation for UX
* Server for security
* Regex powerful
* preventDefault

---

If you want Roshan, I can give:

👉 Full form project
👉 Password strength meter
👉 MCQ set

Tell me 👍
