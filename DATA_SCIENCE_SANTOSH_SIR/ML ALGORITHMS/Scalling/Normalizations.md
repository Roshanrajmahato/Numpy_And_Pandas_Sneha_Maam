# **Q17. What is Normalization?**

## **Interview-Ready Answer**

**Normalization** is the process of **scaling numerical features to a common range**, usually **0 to 1**, so that no feature dominates others due to its larger scale.

It is especially important for algorithms that use **distance-based calculations**, such as **KNN** and **K-Means**.

Common normalization methods include:

* **Min-Max Normalization**
* **Standardization (Z-score scaling)**
* **Robust Scaling**

---

## **Core Formula (Min-Max Normalization)**

x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}

This formula converts values into the **0 to 1 range**.

---

## **Simple Explanation**

Normalization ensures that:

👉 **All features contribute equally to the model.**

Without normalization:

* Large values dominate
* Small values get ignored

With normalization:

* All features are treated **fairly**.

---

## **Real-Time Example (Interview Friendly)**

Suppose you are building a **health risk prediction model** 🏥.

### Features Before Normalization:

* **Weight** → 50–100 kg
* **Income** → ₹30,000–₹2,00,000

Here:

👉 Income values are much larger than weight values
👉 Model may think **income is more important**, even if it's not.

### After Normalization:

Both features scale to:

* **0 to 1 range**

Result:

* **KNN Accuracy improved from 68% → 84%**

---

## **Types of Normalization**

### **1. Min-Max Normalization**

* Scales values to **0–1 range**
* Most commonly used
* Sensitive to outliers

Used when:

* Data has known minimum and maximum values.

---

### **2. Standardization (Z-Score Scaling)**

Transforms data to:

* Mean = 0
* Standard Deviation = 1

Used when:

* Data follows **normal distribution**.

---

### **3. Robust Scaling**

Uses:

* Median
* Interquartile Range (IQR)

Used when:

* Dataset contains **outliers**.

---

## **Why Normalization is Important**

✔ Improves **model performance**
✔ Prevents **feature dominance**
✔ Helps **faster convergence** in Gradient Descent
✔ Required for **distance-based algorithms**

Important algorithms needing normalization:

* **K-Nearest Neighbors (KNN)**
* **K-Means Clustering**
* **Support Vector Machines (SVM)**
* **Neural Networks**

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"Which algorithms require normalization?"**

Say:

👉 *"Normalization is important for distance-based algorithms like KNN, K-Means, SVM, and Neural Networks because feature scale directly affects distance calculations."*

That sounds **very interview-strong**.

---

Next question:

# **Q18. Parametric vs Non-Parametric Models?**
