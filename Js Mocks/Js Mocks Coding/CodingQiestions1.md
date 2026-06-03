
# ✅ 1. FACTORIAL NUMBER

## 👉 Theory

Factorial of a number **n** is the product of all positive integers from **1 to n**.

[
n! = n × (n-1) × (n-2) … × 1
]

### Examples

* 5! = 5×4×3×2×1 = **120**
* 0! = **1** (by definition)

---

## 👉 JavaScript Code – Iterative

```javascript
function factorial(n) {
    if (n < 0) return "Not defined for negative";

    let fact = 1;
    for (let i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

console.log(factorial(5));   // 120
```

---

## 👉 JavaScript Code – Recursive

```javascript
function factorialRec(n) {
    if (n === 0 || n === 1) return 1;
    return n * factorialRec(n - 1);
}

console.log(factorialRec(5));   // 120
```

---

## 🎯 Interview Points

* Time Complexity → **O(n)**
* Factorial grows very fast → risk of overflow.
* 0! = 1 is a favorite interview question.
* Recursive solution may cause stack overflow for large n.

---

# ✅ 2. STRONG NUMBER

## 👉 Theory

A number is **Strong** if:

👉 Sum of factorials of its digits = original number

### Example

145
1! + 4! + 5!
= 1 + 24 + 120
= **145** → Strong Number

---

## 👉 JavaScript Code

```javascript
function factorial(n) {
    let f = 1;
    for (let i = 1; i <= n; i++) {
        f *= i;
    }
    return f;
}

function isStrong(num) {
    let temp = num;
    let sum = 0;

    while (temp > 0) {
        let digit = temp % 10;
        sum += factorial(digit);
        temp = Math.floor(temp / 10);
    }

    return sum === num;
}

console.log(isStrong(145));   // true
console.log(isStrong(123));   // false
```

---

## 🎯 Interview Points

* Requires factorial of each digit.
* Very rare numbers: 1, 2, 145, 40585.
* Complexity → O(d × 10) where d = digits.

---

# ✅ 3. PERFECT NUMBER

## 👉 Theory

A number is **Perfect** if:

👉 Sum of its proper divisors = number itself

### Example – 6

Divisors → 1,2,3
1+2+3 = **6** → Perfect

---

## 👉 JavaScript Code

```javascript
function isPerfect(n) {
    let sum = 0;

    for (let i = 1; i <= n/2; i++) {
        if (n % i === 0) {
            sum += i;
        }
    }

    return sum === n;
}

console.log(isPerfect(6));   // true
console.log(isPerfect(28));  // true
console.log(isPerfect(10));  // false
```

---

## 🎯 Interview Points

* First few perfect numbers → 6, 28, 496, 8128
* Loop till n/2 optimization
* Complexity → O(n)

---

# ✅ 4. PRIME NUMBER

## 👉 Theory

A number divisible only by:

👉 1 and itself → PRIME

Examples → 2,3,5,7,11

---

## 👉 JavaScript Code – Optimized

```javascript
function isPrime(n) {
    if (n < 2) return false;

    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }

    return true;
}

console.log(isPrime(7));   // true
console.log(isPrime(10));  // false
```

---

## 🎯 Interview Points

* Best approach → loop till √n
* 2 is only even prime
* Complexity → **O(√n)**
* Ask about negative & 0,1 handling.

---

# ✅ 5. PALINDROME NUMBER

## 👉 Theory

A number/string that reads:

👉 Same from left → right
👉 Same from right → left

Examples → 121, 1331, “madam”

---

## 👉 JavaScript Code – Number

```javascript
function isPalindrome(num) {
    let original = num;
    let rev = 0;

    while (num > 0) {
        let digit = num % 10;
        rev = rev * 10 + digit;
        num = Math.floor(num / 10);
    }

    return rev === original;
}

console.log(isPalindrome(121));   // true
console.log(isPalindrome(123));   // false
```

---

## 👉 String Version

```javascript
function isPalindromeStr(str) {
    return str === str.split("").reverse().join("");
}

console.log(isPalindromeStr("madam")); // true
```

---

## 🎯 Interview Points

* Can be solved without converting to string.
* Case sensitivity matters.
* Space & special character handling may be asked.

---

# 🚀 MOST IMPORTANT INTERVIEW QUESTIONS

### 1. Difference Questions

| Concept    | Based On            |
| ---------- | ------------------- |
| Prime      | Divisibility        |
| Perfect    | Sum of divisors     |
| Strong     | Factorial of digits |
| Palindrome | Reverse equality    |
| Factorial  | Product series      |

---

### 2. Favorite Tricky Questions

👉 Is 1 prime?
→ ❌ No

👉 0! value?
→ ✅ 1

👉 2 is prime?
→ ✅ Yes (only even prime)

👉 145 is?
→ ✅ Strong

👉 6 is?
→ ✅ Perfect

---

### 3. Edge Cases to Handle

* Negative numbers
* 0 and 1
* Large number overflow
* String vs number palindrome
* Performance optimization

---

# 💯 Final Summary

| Program    | Main Logic                   |
| ---------- | ---------------------------- |
| Factorial  | Multiply 1 to n              |
| Strong     | Sum of factorial of digits   |
| Perfect    | Sum of divisors              |
| Prime      | Divisible by only 1 & itself |
| Palindrome | Reverse equals original      |

---

If you want I can also give:

* ✅ All programs in ONE MENU DRIVEN JS program
* ✅ HTML + JS UI for these checks
* ✅ MCQs & viva questions for exam

Just tell me 👍
