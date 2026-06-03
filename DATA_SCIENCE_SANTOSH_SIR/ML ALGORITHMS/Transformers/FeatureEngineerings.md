# **Q16. What is Feature Engineering?**

## **Interview-Ready Answer**

**Feature Engineering** is the process of **creating new features or transforming existing features** from raw data to improve the performance of a machine learning model.

It involves using **domain knowledge** to make data more meaningful so that the model can learn better patterns.

Common techniques include:

* Creating **new features**
* Transforming features
* Encoding categorical data
* Handling missing values
* Scaling features

---

## **Simple Explanation**

Feature Engineering means:

👉 **Making better input features so the model performs better.**

Even a simple model can perform very well if **good features** are created.

---

## **Real-Time Example (Interview Friendly)**

Suppose you are working on an **e-commerce customer prediction system** 🛒.

### Original Features:

* Age = 35
* Account Creation Date = 2019
* Last Purchase Date = 2024

### Engineered Features:

* **Account Age** = 5 years
* **Days Since Last Purchase** = 45 days
* **Purchase Frequency** = 2.5 purchases/month

Result:

* Model Accuracy improved from **75% → 92%**

👉 This improvement happened **not by changing the model**, but by creating **better features**.

---

## **Common Feature Engineering Techniques**

### **1. Creating New Features**

Combine or derive new information from existing data.

Examples:

* **BMI** = Weight / Height²
* **Total Price** = Quantity × Unit Price
* **Age from Date of Birth**

---

### **2. Feature Transformation**

Modify existing features.

Examples:

* Log transformation
* Square root transformation
* Polynomial features

Used when:

* Data distribution is skewed

---

### **3. Encoding Categorical Variables**

Convert categories into numbers.

Methods:

* **Label Encoding**
* **One-Hot Encoding**

Example:

City:

* Delhi → 1
* Mumbai → 2
* Bangalore → 3

---

### **4. Handling Missing Values**

Fill or remove missing data.

Methods:

* Mean / Median Imputation
* Forward fill
* Dropping missing rows

---

### **5. Feature Scaling**

Make features comparable.

Methods:

* Normalization
* Standardization

---

## **Why Feature Engineering is Important**

✔ Improves **model accuracy**
✔ Helps models learn **better patterns**
✔ Reduces noise
✔ Often more important than choosing complex models

Many interviewers believe:

👉 **"Better features beat better algorithms."**

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"Which is more important — model selection or feature engineering?"**

Say:

👉 *"Feature engineering is often more important because well-designed features allow even simple models to perform very well."*

This is a **very strong interview-level answer**.

---

Next question:

# **Q17. What is Normalization?**
