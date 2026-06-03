# **Q12. Training vs Validation vs Test Set**

## **Interview-Ready Answer**

In Machine Learning, the dataset is divided into **three parts** to properly train, tune, and evaluate a model:

* **Training Set** → Used to **learn patterns** from data
* **Validation Set** → Used to **tune hyperparameters** and improve the model
* **Test Set** → Used to **evaluate final performance once**, after model development is complete

A common split is:

* **Training:** 60–80%
* **Validation:** 10–20%
* **Test:** 10–20%

**Important Rule:**
👉 The **test set should never be used during training or tuning**, otherwise the model evaluation becomes biased.

---

## **Simple Explanation**

Think of building a model like preparing for an exam 📚:

| Dataset            | Purpose          | Analogy           |
| ------------------ | ---------------- | ----------------- |
| **Training Set**   | Learn patterns   | Practice problems |
| **Validation Set** | Tune model       | Mock tests        |
| **Test Set**       | Final evaluation | Final exam        |

If you practice using the **final exam questions**, your score will look high but **real performance will be poor**.

---

## **Real-Time Example (Interview Friendly)**

Suppose you are building a **house price prediction model**:

You have **10,000 house records**.

Split data:

* **Training Set (70%) → 7,000 houses**
  Model learns relationship between:

  * Size
  * Bedrooms
  * Location
  * Price

* **Validation Set (15%) → 1,500 houses**
  Used to:

  * Choose best model
  * Tune hyperparameters
    (like learning rate, number of trees)

* **Test Set (15%) → 1,500 houses**
  Used **only once** to measure final accuracy.

---

## **Why This Split is Important**

✔ Prevents **overfitting**
✔ Helps select **best model**
✔ Gives **real-world performance estimate**
✔ Ensures **fair evaluation**

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"What happens if we use the test set during training?"**

Say:

👉 *"It leads to data leakage and overly optimistic results. The model may perform well on test data but fail on real-world unseen data."*

That line is **very interview-impressive**.

---

Next question:

# **Q13. What is Regularization?**
