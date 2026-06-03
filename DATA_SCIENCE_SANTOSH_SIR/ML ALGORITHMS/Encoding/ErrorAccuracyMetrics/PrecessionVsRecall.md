
**"What is Precision–Recall Curve?"**

You can answer:

> Precision–Recall Curve plots Precision versus Recall at different thresholds and is especially useful for imbalanced datasets. It shows the trade-off between detecting more positives (Recall) and reducing false positives (Precision). The Area Under Precision–Recall Curve (AUPRC) summarizes the overall model performance.

---

## **1️⃣ What is Precision–Recall (PR) Curve?**

**Precision–Recall Curve** is used to evaluate:

> **Classification model performance at different thresholds**, especially when data is **imbalanced**.

It plots:

* **Precision** → Y-axis
* **Recall** → X-axis

So:

> PR Curve shows the **trade-off between Precision and Recall**.

---

# **2️⃣ Important Terms First**

Before understanding PR Curve, you must know:

---

## **Precision**

Precision measures:

> Out of predicted positives, how many were actually correct.

Precision = \frac{TP}{TP + FP}

Meaning:

High precision → Few false alarms.

---

## **Recall (Sensitivity)**

Recall measures:

> Out of actual positives, how many were correctly detected.

Recall = \frac{TP}{TP + FN}

Meaning:

High recall → Few missed positives.

---

# **3️⃣ Why Precision–Recall Curve is Needed**

PR Curve is **very useful** when:

> Dataset is **imbalanced**.

Because:

Accuracy and ROC can look good even when minority class performance is poor.

PR Curve focuses on:

> **Positive class performance.**

Very important in:

✔ Fraud Detection
✔ Disease Detection
✔ Spam Filtering
✔ Defect Detection

---

# **4️⃣ Understanding Trade-Off Between Precision and Recall**

This is **core concept**.

Usually:

When Recall increases → Precision decreases.

When Precision increases → Recall decreases.

Why?

Because:

Lower threshold → More positives predicted → More FP → Precision drops.

Higher threshold → Fewer positives predicted → Some TP missed → Recall drops.

---

# **5️⃣ How PR Curve is Created**

Steps:

1️⃣ Choose threshold
2️⃣ Calculate Precision
3️⃣ Calculate Recall
4️⃣ Plot point
5️⃣ Change threshold
6️⃣ Repeat
7️⃣ Connect points → PR Curve

---

# **6️⃣ Understanding PR Curve Shape**

Key ideas:

✔ Curve closer to **top-right** → Better
✔ Curve near **bottom** → Poor
✔ Larger area → Better model

---

# **7️⃣ What is AUPRC?**

**AUPRC** stands for:

> **Area Under Precision–Recall Curve**

It measures:

> Overall PR performance.

Higher value:

✔ Better model

Lower value:

❌ Poor model

---

# **8️⃣ Real-Time Example (Your Given Example Expanded)**

Fraud Detection:

Dataset:

* Fraud = **1%**
* Normal = **99%**

If model predicts many fraud cases:

Recall increases.

But:

False alarms increase → Precision decreases.

PR Curve shows:

Trade-off clearly.

---

## **Example Threshold Table**

| Threshold | Precision | Recall |
| --------- | --------- | ------ |
| 0.9       | 0.95      | 0.40   |
| 0.5       | 0.80      | 0.70   |
| 0.1       | 0.50      | 0.95   |

Meaning:

Lower threshold:

✔ Recall increases
❌ Precision decreases

---

# **9️⃣ Why PR Curve is Better for Imbalanced Data**

Very important interview concept.

Example:

Fraud detection:

Fraud = 1%

Model predicts:

Mostly normal.

ROC may look good.

But:

PR Curve shows:

> Real positive performance.

That’s why:

PR Curve preferred.

---

# **🔟 PR Curve vs ROC Curve**

Very common interview question.

| Feature        | PR Curve            | ROC Curve           |
| -------------- | ------------------- | ------------------- |
| Axes           | Precision vs Recall | TPR vs FPR          |
| Best Use       | Imbalanced data     | Balanced data       |
| Focus          | Positive class      | Overall classes     |
| Interpretation | Minority-focused    | General performance |

---

# **11️⃣ Practical Interpretation**

Suppose:

AUPRC = **0.85**

Means:

Model maintains:

✔ Good precision
✔ Good recall

Across thresholds.

That’s strong performance.

---

# **12️⃣ When Should You Use PR Curve?**

Use PR Curve when:

✔ Imbalanced dataset
✔ Rare positive events
✔ False positives costly
✔ False negatives dangerous

Common in:

* Fraud Detection
* Disease Detection
* Spam Filtering
* Intrusion Detection

---

# **13️⃣ When PR Curve Not Necessary**

PR Curve less useful when:

✔ Balanced dataset
✔ Equal class distribution

In those cases:

ROC works well.

---

# **14️⃣ Visual Understanding**

Think:

Precision:

> How correct predicted positives are.

Recall:

> How many positives detected.

PR Curve:

> Shows balance between them.

---

# **15️⃣ Advantages of PR Curve**

✔ Good for imbalanced data
✔ Focuses on minority class
✔ Shows trade-off clearly
✔ Helps threshold selection

---

# **16️⃣ Disadvantages**

❌ Harder to interpret than ROC
❌ Sensitive to class imbalance
❌ Depends on prevalence

---

# **17️⃣ Interview Cross Questions 🔥**

Very commonly asked.

---

## **Cross Q1: When should you use PR Curve instead of ROC?**

Answer:

When:

Dataset is **imbalanced**.

---

## **Cross Q2: What happens when recall increases?**

Answer:

Precision usually decreases.

More false positives occur.

---

## **Cross Q3: What does High Precision mean?**

Answer:

Few false positives.

Predictions mostly correct.

---

## **Cross Q4: What does High Recall mean?**

Answer:

Few false negatives.

Most positives detected.

---

## **Cross Q5: Which is better for fraud detection — ROC or PR?**

Answer:

> **PR Curve**

Because fraud datasets are imbalanced.

---

## **Cross Q6: What does AUPRC measure?**

Answer:

Overall precision–recall performance.

Higher → Better.

---

## **Cross Q7: Can Precision be high but Recall low?**

Yes.

When:

Model predicts very few positives.

But mostly correct.

---

# **18️⃣ Short Interview Summary (Best Answer Style)**

If interviewer asks:

# Next Step

We'll continue with:

➡ **Q53 — Specificity vs Sensitivity**
(next detailed explanation with cross-questions).
