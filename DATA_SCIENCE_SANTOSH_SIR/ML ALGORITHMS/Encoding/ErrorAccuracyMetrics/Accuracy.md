
# **9️⃣ Short Interview Summary (Best Answer Style)**

If interviewer asks:

**"What are the limitations of Accuracy?"**

You can answer:

> Accuracy measures overall correctness but becomes misleading in imbalanced datasets, when error costs differ, or when one class is more important. For example, in cancer detection with 990 healthy and 10 cancer patients, a model predicting all healthy achieves 99% accuracy but misses all cancer cases, making it useless. In such cases, metrics like Recall, Precision, and F1-score are more appropriate.

---

# **Q46. Accuracy Limitations — Detailed Explanation**

## **1️⃣ What is Accuracy?**

Accuracy is the **most basic evaluation metric** used in classification problems.

It measures:

> **How many predictions the model got correct out of all predictions.**

Using the formula:

Accuracy = \frac{TP + TN}{TP + TN + FP + FN}

Where:

* **TP (True Positive)** → Correctly predicted Positive
* **TN (True Negative)** → Correctly predicted Negative
* **FP (False Positive)** → Wrongly predicted Positive
* **FN (False Negative)** → Wrongly predicted Negative

---

## **2️⃣ Simple Real Example**

Suppose:

| Actual  | Predicted |
| ------- | --------- |
| Cancer  | Cancer ✅  |
| Cancer  | Healthy ❌ |
| Healthy | Healthy ✅ |
| Healthy | Healthy ✅ |

Here:

* TP = 1
* FN = 1
* TN = 2
* FP = 0

So:

Accuracy = (1 + 2) / 4
Accuracy = **75%**

That means:

> Model is correct **75% of the time**.

Seems good… but sometimes **accuracy lies ❗**

---

# **3️⃣ Why Accuracy Can Be Misleading ⚠️**

Accuracy has **major limitations** in real-world problems.

There are **3 main situations** where accuracy fails:

---

# **Limitation 1️⃣ — Imbalanced Dataset (Most Important)**

This is the **biggest problem** with accuracy.

## **What is Imbalanced Data?**

When:

> One class has **many samples**,
> Another class has **very few samples**.

Example:

Cancer Screening Dataset:

| Class   | Count |
| ------- | ----- |
| Healthy | 990   |
| Cancer  | 10    |

Total = **1000 patients**

---

## **Bad Model Example**

Model predicts:

> **All patients = Healthy**

So:

* TN = 990
* TP = 0
* FN = 10
* FP = 0

Accuracy:

= (990 + 0) / 1000
= **99% Accuracy**

Looks amazing…

But:

> ❌ **Model detected ZERO cancer patients**

This is **dangerous and useless**.

---

## **Better Metric Here: Recall**

Recall tells:

> Out of actual cancer cases, how many did we catch?

Recall:

= TP / (TP + FN)
= 0 / (0 + 10)
= **0% Recall**

That means:

> ❌ Model failed completely.

---

## **Interview Cross Question 🔁**

**Q: When should you NOT rely on Accuracy?**

Answer:

* Imbalanced datasets
* Medical diagnosis
* Fraud detection
* Spam detection
* Rare event prediction

---

# **Limitation 2️⃣ — Different Error Costs**

Sometimes:

> Some mistakes are more expensive than others.

Accuracy treats **all errors equally**, which is wrong in real life.

---

## **Real Example: Fraud Detection**

Suppose:

* FP → Blocking genuine customer
* FN → Missing fraud

Which is worse?

> Missing fraud (FN) 💸

Because:

Money is stolen.

But:

Accuracy counts FP and FN equally.

That is **not realistic**.

---

## **Interview Cross Question 🔁**

**Q: Why is False Negative dangerous in fraud detection?**

Answer:

Because:

> Fraud happens but system fails to detect it.

That causes:

> Financial loss.

---

# **Limitation 3️⃣ — When One Class Is More Important**

Sometimes:

> One class matters more than others.

Example:

Medical Diagnosis

Classes:

* Healthy
* Cancer

Missing cancer:

> Very dangerous ❌

Wrong healthy prediction:

> Not very dangerous

But:

Accuracy treats both equally.

---

## **Better Metrics Instead**

Use:

* **Recall → When missing positives is dangerous**
* **Precision → When false alarms are dangerous**
* **F1 Score → When both matter**

---

# **4️⃣ Visual Understanding Using Confusion Matrix**

|                 | Predicted Positive | Predicted Negative |
| --------------- | ------------------ | ------------------ |
| Actual Positive | TP                 | FN                 |
| Actual Negative | FP                 | TN                 |

Accuracy counts:

✔ TP
✔ TN

But ignores:

⚠ FP
⚠ FN importance

That’s the weakness.

---

# **5️⃣ Real-World Example (Your Given Example Expanded)**

Cancer Screening:

* 990 Healthy
* 10 Cancer

Model:

Predicts **Healthy for all**

Results:

| Metric    | Value     |
| --------- | --------- |
| Accuracy  | 99%       |
| Recall    | 0%        |
| Precision | Undefined |
| F1 Score  | 0         |

Conclusion:

> **High Accuracy does NOT mean good model.**

Very important interview statement.

---

# **6️⃣ When Accuracy IS Useful ✅**

Accuracy works well when:

✔ Dataset is **balanced**
✔ Error costs are **same**
✔ All classes equally important

Example:

* Digit recognition
* Image classification
* Balanced datasets

---

# **7️⃣ When Accuracy Should NOT Be Used ❌**

Avoid accuracy in:

* Fraud detection
* Disease detection
* Rare event prediction
* Spam detection
* Credit card fraud

Use:

* Recall
* Precision
* F1 Score
* ROC-AUC
* PR Curve

---

# **8️⃣ Interview-Level Cross Questions 🔥**

These are **very commonly asked follow-ups.**

---

## **Cross Q1: Can Accuracy be 100% but model still useless?**

Yes.

Example:

All predictions = majority class.

Accuracy high
Performance bad.

---

## **Cross Q2: What metric is better than Accuracy for imbalanced data?**

Answer:

* Precision
* Recall
* F1 Score
* PR Curve

Best choice:

> **Recall (when missing positives is dangerous)**

---

## **Cross Q3: Accuracy vs Recall — Difference?**

Accuracy:

Measures overall correctness.

Recall:

Measures how many **actual positives were caught.**

---

## **Cross Q4: What happens when FN increases?**

Recall decreases.

Accuracy may still look high.

That’s dangerous.

---

## **Cross Q5: Why is Accuracy misleading in cancer detection?**

Because:

Cancer cases are rare.

Model predicting "Healthy" always gives high accuracy but misses all cancers.

---
