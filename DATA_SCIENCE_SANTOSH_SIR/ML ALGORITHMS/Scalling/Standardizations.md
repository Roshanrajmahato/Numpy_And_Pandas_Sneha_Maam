# **Standardization (Z-Score Scaling)**

## **Interview-Ready Answer**

**Standardization** is a feature scaling technique where data is transformed so that:

* **Mean = 0**
* **Standard Deviation = 1**

It helps bring all features to a similar scale while preserving the distribution of the data.

It is also called **Z-Score Normalization**.

---

## **Formula**

genui{"math_block_widget_always_prefetch_v2": {"content": "z = \frac{x - \mu}{\sigma}"}}

Where:

* **x** = Original value
* **μ (mu)** = Mean of feature
* **σ (sigma)** = Standard deviation
* **z** = Standardized value

---

## **Simple Explanation**

Standardization measures:

👉 **How far a value is from the mean**

in terms of **standard deviation**.

After scaling:

* Positive values → Above mean
* Negative values → Below mean
* Zero → Exactly at mean

---

## **Real-Time Example (Interview Friendly)**

Suppose you are building a **salary prediction model** 💼.

### Original Features:

| Feature | Range             |
| ------- | ----------------- |
| Age     | 18–60             |
| Salary  | ₹20,000–₹5,00,000 |

Here:

👉 Salary values are much larger than age values.

So models like:

* KNN
* SVM
* Gradient Descent

may give too much importance to salary.

---

### After Standardization

Both features become centered around:

* Mean = 0
* Std Dev = 1

Now all features contribute more fairly.

---

## **Example Calculation**

Suppose:

* Mean salary = ₹50,000
* Standard deviation = ₹10,000
* Employee salary = ₹70,000

Then:

z = \frac{70000 - 50000}{10000} = 2

Meaning:

👉 Salary is **2 standard deviations above the mean**.

---

## **When to Use Standardization**

Use when:

✔ Data follows approximately **normal distribution**
✔ Features have different scales
✔ Using distance or gradient-based algorithms

Very important for:

* Logistic Regression
* Linear Regression
* SVM
* Neural Networks
* PCA
* KNN

---

## **Difference Between Normalization and Standardization**

| Normalization         | Standardization                    |
| --------------------- | ---------------------------------- |
| Scales to 0–1         | Mean = 0, Std = 1                  |
| Sensitive to outliers | Handles outliers better            |
| Uses min & max        | Uses mean & std deviation          |
| Best for bounded data | Best for normally distributed data |

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"Why is Standardization important?"**

Say:

👉 *"Standardization ensures that all features contribute equally and helps optimization algorithms converge faster by keeping features on similar scales."*

That sounds very professional in interviews.
