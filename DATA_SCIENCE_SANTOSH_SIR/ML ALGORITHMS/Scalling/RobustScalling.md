# **Robust Scaling**

## **Interview-Ready Answer**

**Robust Scaling** is a feature scaling technique that scales data using the:

* **Median**
* **Interquartile Range (IQR)**

instead of mean and standard deviation.

It is mainly used when the dataset contains **outliers**, because median and IQR are less affected by extreme values.

---

## **Formula**

x_{scaled} = \frac{x - \text{Median}}{Q_3 - Q_1}

Where:

* **Median** = Middle value
* **Q1** = 25th percentile
* **Q3** = 75th percentile
* **IQR = Q3 − Q1**

---

## **Simple Explanation**

Robust Scaling works by:

👉 Centering data around the **median**
👉 Scaling based on the **spread of middle values**

Because it ignores extreme values, it performs well when outliers exist.

---

## **Real-Time Example (Interview Friendly)**

Suppose you are building a **salary prediction model** 💼.

### Salaries:

₹25K, ₹30K, ₹35K, ₹40K, ₹45K, ₹50K, ₹10 Crore

Here:

👉 ₹10 Crore is an **outlier**.

If you use:

* **Standardization** → Mean gets heavily affected
* **Min-Max Scaling** → Most values become compressed

But with **Robust Scaling**:

* Median stays stable
* Scaling remains meaningful

So the model learns better.

---

## **Why Robust Scaling is Important**

✔ Handles **outliers effectively**
✔ Prevents distortion from extreme values
✔ Better than Min-Max when data is skewed
✔ Improves performance of distance-based models

---

## **When to Use Robust Scaling**

Use it when:

✔ Dataset contains many outliers
✔ Data distribution is skewed
✔ Extreme values exist

Common use cases:

* Financial data
* Salary data
* Transaction amounts
* Fraud detection datasets

---

## **Difference Between Scaling Methods**

| Method          | Uses           | Problem               |
| --------------- | -------------- | --------------------- |
| Min-Max Scaling | Min & Max      | Sensitive to outliers |
| Standardization | Mean & Std Dev | Affected by outliers  |
| Robust Scaling  | Median & IQR   | Best for outliers     |

---

## **Python Interview Line ⚡**

If interviewer asks:

**"Which scaler would you use when dataset has outliers?"**

Say:

👉 *"I would prefer Robust Scaling because it uses median and IQR, which are less sensitive to extreme values."*

That is a very strong interview answer.

---

## **Scikit-Learn Implementation**

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()

X_scaled = scaler.fit_transform(X)
```

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"Why is it called Robust Scaling?"**

Say:

👉 *"Because it is robust to outliers and extreme values compared to normalization and standardization."*

That sounds very interview-ready.
