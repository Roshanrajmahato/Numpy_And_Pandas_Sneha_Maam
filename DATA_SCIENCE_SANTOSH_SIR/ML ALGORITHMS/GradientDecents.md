# **Q14. What is Gradient Descent?**

## **Interview-Ready Answer**

**Gradient Descent** is an **optimization algorithm** used to **minimize the loss function** by iteratively updating model parameters in the direction of the **steepest decrease** of the loss.

It adjusts model weights step-by-step until the model reaches the **lowest possible error**.

The size of each step is controlled by the **learning rate (α)**.

---

## **Core Idea (Mathematical Update Rule)**

\theta = \theta - \alpha \frac{\partial J(\theta)}{\partial \theta}

Where:

* **θ (theta)** → Model parameters (weights)
* **α (alpha)** → Learning rate
* **J(θ)** → Loss function
* **∂J/∂θ** → Gradient (slope of loss)

---

## **Simple Explanation**

Gradient Descent works like **walking downhill** ⛰️.

* You want to reach the **lowest point** (minimum error).
* At each step, you move in the **steepest downward direction**.
* Repeat until you reach the **bottom**.

---

## **Real-Time Example (Interview Friendly)**

Imagine you are **hiking down a mountain in fog** 🌫️.

* You cannot see the valley (minimum loss).
* So you check which direction goes **downhill**.
* Take a step in that direction.
* Repeat until you reach the lowest point.

That is exactly how **Gradient Descent finds best model parameters**.

---

## **Types of Gradient Descent**

### **1. Batch Gradient Descent**

* Uses **entire dataset** for each update
* Very accurate
* But **slow** for large datasets

Best for:

* Small datasets

---

### **2. Stochastic Gradient Descent (SGD)**

* Uses **one data point at a time**
* Very fast
* Noisy but efficient

Best for:

* Large datasets

---

### **3. Mini-Batch Gradient Descent** ⭐ (Most Common)

* Uses **small batches** (e.g., 32, 64, 128 samples)
* Balanced speed and stability
* Widely used in deep learning

Best for:

* Modern ML systems

---

## **Learning Rate (Very Important)**

Learning rate **α** controls step size.

* **Too Small** → Very slow learning 🐢
* **Too Large** → Overshoots minimum ⚠️
* **Optimal** → Fast and stable convergence 🚀

---

## **Why Gradient Descent is Important**

✔ Used in **Linear Regression**
✔ Used in **Logistic Regression**
✔ Used in **Neural Networks**
✔ Core optimization method in **Deep Learning**

Almost every ML model relies on it.

---

## **Key Interview Tip ⚡**

If interviewer asks:

**"What happens if learning rate is too large?"**

Say:

👉 *"If the learning rate is too large, the algorithm may overshoot the minimum and fail to converge, causing the loss to oscillate or even increase."*

That answer sounds **very professional**.

---

Next question:

# **Q15. What is a Feature?**
