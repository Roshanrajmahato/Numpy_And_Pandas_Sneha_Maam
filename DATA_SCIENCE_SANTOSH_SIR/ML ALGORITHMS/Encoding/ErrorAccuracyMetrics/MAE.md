
**"What is Mean Absolute Error?"**

You can answer:

> Mean Absolute Error (MAE) is a regression evaluation metric that measures the average absolute difference between actual and predicted values. It provides an easily interpretable error measure because it uses the same units as the target variable. Unlike MSE, MAE is less sensitive to outliers since it does not square the errors.

## **1️⃣ What is Mean Absolute Error (MAE)?**

**Mean Absolute Error (MAE)** is a **regression evaluation metric**.

It measures:

> **Average of absolute differences between actual and predicted values.**

In simple words:

> It tells **how far predictions are from actual values on average**, without considering direction.

Used in:

✔ Regression problems
✔ Forecasting
✔ Demand prediction
✔ Price prediction

---

## **MAE Formula**

MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|

Where:

* **n** → Number of observations
* **yᵢ** → Actual value
* **ŷᵢ** → Predicted value
* **| |** → Absolute value (removes negative sign)

---

# **2️⃣ Step-by-Step Calculation Example**

Using your **house price example**:

### Given Errors:

* -20K
* +10K
* +50K
* -10K

---

## **Step 1: Take Absolute Values**

| Error | Absolute Error |
| ----- | -------------- |
| -20K  | 20K            |
| +10K  | 10K            |
| +50K  | 50K            |
| -10K  | 10K            |

(Removes negative signs)

---

## **Step 2: Find Average**

Add:

20 + 10 + 50 + 10
= **90K**

Divide by 4:

MAE = 90 / 4
MAE = **22.5K**

✔ **Final MAE = $22,500**

Meaning:

> Average prediction error is **$22.5K**.

---

# **3️⃣ What Does MAE Tell Us?**

MAE tells:

> Average magnitude of prediction errors.

Important:

✔ **Lower MAE = Better model**
❌ **Higher MAE = Worse model**

---

# **4️⃣ Why Absolute Value is Used**

Very important concept.

Absolute value:

✔ Removes negative signs
✔ Prevents error cancellation

Example:

Without absolute value:

+10 and -10 → 0 ❌

That hides errors.

With absolute:

10 + 10 → 20 ✔

Correct measurement.

---

# **5️⃣ Units of MAE (Very Important)**

MAE units are:

> **Same as target variable**

Example:

If predicting:

House price → Dollars ($)

Then:

MAE → Dollars ($)

That makes MAE:

> Easy to interpret.

---

## **Example Interpretation**

MAE = **$22,500**

Means:

> On average, predictions are wrong by **$22.5K**.

Very intuitive.

---

# **6️⃣ MAE vs MSE (Very Important Comparison)**

This is commonly asked in interviews.

| Metric  | Error Type        |
| ------- | ----------------- |
| **MAE** | Linear penalty    |
| **MSE** | Quadratic penalty |

Meaning:

MSE punishes large errors more.

MAE treats all errors equally.

---

## **Example Comparison**

Errors:

2, 2, 20

MAE:

(2 + 2 + 20)/3
= **8**

MSE:

(4 + 4 + 400)/3
= **136**

See:

Large error dominates MSE.

But not MAE.

---

# **7️⃣ When Should You Use MAE?**

Use MAE when:

✔ Outliers exist
✔ Equal penalty desired
✔ Interpretability important
✔ Real-world error understanding needed

Common in:

* Sales forecasting
* Demand prediction
* Temperature prediction
* Delivery time estimation

---

# **8️⃣ When MAE Can Be Problematic**

Avoid MAE when:

❌ Large errors must be penalized heavily
❌ Optimization speed matters
❌ Smooth gradients required

Because:

MAE not differentiable at zero.

That affects:

Gradient-based algorithms.

---

# **9️⃣ Real-World Example (Expanded)**

House Price Prediction:

| Actual | Predicted | Error |
| ------ | --------- | ----- |
| 200K   | 180K      | -20K  |
| 300K   | 310K      | +10K  |
| 500K   | 550K      | +50K  |
| 250K   | 240K      | -10K  |

Absolute errors:

20K, 10K, 50K, 10K

MAE:

= **$22.5K**

Meaning:

Average prediction error:

> **$22,500**

---

# **🔟 Advantages of MAE**

✔ Easy to understand
✔ Same units as target
✔ Less sensitive to outliers
✔ Interpretable

---

# **11️⃣ Disadvantages of MAE**

❌ Not differentiable at zero
❌ Large errors not punished strongly
❌ Optimization slower than MSE

---

# **12️⃣ MAE vs RMSE**

Another important comparison.

| Metric   | Behavior             |
| -------- | -------------------- |
| **MAE**  | Equal error penalty  |
| **RMSE** | Larger error penalty |

RMSE:

Sensitive to large errors.

MAE:

More robust.

---

# **13️⃣ Visual Understanding**

Think:

MAE measures:

> Average distance between predicted and actual values.

Like:

Distance between points on graph.

---

# **14️⃣ Interview Cross Questions 🔥**

Very commonly asked.

---

## **Cross Q1: Why use absolute value in MAE?**

Answer:

To:

Prevent positive and negative errors from cancelling.

---

## **Cross Q2: What does Lower MAE mean?**

Answer:

Predictions closer to actual values.

Better model.

---

## **Cross Q3: Which is more sensitive to outliers — MAE or MSE?**

Answer:

> **MSE**

Because:

Errors are squared.

---

## **Cross Q4: Can MAE be zero?**

Yes.

When:

Predicted = Actual.

Perfect model.

---

## **Cross Q5: Why is MAE easier to interpret than MSE?**

Answer:

Because:

MAE has same units as target variable.

---

## **Cross Q6: When is MAE preferred over MSE?**

Answer:

When:

Outliers exist.

Or:

Interpretability important.

---

## **Cross Q7: What does MAE = $22K mean?**

Answer:

Average prediction error:

> $22,000.

---

# **15️⃣ Short Interview Summary (Best Answer Style)**

If interviewer asks:
