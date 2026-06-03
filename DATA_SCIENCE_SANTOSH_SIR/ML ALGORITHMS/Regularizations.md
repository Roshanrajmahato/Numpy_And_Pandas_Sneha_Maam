# **Q13. What is Regularization?**

## **Interview-Ready Answer**

**Regularization** is a technique used to **prevent overfitting** by adding a **penalty term** to the loss function, which discourages the model from learning overly complex patterns.

It works by **keeping model weights small**, so the model focuses on important features rather than memorizing noise.

The two main types are:

* **L1 Regularization (Lasso)** → Can make some weights exactly **zero** (feature selection)
* **L2 Regularization (Ridge)** → **Shrinks weights** but rarely makes them zero

A parameter called **λ (lambda)** controls the strength of regularization.

---

## **Simple Explanation**

Regularization is like **adding rules to prevent overcomplication**.

Without regularization:

* Model memorizes training data
* Performs very well on training
* Performs poorly on new data

With regularization:

* Model learns general patterns
* Performs well on unseen data

---

## **Real-Time Example (Interview Friendly)**

Imagine building a **house price prediction model** 🏠.

Without regularization:

* Training Accuracy = **98%**
* Test Accuracy = **70%**
* Model memorized noise (**overfitting**)

With **L2 Regularization**:

* Training Accuracy = **87%**
* Test Accuracy = **84%**
* Model generalizes better

👉 Even though training accuracy decreased slightly, **test performance improved**, which is the real goal.

---

## **Types of Regularization**

### **1. L1 Regularization (Lasso)**

* Adds **absolute value of weights** as penalty
* Can reduce some weights to **zero**
* Helps in **feature selection**

Best used when:

* Many irrelevant features exist

---

### **2. L2 Regularization (Ridge)**

* Adds **square of weights** as penalty
* Shrinks weights but keeps all features
* Most commonly used

Best used when:

* All features contribute somewhat

---

## **Why Regularization is Important**

✔ Prevents **overfitting**
✔ Improves **generalization**
✔ Makes model **simpler**
✔ Helps with **feature selection** (L1)

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"What happens if lambda (λ) is very large?"**

Say:

👉 *"If lambda is too large, the model becomes too simple and may underfit because weights shrink too much."*

That shows **deep understanding**.

---

Next question:

# **Q14. Gradient Descent?**
