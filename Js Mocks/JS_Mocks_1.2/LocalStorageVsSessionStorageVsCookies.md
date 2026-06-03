# 💡 Interview One-Line Answer

> localStorage stores persistent data in the browser, sessionStorage stores data for one tab session, and cookies store small data that is automatically sent to the server with HTTP requests.

# ✅ 18. Difference Between `localStorage`, `sessionStorage`, and Cookies

All three are used to **store data in the browser**, but they behave differently.

---

# 🔹 1️⃣ localStorage

## 🔹 What is it?

`localStorage` stores data in the browser with **no expiration time**.

Data stays:

* Even after browser is closed
* Until manually deleted

---

## 🔹 Example

```javascript
localStorage.setItem("username", "Roshan");

const user = localStorage.getItem("username");
console.log(user); // Roshan

localStorage.removeItem("username");
localStorage.clear(); // removes all
```

---

## 🔹 Characteristics

* Storage limit: ~5MB
* Stored in browser
* Not sent to server automatically
* Persistent

---

# 🔹 2️⃣ sessionStorage

## 🔹 What is it?

`sessionStorage` stores data **only for one browser tab session**.

Data is deleted when:

* Tab is closed
* Browser is closed

---

## 🔹 Example

```javascript
sessionStorage.setItem("token", "abc123");

const token = sessionStorage.getItem("token");
console.log(token);
```

---

## 🔹 Characteristics

* Storage limit: ~5MB
* Only available in same tab
* Not shared between tabs
* Deleted after session ends

---

# 🔹 3️⃣ Cookies

## 🔹 What are Cookies?

Cookies are small pieces of data stored in the browser and **sent automatically to the server with every HTTP request**.

---

## 🔹 Example

```javascript
document.cookie = "username=Roshan; expires=Fri, 31 Dec 2026 12:00:00 UTC; path=/";
```

To read:

```javascript
console.log(document.cookie);
```

---

## 🔹 Characteristics

* Storage limit: ~4KB (very small)
* Sent to server automatically
* Can have expiration date
* Can be HttpOnly (secure)
* Used for authentication

---

# 🔥 Comparison Table (Very Important 🔥)

| Feature            | localStorage | sessionStorage    | Cookies                 |
| ------------------ | ------------ | ----------------- | ----------------------- |
| Expiry             | No expiry    | Until tab closed  | Custom expiry           |
| Storage Limit      | ~5MB         | ~5MB              | ~4KB                    |
| Sent to Server     | ❌ No         | ❌ No              | ✅ Yes                   |
| Accessible from JS | ✅ Yes        | ✅ Yes             | ✅ Yes (unless HttpOnly) |
| Use Case           | Preferences  | Temporary session | Authentication          |

---

# 🔥 Real Project Use Cases

## 🔹 localStorage

* Dark mode preference
* Language settings
* Remember user theme

```javascript
localStorage.setItem("theme", "dark");
```

---

## 🔹 sessionStorage

* Temporary form data
* Multi-step form data
* OTP verification step

---

## 🔹 Cookies

* JWT authentication
* Session ID
* Secure login

Backend example:

* Server sets `HttpOnly` cookie
* Browser sends it automatically

---

# 🔥 Security Difference (Important 🔥)

`localStorage`:

* Vulnerable to XSS

Cookies:

* Can be protected with:

  * `HttpOnly`
  * `Secure`
  * `SameSite`

So for authentication:
👉 Cookies are safer (if configured properly)

---

