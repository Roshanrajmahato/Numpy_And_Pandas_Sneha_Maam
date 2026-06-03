# **Serialization & Deserialization in Python (JSON and Pickle)**

## **1️⃣ What is Serialization?**

### **Definition**

**Serialization** is the process of converting Python objects into a format that can be:

* Stored in a file
* Sent over a network
* Shared between applications

### **Simple Definition (Interview)**

> Serialization means converting Python data into a storable or transferable format.

### **Example**

```python
import json

data = {"name": "Roshan", "age": 23}

json_data = json.dumps(data)

print(json_data)
```

**Output**

```
{"name": "Roshan", "age": 23}
```

Here:

* Python dictionary → JSON string

---

## **2️⃣ What is Deserialization?**

### **Definition**

**Deserialization** converts stored data back into Python objects.

### **Simple Definition (Interview)**

> Deserialization means converting stored or transferred data back into usable Python objects.

### **Example**

```python
import json

data = '{"name": "Roshan", "age": 23}'

python_data = json.loads(data)

print(python_data)
print(type(python_data))
```

**Output**

```
{'name': 'Roshan', 'age': 23}
<class 'dict'>
```

---

# **3️⃣ JSON (JavaScript Object Notation)**

## **Definition**

**JSON** is a lightweight data format used to exchange data between applications.

Very common in:

* Web APIs
* Web applications
* Microservices
* Data transfer

### **Interview Definition**

> JSON (JavaScript Object Notation) is a lightweight data-interchange format used to store and exchange data between different systems.

---

# **JSON Methods (Very Important)**

There are **4 main JSON methods**:

| Method  | Purpose              |
| ------- | -------------------- |
| dumps() | Python → JSON string |
| dump()  | Python → JSON file   |
| loads() | JSON string → Python |
| load()  | JSON file → Python   |

---

# **4️⃣ dumps() Method**

## **Definition**

Converts Python object into **JSON string**.

Used when data is inside the **same file**.

### **Example**

```python
import json

data = {"one": 100, "two": 200}

result = json.dumps(data)

print(result)
print(type(result))
```

**Output**

```
{"one": 100, "two": 200}
<class 'str'>
```

---

### **Interview Points**

* Used for serialization
* Converts Python object → JSON string
* Works inside same script
* Returns **string**

---

# **5️⃣ dump() Method**

## **Definition**

Writes Python object into **external file** in JSON format.

### **Example**

```python
import json

data = {"name": "Roshan", "city": "Bangalore"}

with open("data.json", "w") as f:
    json.dump(data, f)
```

Creates file:

```
data.json
```

Content:

```json
{"name": "Roshan", "city": "Bangalore"}
```

---

### **Interview Points**

* Used to store JSON data in file
* Serialization method
* Writes directly to file

---

# **6️⃣ loads() Method**

## **Definition**

Converts JSON string into Python object.

Used when JSON is inside a **string variable**.

### **Example**

```python
import json

data = '{"one": 100, "two": 200}'

result = json.loads(data)

print(result)
print(type(result))
```

**Output**

```
{'one': 100, 'two': 200}
<class 'dict'>
```

---

### **Interview Points**

* Used for deserialization
* Accepts **string input**
* Returns Python object

---

# **7️⃣ load() Method**

## **Definition**

Reads JSON data from external file and converts into Python object.

### **Example**

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
```

---

### **Interview Points**

* Reads JSON file
* Converts into Python object
* Used for file-based deserialization

---

# **JSON Method Summary Table**

| Operation       | Same File | External File |
| --------------- | --------- | ------------- |
| Serialization   | dumps()   | dump()        |
| Deserialization | loads()   | load()        |

Very common **interview question**.

---

# **8️⃣ Pickle Module in Python**

## **Definition**

**Pickle** is a Python module used to convert Python objects into **byte format** and store them.

### **Interview Definition**

> Pickle is used to serialize and deserialize Python objects into binary (byte) format.

---

# **Pickling and Unpickling**

## **Pickling**

Serialization process in Pickle.

Converts:

Python Object → Byte Data

Methods:

* dumps()
* dump()

---

## **Unpickling**

Deserialization process.

Converts:

Byte Data → Python Object

Methods:

* loads()
* load()

---

# **9️⃣ Pickle dumps()**

## **Definition**

Converts Python object into **byte string**.

### **Example**

```python
import pickle

data = {"name": "Roshan", "age": 23}

result = pickle.dumps(data)

print(result)
print(type(result))
```

**Output**

```
b'\x80\x04\x95...'
<class 'bytes'>
```

---

### **Interview Points**

* Serialization
* Returns **byte string**
* Used inside same file

---

# **🔟 Pickle dump()**

## **Definition**

Stores Python object into **external file**.

### **Example**

```python
import pickle

data = {"name": "Roshan", "age": 23}

with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```

File created:

```
data.pkl
```

(Binary file)

---

# **1️⃣1️⃣ Pickle load()**

## **Definition**

Reads pickled data from file.

### **Example**

```python
import pickle

with open("data.pkl", "rb") as f:
    data = pickle.load(f)

print(data)
```

---

# **1️⃣2️⃣ Pickle loads()**

## **Definition**

Converts byte string into Python object.

### **Example**

```python
import pickle

data = {"a": 10}

byte_data = pickle.dumps(data)

original = pickle.loads(byte_data)

print(original)
```

---

# **Pickle Method Summary Table**

| Operation  | Same File | External File |
| ---------- | --------- | ------------- |
| Pickling   | dumps()   | dump()        |
| Unpickling | loads()   | load()        |

---

# **13️⃣ JSON vs Pickle (Very Important Interview Question)**

| Feature          | JSON           | Pickle       |
| ---------------- | -------------- | ------------ |
| Format           | Text           | Binary       |
| Language Support | Multi-language | Python only  |
| Readability      | Human readable | Not readable |
| Security         | Safer          | Less safe    |
| Speed            | Slower         | Faster       |
| File Type        | .json          | .pkl         |

---

# **14️⃣ Key Terms Summary**

### **Serialization**

Also called:

* Sending
* Pickling
* Encoding

Meaning:

Convert Python object → storable format

---

### **Deserialization**

Also called:

* Retrieving
* Unpickling
* Decoding

Meaning:

Convert stored data → Python object

---

# **15️⃣ Real-World Usage (Very Important for Interviews)**

## **JSON is used in**

* APIs
* Web development
* Data exchange
* Configuration files

Example:

```python
import requests

response = requests.get("https://api.github.com")

data = response.json()
```

Most APIs return **JSON**.

---

## **Pickle is used in**

* Saving machine learning models
* Storing Python objects
* Caching results

Since you're working in **Data Science**, this is especially important.

Example:

```python
import pickle

model = {"accuracy": 95}

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
```

Very common in:

* Machine Learning
* Model storage

---

# **16️⃣ Most Important Interview Questions**

You should prepare these:

### Q1: What is JSON?

**Answer:**
JSON is a lightweight data format used to store and exchange data between applications.

---

### Q2: Difference between dump() and dumps()

**Answer:**

| dump()         | dumps()        |
| -------------- | -------------- |
| Writes to file | Returns string |
| External file  | Same file      |

---

### Q3: What is Pickling?

**Answer:**
Pickling is the process of converting Python objects into byte format.

---

### Q4: Difference between JSON and Pickle?

Very common question.

Key point:

> JSON is language-independent, Pickle is Python-specific.

---

### Q5: What is Serialization?

**Answer:**
Serialization is the process of converting Python objects into a format that can be stored or transmitted.

---

# **17️⃣ Short Interview Explanation (Best to Memorize)**

If interviewer asks:

**"Explain JSON and Pickle in Python."**

You can answer:

> JSON and Pickle are used for serialization and deserialization in Python.
> JSON converts Python objects into text format and is mainly used for data exchange between applications.
> Pickle converts Python objects into binary format and is mainly used for storing Python objects locally.
> JSON is human-readable and language-independent, while Pickle is faster but Python-specific.

---

# **If you're preparing for Python interviews**, the most important parts to revise are:

✔ dumps vs dump
✔ loads vs load
✔ JSON vs Pickle
✔ Serialization vs Deserialization
✔ Real-world usage examples
