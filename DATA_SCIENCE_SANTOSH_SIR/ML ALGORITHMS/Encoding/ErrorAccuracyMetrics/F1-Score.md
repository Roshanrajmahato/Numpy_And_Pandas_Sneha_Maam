
# Short Interview Answer (Best Version)

**F1 Score is the harmonic mean of Precision and Recall. It is used to measure a model’s performance when both false positives and false negatives are important. It is especially useful for imbalanced datasets.**


# Q10. What is F1 Score?


# Simple Definition

**F1 Score** is a metric that **balances Precision and Recall** into a **single value**.

👉 In simple words:
**F1 Score tells how well your model balances both correctness (Precision) and completeness (Recall).**

---

# Mathematical Formula

The F1 Score is the **harmonic mean** of Precision and Recall.

F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}

---

# Why Use F1 Score?

Sometimes:

* Precision is high
* Recall is low

OR

* Recall is high
* Precision is low

So:

👉 We need **one single metric** that balances both.

That metric is:

✔ **F1 Score**

---

# Why Harmonic Mean (Not Simple Average)?

Because:

**Harmonic mean punishes extreme values.**

Example:

Precision = **1.0**
Recall = **0.0**

Average:

(1 + 0) / 2 = **0.5** ❌ misleading

F1 Score:

= **0** ✔ correct

Because:

If either Precision or Recall is poor → F1 becomes low.

---

# Range of F1 Score

F1 Score ranges:

👉 **0 to 1**

| Value   | Meaning       |
| ------- | ------------- |
| 1       | Perfect model |
| 0       | Worst model   |
| 0.7–0.9 | Good model    |
| <0.5    | Poor model    |

---

# Example Calculation

Suppose:

Precision = **0.80**
Recall = **0.60**

Using formula:

F1 =

2 × (0.80 × 0.60) / (0.80 + 0.60)

= 2 × 0.48 / 1.40

= 0.96 / 1.40

= **0.69**

👉 F1 Score = **0.69**

Meaning:

Model has **moderate performance**.

---

# Real-Life Example

### Fraud Detection System 💳

Suppose:

Precision = **95%**
Recall = **50%**

Meaning:

* Predictions are mostly correct
* But many fraud cases missed

Result:

👉 F1 Score becomes **low**, showing imbalance.

Better Case:

Precision = **85%**
Recall = **80%**

Result:

👉 **Higher F1 Score**

Meaning:

Balanced model.

---

# When F1 Score is Important

Use F1 Score when:

✔ Dataset is **imbalanced**
✔ Accuracy is misleading
✔ Both Precision & Recall matter

---

## Real-Life Example

Spam detection systems like:

* **Gmail**

Why F1 Score matters:

Because:

* Spam emails are fewer
* Normal emails are many

Accuracy alone can mislead.

F1 Score gives better evaluation.

---

# Accuracy vs F1 Score

Very common interview comparison.

| Metric   | When Useful        |
| -------- | ------------------ |
| Accuracy | Balanced dataset   |
| F1 Score | Imbalanced dataset |

---

# Real Project Example (Very Useful for You)

In your **Fake News Detection** project:

Suppose:

Precision = **85%**
Recall = **80%**

Then:

F1 Score ≈ **0.82**

That indicates:

✔ Balanced performance
✔ Good classification model

This is a **strong point** to mention in interviews.

---

# Quick Summary of Q8–Q10 (Very Important)

These 3 questions are connected:

* **Confusion Matrix → Base**
* **Precision & Recall → Derived**
* **F1 Score → Balanced metric**

Think:

👉 Confusion Matrix → Metrics → F1 Score

---
