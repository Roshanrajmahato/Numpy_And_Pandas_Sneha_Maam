To **hide the last 5 digits of a mobile number**, we usually replace them with `*` for privacy (masking).
I'll show **multiple ways**, explain the **logic**, and include **interview points**.

---

# ✅ Method 1 — Using `slice()` (Most Common)

## Code

```javascript
let mobile = "9876543210";

// Keep first digits and hide last 5 digits
let hidden = mobile.slice(0, -5) + "*****";

console.log(hidden); 
// Output: 98765*****
```

---

## 🔍 How It Works

```javascript
mobile.slice(0, -5)
```

Means:

* Start from index **0**
* Stop **before last 5 digits**

Example:

```text
Mobile: 9876543210
Keep:   98765
Hide:        43210 → *****
Result: 98765*****
```

---

# ✅ Method 2 — Dynamic Version (Works for Any Length)

## Code

```javascript
let mobile = "9876543210";

let hideCount = 5;

let visiblePart = mobile.slice(0, mobile.length - hideCount);
let hiddenPart = "*".repeat(hideCount);

let result = visiblePart + hiddenPart;

console.log(result);
// Output: 98765*****
```

---

## Why This is Better

* Works for any number length
* Hide digits dynamically

Very useful in **real applications**.

---

# ✅ Method 3 — Using `substring()`

## Code

```javascript
let mobile = "9876543210";

let result = mobile.substring(0, mobile.length - 5) + "*****";

console.log(result);
// Output: 98765*****
```

---

# ✅ Method 4 — Hide Middle Digits (Real-world Masking)

Often used in apps:

```text
987*****10
```

## Code

```javascript
let mobile = "9876543210";

let result =
    mobile.slice(0, 3) +
    "*****" +
    mobile.slice(-2);

console.log(result);
// Output: 987*****10
```

---

# 🎯 Interview Points

These are frequently asked.

## ⭐ What is `slice(0, -5)`?

Means:

```text
Take everything except last 5 characters
```

---

## ⭐ How to hide digits dynamically?

Use:

```javascript
"*".repeat(5)
```

---

## ⭐ Real-world Uses

Used in:

* OTP verification systems 🔐
* Banking apps 💳
* Login masking
* User privacy display

---

# ⚠️ Edge Case Handling (Important)

Check length before masking.

```javascript
let mobile = "98765";

if (mobile.length > 5) {
    let result =
        mobile.slice(0, -5) +
        "*".repeat(5);

    console.log(result);
} else {
    console.log("Invalid mobile number");
}
```

---

# 🚀 Bonus — Function Version (Best Practice)

```javascript
function hideLastDigits(mobile, hideCount = 5) {

    if (mobile.length <= hideCount) {
        return "Invalid Number";
    }

    return mobile.slice(0, -hideCount) +
           "*".repeat(hideCount);
}

console.log(hideLastDigits("9876543210"));
// Output: 98765*****
```

---

# 🧾 Summary

| Method           | Use Case        |
| ---------------- | --------------- |
| `slice()`        | Most used       |
| `substring()`    | Alternative     |
| `"*".repeat()`   | Dynamic masking |
| Function version | Real-world apps |

---

If you're practicing **JavaScript interview programs**, the next useful ones are:

* Hide first digits
* Hide middle digits
* Format mobile number (98765-43210)
* Mask email address
* Mask credit card number

I can provide those too if you want 👍
