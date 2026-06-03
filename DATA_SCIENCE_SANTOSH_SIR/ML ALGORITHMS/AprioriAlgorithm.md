# **11️⃣ Short Interview Summary**

If interviewer asks:

**"Explain Apriori Algorithm."**

Say:

> Apriori is an association rule learning algorithm used to find frequent itemsets and generate rules based on support, confidence, and lift. It is widely used in market basket analysis to identify products that are frequently bought together.

---

# **Q40. Association Rule Learning — Apriori Algorithm (Market Basket Analysis)** ⭐⭐⭐

This topic is commonly asked in:

* Data Science interviews
* Machine Learning exams
* Business analytics roles

Especially when they ask:

👉 **"How do supermarkets recommend products?"**

---

# **1️⃣ What is Association Rule Learning? (Interview Definition)**

**Association Rule Learning** is an unsupervised learning technique used to **find relationships between items in a dataset**.

---

# **Simple Interview Definition**

> Association rule learning is a technique used to discover interesting relationships or patterns between items in large datasets.

---

# **Real-Life Example — Supermarket 🛒**

If customers buy:

```text
Bread
```

They often also buy:

```text
Butter
```

Rule formed:

```text
Bread → Butter
```

This is called:

```text
Association Rule
```

---

# **2️⃣ What is Market Basket Analysis?**

**Market Basket Analysis** is the most common application of association rule learning.

Used to:

✔ Understand customer purchase patterns
✔ Improve product placement
✔ Increase sales

Example companies:

* Amazon
* Walmart
* Flipkart

They use this to recommend:

```text
Customers who bought X also bought Y
```

---

# **3️⃣ Important Terms in Association Rules** ⭐⭐⭐

Very important — **Support, Confidence, Lift** are frequently asked.

---

# **1️⃣ Support**

Support measures:

```text
How frequently an item appears
```

Formula:

[
Support(A) = \frac{\text{Transactions containing A}}{\text{Total Transactions}}
]

---

## Example

Transactions:

```text
T1 → Bread, Milk  
T2 → Bread, Butter  
T3 → Milk, Butter  
T4 → Bread, Milk
```

Bread appears:

```text
3 times
```

Total transactions:

```text
4
```

Support:

```text
Support(Bread) = 3/4 = 0.75
```

---

# **2️⃣ Confidence**

Confidence measures:

```text
How often Y occurs when X occurs
```

Formula:

[
Confidence(A → B) =
\frac{Support(A \cap B)}
{Support(A)}
]

---

## Example

Bread → Butter

If:

```text
Bread appears → 3 times  
Bread & Butter → 1 time
```

Confidence:

```text
1/3 = 0.33
```

---

# **3️⃣ Lift** ⭐ Very Important

Lift measures:

```text
Strength of rule
```

Formula:

[
Lift(A → B) =
\frac{Confidence(A → B)}
{Support(B)}
]

---

## Lift Interpretation

| Lift Value | Meaning           |
| ---------- | ----------------- |
| Lift = 1   | No relation       |
| Lift > 1   | Positive relation |
| Lift < 1   | Negative relation |

---

# **4️⃣ What is the Apriori Algorithm?** ⭐⭐⭐

The **Apriori Algorithm** is the **most popular algorithm** used for association rule mining.

---

# **Simple Definition**

> Apriori is an algorithm used to find frequent itemsets in datasets and generate association rules.

---

# **5️⃣ How Apriori Works — Step-by-Step**

Very important.

---

## Step 1 — Set Minimum Support

Example:

```text
Min Support = 50%
```

Meaning:

```text
Item must appear in at least half transactions
```

---

## Step 2 — Find Frequent Single Items

Check:

```text
Items meeting minimum support
```

Remove:

```text
Low-frequency items
```

---

## Step 3 — Generate Item Pairs

Combine:

```text
Frequent items
```

Example:

```text
Bread + Milk  
Bread + Butter
```

---

## Step 4 — Repeat

Continue:

```text
Create larger itemsets
```

Until:

```text
No more frequent sets
```

---

## Step 5 — Generate Rules

Create rules like:

```text
Bread → Butter
Milk → Bread
```

Check:

```text
Confidence & Lift
```

---

# **6️⃣ Real Dataset Example**

Let's take:

```text
Transactions:
T1 → Bread, Milk
T2 → Bread, Butter
T3 → Milk, Butter
T4 → Bread, Milk, Butter
```

---

## Step 1 — Count Single Items

| Item   | Count |
| ------ | ----- |
| Bread  | 3     |
| Milk   | 3     |
| Butter | 3     |

All pass minimum support.

---

## Step 2 — Generate Pairs

| Pair          | Count |
| ------------- | ----- |
| Bread, Milk   | 2     |
| Bread, Butter | 2     |
| Milk, Butter  | 2     |

---

## Step 3 — Generate Triplets

```text
Bread, Milk, Butter → 1
```

If below support:

```text
Remove
```

---

## Step 4 — Generate Rules

Example:

```text
Bread → Milk
Milk → Bread
Bread → Butter
```

---

# **7️⃣ Advantages of Apriori**

✔ Easy to understand
✔ Works well with transactional data
✔ Useful for recommendation systems

---

# **8️⃣ Disadvantages**

❌ Slow for large datasets
❌ Requires many database scans
❌ Memory intensive

To solve this:

Use faster algorithm:

* FP-Growth

---

# **9️⃣ Real-World Applications**

Very important.

---

## Product Recommendation 🛒

Used by:

* Amazon
* Flipkart

Example:

```text
Laptop → Mouse
```

---

## Store Layout Optimization

Place:

```text
Frequently bought items nearby
```

Example:

```text
Bread near Butter
```

---

## Web Recommendation

Example:

```text
Users who watched X also watched Y
```

Used by:

* Netflix

---

# **🔟 Interview Cross Questions** 🔥

---

## Q1 — What is association rule learning?

**Answer:**

> It is an unsupervised learning technique used to find relationships between items in datasets.

---

## Q2 — What are important metrics?

**Answer:**

```text
Support  
Confidence  
Lift
```

---

## Q3 — What is Apriori algorithm?

**Answer:**

> Apriori is an algorithm used to find frequent itemsets and generate association rules.

---

## Q4 — What is lift?

**Answer:**

> Lift measures the strength of association between two items.

---

## Q5 — What is a real-world example?

**Answer:**

```text
Market basket analysis  
Product recommendation  
Store layout optimization
```

---

