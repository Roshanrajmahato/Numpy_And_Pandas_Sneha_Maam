
**"What is Sensitivity vs Specificity?"**

You can answer:

> Sensitivity measures how well a model identifies actual positive cases, while Specificity measures how well it identifies actual negative cases. Sensitivity is important when missing positives is dangerous, such as in disease detection, while Specificity is important when false positives are costly.

# **Q53. Specificity vs Sensitivity — Detailed Explanation**

## **1️⃣ What is Sensitivity? (Recall / True Positive Rate)**

**Sensitivity** measures:

> **How well the model detects actual positive cases.**

In simple words:

> Out of all real positive cases, how many did the model correctly identify?

This is extremely important when:

> Missing a positive case is dangerous.

---

## **Sensitivity Formula**

Sensitivity = \frac{TP}{TP + FN}

Where:

* **TP** → True Positives
* **FN** → False Negatives

Meaning:

High Sensitivity → Few missed positives.

---

# **2️⃣ What is Specificity? (True Negative Rate)**

**Specificity** measures:

> **How well the model correctly identifies negative cases.**

In simple words:

> Out of all real negative cases, how many were correctly predicted as negative?

Important when:

> False alarms must be minimized.

---

## **Specificity Formula**

Specificity = \frac{TN}{TN + FP}

Where:

* **TN** → True Negatives
* **FP** → False Positives

Meaning:

High Specificity → Few false alarms.

---

# **3️⃣ Sensitivity vs Specificity — Core Difference**

| Metric          | Measures            |
| --------------- | ------------------- |
| **Sensitivity** | Detecting positives |
| **Specificity** | Detecting negatives |

Simple memory trick:

> **Sensitivity → Sick people detected**
> **Specificity → Safe people confirmed**

---

# **4️⃣ Understanding Using Medical Example**

This is the **most common real-world example**.

Suppose:

COVID Testing.

Total Patients:

| Condition | Count |
| --------- | ----- |
| Infected  | 100   |
| Healthy   | 900   |

---

## **Sensitivity Example**

Model detects:

95 infected correctly.

Misses:

5 infected.

So:

TP = 95
FN = 5

Sensitivity:

= 95 / (95 + 5)
= **95%**

Meaning:

> Model detects **95% of infected patients.**

Very good detection.

---

## **Specificity Example**

Model correctly identifies:

882 healthy.

Wrongly flags:

18 healthy as infected.

So:

TN = 882
FP = 18

Specificity:

= 882 / (882 + 18)
= **98%**

Meaning:

> Model correctly identifies **98% of healthy people.**

Few false alarms.

---

# **5️⃣ Why Both Are Important**

Real systems need:

✔ High Sensitivity
✔ High Specificity

Because:

* Missing disease → Dangerous
* False alarm → Expensive

Balance is needed.

---

# **6️⃣ Trade-Off Between Sensitivity and Specificity**

Very important concept.

Usually:

If Sensitivity increases → Specificity decreases.

If Specificity increases → Sensitivity decreases.

Reason:

Threshold changes affect predictions.

---

## **Example**

Lower threshold:

More positives predicted.

Result:

✔ Sensitivity increases
❌ Specificity decreases

Higher threshold:

Fewer positives predicted.

Result:

✔ Specificity increases
❌ Sensitivity decreases

---

# **7️⃣ Real-Time Example (Your Given Example Expanded)**

COVID Test:

Sensitivity = **95%**

Means:

> Detects 95% infected people.

Specificity = **98%**

Means:

> Correctly identifies 98% healthy people.

Both important.

---

# **8️⃣ When Sensitivity is More Important**

Use high Sensitivity when:

Missing positives is dangerous.

Examples:

✔ Cancer detection
✔ COVID detection
✔ Fraud detection
✔ Fire alarm systems

Because:

False negative → Dangerous.

---

# **9️⃣ When Specificity is More Important**

Use high Specificity when:

False alarms costly.

Examples:

✔ Spam filtering
✔ Credit approval
✔ Legal decisions
✔ Alarm systems

Because:

False positive → Expensive.

---

# **🔟 Sensitivity vs Precision**

Common confusion.

| Metric          | Measures                 |
| --------------- | ------------------------ |
| **Sensitivity** | Detects positives        |
| **Precision**   | Correctness of positives |

Sensitivity:

Focuses on FN.

Precision:

Focuses on FP.

---

# **11️⃣ Relationship with ROC Curve**

ROC uses:

✔ Sensitivity (TPR)
✔ False Positive Rate

So:

Sensitivity is key in ROC.

---

# **12️⃣ Practical Interpretation**

Suppose:

Sensitivity = **95%**

Meaning:

Out of 100 infected people:

95 detected
5 missed.

Suppose:

Specificity = **98%**

Meaning:

Out of 100 healthy people:

98 correctly cleared
2 falsely flagged.

---

# **13️⃣ Advantages**

✔ Easy to interpret
✔ Important for healthcare
✔ Useful in risk-based systems
✔ Helps threshold selection

---

# **14️⃣ Disadvantages**

❌ Need both metrics
❌ Trade-off exists
❌ Not enough alone

Often combined with:

✔ Precision
✔ Recall
✔ F1 Score

---

# **15️⃣ Interview Cross Questions 🔥**

Very commonly asked.

---

## **Cross Q1: What is another name for Sensitivity?**

Answer:

> **Recall** or **True Positive Rate**

---

## **Cross Q2: What is another name for Specificity?**

Answer:

> **True Negative Rate**

---

## **Cross Q3: Why is Sensitivity important in cancer detection?**

Answer:

Because:

Missing cancer (FN) is dangerous.

---

## **Cross Q4: Why is Specificity important in spam filtering?**

Answer:

Because:

False alarms annoy users.

---

## **Cross Q5: Can a model have high Sensitivity but low Specificity?**

Yes.

When:

Model predicts many positives.

---

## **Cross Q6: What happens when threshold decreases?**

Answer:

Sensitivity increases
Specificity decreases.

---

## **Cross Q7: Which is more important — Sensitivity or Specificity?**

Answer:

Depends on problem.

Medical → Sensitivity
Finance → Specificity

---

# **16️⃣ Short Interview Summary (Best Answer Style)**

If interviewer asks:
