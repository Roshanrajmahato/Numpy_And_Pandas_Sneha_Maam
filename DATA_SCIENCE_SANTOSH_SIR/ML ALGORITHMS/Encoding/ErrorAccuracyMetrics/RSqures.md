
**"What is R²?"**

You can answer:

> R², or R-squared, measures the proportion of variance in the target variable explained by the model. It is calculated as one minus the ratio of residual variance to total variance. R² ranges from negative infinity to 1, where 1 indicates a perfect fit, 0 indicates performance equal to predicting the mean, and negative values indicate worse-than-baseline performance.

# **Q49. R² (R-squared) — Detailed Explanation**

## **1️⃣ What is R² (R-squared)?**

**R² (R-squared)** is a **regression evaluation metric**.

It measures:

> **How much of the variation in the target variable is explained by the model.**

In simple words:

> It tells **how well the model explains the data.**

---

## **R² Formula**

R^2 = 1 - \frac{SS_{res}}{SS_{tot}}

Where:

* **SS_res (Residual Sum of Squares)**
  = Error made by model

* **SS_tot (Total Sum of Squares)**
  = Total variation in data

Meaning:

> R² compares model error with baseline error.

---

# **2️⃣ What Does R² Actually Mean?**

R² tells:

> How much variance is captured by the model.

Example:

R² = **0.80**

Means:

> Model explains **80% of variation** in target.

Remaining:

> 20% unexplained (noise or missing features)

---

# **3️⃣ Understanding Variance (Important Concept)**

Variance means:

> How much values spread around mean.

Example:

House Prices:

200K, 250K, 300K, 500K

Prices vary widely.

That variation:

> Must be explained by model.

Better model:

Explains more variation → Higher R².

---

# **4️⃣ Range of R² Values**

Very important for interviews.

| R² Value    | Meaning                       |
| ----------- | ----------------------------- |
| **1**       | Perfect model                 |
| **0**       | Same as baseline (mean model) |
| **<0**      | Worse than baseline           |
| **0.7–0.9** | Good model                    |
| **>0.9**    | Excellent                     |

---

# **5️⃣ What is Baseline Model?**

Baseline model predicts:

> Mean of target value.

Example:

House Prices:

Actual:

200K, 300K, 400K

Mean:

300K

Baseline predicts:

300K for all houses.

If your model performs worse than this:

> R² becomes negative.

---

# **6️⃣ Real-Time Example (Your Given Example Expanded)**

House Price Model:

Different R² values:

---

### **Case 1: R² = 0.10**

Means:

Model explains:

> Only **10%** of variation.

Very poor.

Model not useful.

---

### **Case 2: R² = 0.80**

Means:

Model explains:

> **80%** variation.

Good model.

Useful predictions.

---

### **Case 3: R² = 0.95**

Means:

Model explains:

> **95%** variation.

Excellent performance.

Very strong model.

---

### **Sales Forecast Example**

R² = **0.85**

Means:

> Model captures **85% of sales variation.**

Very strong prediction capability.

---

# **7️⃣ How R² Works Conceptually**

R² compares:

Two errors:

1️⃣ Model Error
2️⃣ Mean Model Error

If:

Model Error << Mean Error

Then:

R² → High.

---

# **8️⃣ Why R² Can Be Negative**

Very common interview question.

R² becomes negative when:

> Model performs worse than predicting mean.

Example:

Bad predictions:

Actual: 100
Predicted: 1000

Huge error.

Baseline better.

So:

R² < 0.

---

# **9️⃣ R² vs MSE (Important Comparison)**

| Metric  | Measures                  |
| ------- | ------------------------- |
| **MSE** | Absolute prediction error |
| **R²**  | Variance explained        |

MSE:

Lower → Better

R²:

Higher → Better

---

# **🔟 Adjusted R² (Advanced but Important)**

Normal R²:

Always increases when adding features.

Even useless features.

That causes:

> Overfitting risk.

Solution:

> **Adjusted R²**

It penalizes:

Extra features.

So:

Only useful features improve score.

---

## **Adjusted R² Concept**

Normal R²:

May increase falsely.

Adjusted R²:

Increases only if feature is useful.

---

# **11️⃣ When R² is Useful**

Use R² when:

✔ Comparing regression models
✔ Measuring explained variance
✔ Evaluating goodness of fit

Common in:

* Linear Regression
* Multiple Regression
* Polynomial Regression

---

# **12️⃣ When R² Can Mislead**

R² alone is not enough when:

❌ Outliers exist
❌ Non-linear relationships
❌ Overfitting present

Always check:

* MSE
* RMSE
* Residual plots

---

# **13️⃣ Visual Interpretation**

Think:

Target values scattered.

Model tries to fit line.

Better fit:

Points close to line.

Higher R².

---

# **14️⃣ Advantages of R²**

✔ Easy to interpret
✔ Shows variance explained
✔ Good for model comparison
✔ Scale-independent

---

# **15️⃣ Disadvantages of R²**

❌ Doesn't show error size
❌ Can be misleading alone
❌ Increases with more features
❌ Doesn't detect overfitting

---

# **16️⃣ Interview Cross Questions 🔥**

Very commonly asked.

---

## **Cross Q1: What does R² = 0 mean?**

Answer:

Model is:

Same as predicting mean.

No improvement.

---

## **Cross Q2: Can R² be negative?**

Yes.

When:

Model worse than baseline.

---

## **Cross Q3: Is higher R² always better?**

Not always.

Because:

Overfitting possible.

Use:

Adjusted R².

---

## **Cross Q4: What is difference between R² and Adjusted R²?**

Answer:

R²:

Always increases with features.

Adjusted R²:

Penalizes unnecessary features.

---

## **Cross Q5: Can R² be 1?**

Yes.

When:

Perfect predictions.

Rare in real-world.

---

## **Cross Q6: What does R² = 0.85 mean?**

Answer:

Model explains:

> **85% of variance** in data.

---

## **Cross Q7: Does high R² guarantee good predictions?**

No.

Must also check:

* RMSE
* Residuals

---
