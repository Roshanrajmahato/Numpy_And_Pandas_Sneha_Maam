Got it 👍
You want **explanation + proper JavaScript code** for each program so that the output shown after `#` is achieved.

I will rewrite each program in a clean way and explain:

---

# ✅ 1. Removing Falsy Values from Array

### Code

```javascript
let arr = [false, null, undefined, 10, 'hello'];

let result = arr.filter(Boolean);

console.log(result);   // [10, 'hello']
```

### Explanation

* `Boolean` inside filter automatically removes:

  * false
  * null
  * undefined
  * 0
  * NaN
  * ""

👉 Only truthy values remain → `[10, 'hello']`

---

# ✅ 2. Getting Unique Values from Array

### Code

```javascript
let unique = [...new Set([1,3,4,5,3,3])];

console.log(unique);   // [1, 3, 4, 5]
```

### Explanation

* `Set` stores only unique values.
* Spread operator `...` converts Set back to array.

---

# ✅ 3. Making Array Empty

### Code

```javascript
let arrEle = ['hello','hi','Bye'];

arrEle.length = 0;

console.log(arrEle);   // []
```

### Explanation

* Setting `length = 0` removes all elements.
* Original reference is also cleared (best method).

---

# ✅ 4. Rounding Number to Certain Decimal

### Code

```javascript
let num = 10.253647896544;

console.log(num.toFixed(3));   // 10.254
```

### Explanation

* `toFixed(3)` → 3 digits after decimal
* Also performs rounding.

---

# ✅ 5. Converting Array into Object

### Code

```javascript
let student = ['xyz','BE',2024,'CS'];

let stdObject = {...student};

console.log(stdObject);
// { '0': 'xyz', '1': 'BE', '2': 2024, '3': 'CS' }
```

### Explanation

* Spread operator converts array index → object keys.

---

# ✅ 6. Creating Array with Same Data

### Code

```javascript
let newArray = new Array(5).fill('Hi');

console.log(newArray);
// [ 'Hi', 'Hi', 'Hi', 'Hi', 'Hi' ]
```

### Explanation

* `new Array(5)` → creates 5 empty slots
* `.fill('Hi')` → fills all positions.

---

# 🔥 FINAL COMBINED PROGRAM

```javascript
// 1. Remove falsy values
let arr = [false, null, undefined, 10, 'hello'];
console.log(arr.filter(Boolean)); 
// [10, 'hello']


// 2. Unique values
console.log([...new Set([1,3,4,5,3,3])]);
// [1, 3, 4, 5]


// 3. Empty array
let arrEle = ['hello','hi','Bye'];
arrEle.length = 0;
console.log(arrEle);
// []


// 4. Round decimal
let num = 10.253647896544;
console.log(num.toFixed(3));
// 10.254


// 5. Array → Object
let student = ['xyz','BE',2024,'CS'];
let stdObject = {...student};
console.log(stdObject);
// { '0': 'xyz', '1': 'BE', '2': 2024, '3': 'CS' }


// 6. Same data array
let newArray = new Array(5).fill('Hi');
console.log(newArray);
// ['Hi','Hi','Hi','Hi','Hi']
```

---

## 🎯 Interview Points

* `filter(Boolean)` → best way to remove falsy
* `Set` → removes duplicates
* `length = 0` → fastest way to empty array
* `toFixed()` → returns STRING
* Spread `{...arr}` → index becomes key
* `fill()` → initialize array

---

If you want I can convert this into:

👉 Viva questions
👉 MCQs
👉 Output prediction questions
👉 Tricky interview questions

Tell me your exam type 👍
