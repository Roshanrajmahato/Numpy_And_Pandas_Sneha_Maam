
# 12. Perfect Interview Definition

> The `==` operator compares values after performing type coercion, while the `===` operator compares both value and data type without conversion. `===` is safer and recommended to avoid unexpected results.

---

# 1. Basic Meaning

## 👉 `==`  → Loose Equality

## 👉 `===` → Strict Equality

| Operator | Name            | Checks                               |
| -------- | --------------- | ------------------------------------ |
| `==`     | Loose equality  | Value only (type conversion allowed) |
| `===`    | Strict equality | Value + Type                         |

---

# 2. Main Difference

### `==` performs TYPE CONVERSION

### `===` does NOT perform TYPE CONVERSION

---

# 3. Examples

## A. Loose Equality (==)

```js
5 == "5"   // true
```

👉 JavaScript converts string "5" → number 5

---

## B. Strict Equality (===)

```js
5 === "5"  // false
```

👉 Type is different → no conversion

---

# 4. Detailed Comparison Table

| Expression         | Result |
| ------------------ | ------ |
| 0 == false         | true   |
| 0 === false        | false  |
| "" == false        | true   |
| "" === false       | false  |
| null == undefined  | true   |
| null === undefined | false  |
| "5" == 5           | true   |
| "5" === 5          | false  |

---

# 5. Internal Working

## How `==` Works

1. If types different
2. JavaScript converts types
3. Then compares values

### Example

```js
"10" == 10
```

Step:

* string → number
* 10 == 10 → true

---

## How `===` Works

1. First check type
2. If type not same → false
3. No conversion

---

# 6. Dangerous Parts of ==

```js
"" == 0        // true
false == 0     // true
null == 0      // false
undefined == 0 // false
```

👉 Confusing behavior → avoid in real projects

---

# 7. Special Cases

## null vs undefined

```js
null == undefined   // true
null === undefined  // false
```

---

## NaN Case

```js
NaN == NaN   // false
NaN === NaN  // false
```

👉 Use:

```js
Number.isNaN()
```

---

# 8. Best Practice

### Always use ===

✔ More safe
✔ Predictable
✔ No type coercion bug

---

# 9. Real Interview Examples

### 1️⃣

```js
console.log(1 == "1");
```

👉 true

---

### 2️⃣

```js
console.log(1 === "1");
```

👉 false

---

### 3️⃣

```js
console.log(false == "0");
```

👉 true

---

### 4️⃣

```js
console.log(false === "0");
```

👉 false

---

# 10. Interview Questions

### Q1. Difference between == and ===?

> == compares values after type conversion
> === compares value and type without conversion

---

### Q2. Which is better?

👉 Always ===

---

### Q3. null == undefined?

👉 true

---

### Q4. Why avoid == ?

* Unexpected conversion
* Bugs

---

# 11. Output Based Questions

### A.

```js
" " == 0
```

👉 true

---

### B.

```js
" " === 0
```

👉 false

---

### C.

```js
true == 1
```

👉 true

---
