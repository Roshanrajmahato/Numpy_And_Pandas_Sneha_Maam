
# **15️⃣ Short Interview Summary**

If interviewer asks:

**"Explain PCA."**

Say:

> PCA is a dimensionality reduction technique used to reduce the number of features while preserving maximum variance. It works by computing covariance, finding eigenvalues and eigenvectors, selecting top components, and transforming data into principal components.

# **1️⃣ What is Dimensionality Reduction?**

Before PCA, understand this first.

---

## Definition

**Dimensionality Reduction** is the process of **reducing the number of input features** while keeping important information.

---

## Why Dimensionality Reduction is Needed

Real datasets often have:

```text
Too many features
```

Example:

```text
Dataset → 100 features  
Reduce → 10 important features
```

Benefits:

✔ Faster computation
✔ Less memory usage
✔ Reduce overfitting
✔ Better visualization

---

# **2️⃣ What is PCA (Principal Component Analysis)?** ⭐⭐⭐

**Principal Component Analysis (PCA)** is the **most popular dimensionality reduction technique**.

---

## Interview Definition

> PCA is a dimensionality reduction technique that transforms high-dimensional data into a smaller set of new variables called principal components while preserving maximum variance.

---

# **Simple Understanding**

Think:

```text
Many features → Few important features
```

Without losing much information.

---

# **3️⃣ Key Idea Behind PCA**

PCA:

✔ Finds directions with **maximum variance**
✔ Projects data onto those directions
✔ Creates new features called:

```text
Principal Components
```

---

# **4️⃣ What are Principal Components?**

Principal Components are:

```text
New transformed features
```

Important properties:

✔ Uncorrelated
✔ Ordered by importance
✔ Capture maximum variance

Example:

```text
Original Features → Height, Weight

After PCA:
PC1 → Most important direction  
PC2 → Second important direction
```

---

# **5️⃣ Why PCA is Used (Very Important)** ⭐⭐⭐

Common reasons:

---

## 1️⃣ Reduce Overfitting

Too many features:

```text
Model learns noise
```

PCA:

```text
Removes unnecessary features
```

---

## 2️⃣ Speed Up Training

Fewer features:

```text
Faster computation
```

---

## 3️⃣ Visualization

Convert:

```text
High dimensions → 2D or 3D
```

Used in:

* Data visualization
* Pattern discovery

---

# **6️⃣ How PCA Works — Step-by-Step** ⭐⭐⭐

Very important for interviews.

---

## Step 1 — Standardize Data

Make mean:

```text
0
```

Make standard deviation:

```text
1
```

Why:

```text
Features should be comparable
```

---

## Step 2 — Compute Covariance Matrix

Measures:

```text
Relationship between features
```

Example:

Height vs Weight correlation.

---

## Step 3 — Compute Eigenvalues & Eigenvectors

Important step.

Eigenvectors:

```text
Directions of variance
```

Eigenvalues:

```text
Amount of variance
```

---

## Step 4 — Select Top Components

Choose:

```text
Largest eigenvalues
```

Because:

```text
They contain most information
```

---

## Step 5 — Transform Data

Project data onto:

```text
Selected principal components
```

Result:

```text
Reduced dataset
```

---

# **7️⃣ Mathematical Idea Behind PCA**

Core idea:

Maximize variance along new direction.

Principal Component:

[
Z = W^T X
]

Where:

* **Z** → Transformed data
* **W** → Eigenvectors
* **X** → Original data

(No need deep math in most interviews, just concept.)

---

# **8️⃣ Real Dataset Example**

Let's take:

```text
Student dataset:
Height
Weight
Age
Marks
Study Hours
```

Total:

```text
5 features
```

Using PCA:

```text
Reduce → 2 principal components
```

Result:

```text
PC1 → Study + Marks behavior  
PC2 → Physical characteristics
```

Used for:

✔ Visualization
✔ Modeling

---

# **9️⃣ Explained Variance (Very Important)** ⭐⭐⭐

Explained variance tells:

```text
How much information retained
```

Example:

| Component | Variance |
| --------- | -------- |
| PC1       | 70%      |
| PC2       | 20%      |
| PC3       | 5%       |
| PC4       | 3%       |
| PC5       | 2%       |

Total:

```text
PC1 + PC2 = 90%
```

So:

```text
Keep first 2 components
```

---

# **🔟 Advantages of PCA**

✔ Reduces dimensionality
✔ Removes correlated features
✔ Improves speed
✔ Helps visualization

---

# **11️⃣ Disadvantages**

❌ Loss of interpretability
❌ Some information loss
❌ Sensitive to scaling

---

# **12️⃣ PCA vs Feature Selection**

Very common comparison.

| Feature | PCA              | Feature Selection |
| ------- | ---------------- | ----------------- |
| Type    | Transformation   | Selection         |
| Output  | New features     | Original features |
| Example | Combine features | Remove features   |

---

# **13️⃣ Real-World Applications**

Very important.

---

## Image Compression 📷

Reduce:

```text
Image size
```

While keeping:

```text
Important details
```

---

## Face Recognition 👤

Used in:

* Security systems
* Biometrics

---

## Data Visualization 📊

Used to:

```text
Plot high-dimensional data
```

---

## Finance

Used for:

```text
Stock pattern analysis
```

Example companies:

* Goldman Sachs
* JP Morgan

---

# **14️⃣ Interview Cross Questions** 🔥

---

## Q1 — What is PCA?

**Answer:**

> PCA is a dimensionality reduction technique that transforms data into principal components while preserving maximum variance.

---

## Q2 — Why PCA is used?

**Answer:**

```text
Reduce dimensionality  
Remove correlation  
Improve speed  
Visualize data
```

---

## Q3 — What are eigenvalues?

**Answer:**

> Eigenvalues represent the amount of variance captured by each principal component.

---

## Q4 — What are eigenvectors?

**Answer:**

> Eigenvectors represent the direction of principal components.

---

## Q5 — Why standardization is required before PCA?

**Answer:**

Because:

```text
Features must be on same scale
```

---

## Q6 — What is explained variance?

**Answer:**

> Explained variance measures how much information each principal component retains.

---
