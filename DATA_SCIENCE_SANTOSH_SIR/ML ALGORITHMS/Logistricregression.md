Great question.

In Logistic Regression, the **decision boundary** is calculated from the linear equation learned by the model.

---


# Interview Answer

> Logistic Regression calculates the decision boundary using the equation (w_1x_1 + w_2x_2 + b = 0). The weights are learned using gradient descent to minimize log loss. Points on one side of the boundary belong to one class, and points on the other side belong to the other class.

# Step 1: Linear Equation

Logistic Regression first computes:

z = w_1x_1 + w_2x_2 + b

Where:

* (x_1, x_2) = input features
* (w_1, w_2) = learned weights
* (b) = bias/intercept

---

# Step 2: Convert to Probability

Then sigmoid function is applied:

\sigma(z)=\frac{1}{1+e^{-z}}

This gives probability between 0 and 1.

---

# Step 3: Decision Boundary

The boundary occurs where probability is exactly:

```text id="xk4muu"
0.5
```

Because:

```text id="4i2q8l"
Probability > 0.5 → Class 1
Probability < 0.5 → Class 0
```

---

# Very Important Math

Sigmoid gives 0.5 when:

```text id="4mfkmb"
z = 0
```

So decision boundary is:

w_1x_1 + w_2x_2 + b = 0

THIS is the actual decision boundary.

---

# Example

Suppose model learned:

```text id="0b4tx4"
w1 = 2
w2 = -1
b = -3
```

Then boundary becomes:

2x_1 - x_2 - 3 = 0

Rearrange:

```text id="qzvnn4"
x2 = 2x1 - 3
```

This is a straight line.

---

# What Happens Around Boundary?

Suppose:

| Point      | Equation Result | Class |
| ---------- | --------------- | ----- |
| Above line | Positive        | 1     |
| Below line | Negative        | 0     |

Because:

* (z > 0) → sigmoid > 0.5
* (z < 0) → sigmoid < 0.5

---

# How Are Weights Found?

The model starts with random weights.

Example:

```text id="7z56tr"
w1 = 0.2
w2 = -0.1
```

Then it:

1. Predicts probabilities
2. Calculates error
3. Updates weights
4. Repeats many times

This optimization process is called:

Gradient Descent

---

# Goal of Gradient Descent

Find weights that minimize classification error.

The loss function used is:

-\left(y\log(\hat{y}) + (1-y)\log(1-\hat{y})\right)

called **log loss** or **binary cross-entropy**.

---

# Visual Understanding

The model keeps moving the line until classes separate as best as possible.

![Image](https://images.openai.com/static-rsc-4/bCJj0vqSgU5fHsHjl2793cSO2QxCEGNpCbgBhLwaJ9UDAADKN_yzX9jqIjDgoHbFwCJmlgewgMAPm7uAZ3YMLdYFRm5rj1-Fd194ONs4SGclVsxNLbfYvRtwN-gMOPUBc0Kln91jXfqOqJYoi_mSvcc0qwNF8C3y7JIzCCtLr8AyRNobep_rwiEwQoy3yJoM?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/hnBlG8ZIxh8Qk_rJmocYzvk1OCePVkqq0sbX2ZgHtLN8PLs1U4P8sVjpyxDBufbW6Zei38Fmtvbcaj6c-kucTohyfOdteZnL_uWLGNSxPWbsYFhME7pB9MU10r4-wjJXE_PQ3S1KO7ZhgxVIcnTPuPU-uVjHXc_frBhna8dUvkR2ZtzrzhKFjBcLbg1azweD?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/OJ_NvqcOxNocPWytVya9KRgi51cdKueubDz80o-_M7ETbJrlCOVttRUXerqjCdUrAz6s_Dai5AjUyDTKQ8S-6qhqypY6xWa7kKdWxn4wZPfxCSxkCNp6IyqjCuB01KvBxd-fBwJjAB3yOullGDSqBQmyGhwaSEHCXDYHPlG84AbdPBzOyadRdZ4S0KwYyQ5A?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/gNpsZZcbDbmnCKx7ruFo-KnjOZ7t7RNhNVtBTwienuJ3uTNlWcMLiZROrX4KRMmkcAt7oXPhoOjyHoFpfdYdlp6oqoxDFZjfFrrTDzTh0qDuC4Jbbmy3ixh1sl2onHZ2co1A7oklnw1F3IU44O9SyJfmI37iyHQCgvJdeoygPkST2sL4FS9A0Eh_iyfW1wQ6?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/u1oKQDMSWgZ9l1WcVZ7UI7eMoiK5psRbEiax89j1rOmWXm2k755HsN9RXFlg7wWcZM93oKaZ8D4uSQPiK8Z_QSTbADuFjy5nFwOA4gxKEbE4VKQ_1Fuy4dP9TW18bzv7i6nu2ZgUO3acsExr8htuaYRv5iyrnaQJ_3lC24QfKp074_MZMbv2nKVe3N2zvKc4?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/KhgkeoI69mpGFj27DwMKNuvUCoLnY6-U4ve5kwHrr7-uuvapRB-jrHdLZ_JEKHRSLdNkhjo_jSXQArYhMTPr2nSfOuiyUV-J0DF1hwX8ctEm8ia7U_5jFCrmFCY8BTfygjUSN1COHQuyQNOIrVjHHd6RSwouDCh4FPLzrDerab5bjruBMF_qZm5dbwMMJvWS?purpose=fullsize)

---

# Final Flow

```text id="1vbflc"
Input  Features
      ↓
Linear Equation
      ↓
Sigmoid Function
      ↓
Probability
      ↓
Threshold (0.5)
      ↓
Class Prediction
```

---
