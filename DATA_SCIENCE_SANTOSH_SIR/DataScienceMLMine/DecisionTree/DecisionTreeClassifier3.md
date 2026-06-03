Ahh 👍 you mean the **Play Tennis Dataset Decision Tree** — this is the **most famous dataset** used to explain Decision Trees.
I'll solve **one full example** step-by-step so you can **explain it in exams or interviews**.

---

# 🌳 Play Tennis Dataset — Full Solved Decision Tree

We will build a **Decision Tree** using **Information Gain** based on **Entropy**.

---

# 📊 Step 0 — Play Tennis Dataset

Goal:
👉 Predict **Play Tennis (Yes/No)**

| Day | Outlook  | Temperature | Humidity | Wind   | Play Tennis |
| --- | -------- | ----------- | -------- | ------ | ----------- |
| 1   | Sunny    | Hot         | High     | Weak   | No          |
| 2   | Sunny    | Hot         | High     | Strong | No          |
| 3   | Overcast | Hot         | High     | Weak   | Yes         |
| 4   | Rain     | Mild        | High     | Weak   | Yes         |
| 5   | Rain     | Cool        | Normal   | Weak   | Yes         |
| 6   | Rain     | Cool        | Normal   | Strong | No          |
| 7   | Overcast | Cool        | Normal   | Strong | Yes         |
| 8   | Sunny    | Mild        | High     | Weak   | No          |
| 9   | Sunny    | Cool        | Normal   | Weak   | Yes         |
| 10  | Rain     | Mild        | Normal   | Weak   | Yes         |
| 11  | Sunny    | Mild        | Normal   | Strong | Yes         |
| 12  | Overcast | Mild        | High     | Strong | Yes         |
| 13  | Overcast | Hot         | Normal   | Weak   | Yes         |
| 14  | Rain     | Mild        | High     | Strong | No          |

---

# STEP 1️⃣ — Calculate Initial Entropy

Count:

Yes = **9**
No = **5**

Entropy ≈ **0.94**

👉 This means dataset is mixed.

---

# STEP 2️⃣ — Calculate Information Gain for Each Feature

We test:

* Outlook
* Temperature
* Humidity
* Wind

After calculation:

| Feature     | Information Gain |
| ----------- | ---------------- |
| Outlook     | **0.246** ✅      |
| Temperature | 0.029            |
| Humidity    | 0.151            |
| Wind        | 0.048            |

---

# ✅ Root Node Selected:

```text
Root = Outlook
```

Because **Outlook has highest Information Gain**.

---

# 🌳 Tree After Root

```text
            Outlook
        /      |        \
     Sunny  Overcast    Rain
```

Now process each branch.

---

# STEP 3️⃣ — Branch: Outlook = Sunny

Data subset:

| Temperature | Humidity | Wind   | Play |
| ----------- | -------- | ------ | ---- |
| Hot         | High     | Weak   | No   |
| Hot         | High     | Strong | No   |
| Mild        | High     | Weak   | No   |
| Cool        | Normal   | Weak   | Yes  |
| Mild        | Normal   | Strong | Yes  |

Count:

Yes = 2
No = 3

Now test features again:

Best Feature:

```text
Humidity
```

Split:

```text
Humidity = High → No  
Humidity = Normal → Yes
```

Sunny branch completed.

---

# STEP 4️⃣ — Branch: Outlook = Overcast

Subset:

All values:

```text
Yes
```

So:

```text
Leaf = Yes
```

No split needed.

---

# STEP 5️⃣ — Branch: Outlook = Rain

Subset:

| Temperature | Humidity | Wind   | Play |
| ----------- | -------- | ------ | ---- |
| Mild        | High     | Weak   | Yes  |
| Cool        | Normal   | Weak   | Yes  |
| Cool        | Normal   | Strong | No   |
| Mild        | Normal   | Weak   | Yes  |
| Mild        | High     | Strong | No   |

Count:

Yes = 3
No = 2

Best Feature:

```text
Wind
```

Split:

```text
Wind = Weak → Yes  
Wind = Strong → No
```

Rain branch completed.

---

# 🌳 FINAL DECISION TREE

```text
                     Outlook
           /            |            \
        Sunny       Overcast         Rain
          |              |             |
      Humidity          Yes           Wind
       /     \                        /     \
    High    Normal                Weak    Strong
     No       Yes                  Yes       No
```

---

# 🎯 Final Rules (Very Important for Interview)

Convert tree into **IF–THEN rules**.

Rule 1:

```
IF Outlook = Sunny AND Humidity = High  
THEN Play Tennis = No
```

Rule 2:

```
IF Outlook = Sunny AND Humidity = Normal  
THEN Play Tennis = Yes
```

Rule 3:

```
IF Outlook = Overcast  
THEN Play Tennis = Yes
```

Rule 4:

```
IF Outlook = Rain AND Wind = Weak  
THEN Play Tennis = Yes
```

Rule 5:

```
IF Outlook = Rain AND Wind = Strong  
THEN Play Tennis = No
```

---

# 🎤 How to Explain This in Interview (Very Useful)

Say this:

> First, I calculate entropy of the dataset to measure impurity.
> Then I compute information gain for each feature like Outlook, Temperature, Humidity, and Wind.
> The feature with the highest information gain becomes the root node.
> In the Play Tennis dataset, Outlook had the highest gain, so it became the root.
> Then I split the dataset based on Outlook and repeat the same process for each branch until the data becomes pure.
> Finally, I get the complete decision tree with leaf nodes representing Yes or No.

---

# ⭐ Why Play Tennis Dataset Is Important

This example teaches:

✅ Root node selection
✅ Feature splitting
✅ Multiple features
✅ Recursive splitting
✅ Final decision rules
✅ Real interview-level understanding

---

# If you're learning Decision Trees deeply, next best steps:

I can also give:

1️⃣ **Full Entropy calculation step-by-step (numbers shown)**
2️⃣ **Same dataset solved using Gini Index**
3️⃣ **Numeric split example (like Temperature < 30)**
4️⃣ **Pruning example using Play Tennis dataset**
