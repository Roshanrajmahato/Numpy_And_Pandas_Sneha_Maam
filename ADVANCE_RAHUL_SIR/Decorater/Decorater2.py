"""

1️⃣ ✅ Example 1 :-
Authentication System (Very Common in Web Apps)
🎯 Real Problem:-
You want users to access a function only if they are logged in.
Instead of writing login-check code inside every function, we use a decorator.


"""

def login_required(func):
    def inner(user):
        if user.get("is_logged_in"):
            return func(user)
        else:
            print("Access Denied. Please login first.")
    return inner


@login_required
def view_dashboard(user):
    print("Welcome to your dashboard", user["name"])


user1 = {"name": "Roshan", "is_logged_in": True}
user2 = {"name": "Aman", "is_logged_in": False}

view_dashboard(user1)
view_dashboard(user2)
'''
🔎 Output:
Welcome to your dashboard Roshan
Access Denied. Please login first.
'''

'''
🧠 What happened?
@login_required wraps view_dashboard
Before executing it checks login status
If allowed → original function runs
If not → stops execution
👉 This is heavily used in:
Django,Flask,FastAPI,Banking systems

'''

"""

2️⃣ ✅ Example 2 :-
Logging System (Used in Production)
🎯 Real Problem:
You want to log every function call for debugging.

"""
def logger(func):
    def inner(*args, **kwargs):
        print(f"Function '{func.__name__}' started")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' ended")
        return result
    return inner


@logger
def process_data():
    print("Processing data...")

process_data()

'''🔎 Output:
Function 'process_data' started
Processing data...
Function 'process_data' ended
🧠 Real Usage:
Companies use this for:
Debugging,Monitoring,Tracking errors,Creating logs
'''

"""
3️⃣ ✅ Example 3 :-
Execution Time Measurement (Performance Monitoring)

"""
import time

def measure_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", end - start)
        return result
    return inner


@measure_time
def train_model():
    time.sleep(2)
    print("Model training completed")

train_model()

'''
🧠 Real Usage:
Checking slow APIs,Optimizing ML training,Monitoring server performance
AI models,Data Science,Backend APIs
'''
"""

4️⃣ ✅ Example 3 :-
Role-Based Access (Admin Only Feature)
🎯 Real Problem:
Some functions should only run if the user is Admin.
"""
def admin_only(func):
    def inner(user):
        if user.get("role") == "admin":
            return func(user)
        else:
            print("Admin access required")
    return inner


@admin_only
def delete_user(user):
    print("User deleted by", user["name"])


admin = {"name": "Roshan", "role": "admin"}
normal_user = {"name": "Aman", "role": "user"}

delete_user(admin)
delete_user(normal_user)
'''
🧠 Real Usage:
Admin dashboards,Database deletion,Payment approval systems
'''
"""

5️⃣ ✅ Example 5 :-
 Input Validation (Very Important in APIs)
🎯 Real Problem:
You want to validate input before executing function.
"""
def validate_positive(func):
    def inner(x, y):
        if x < 0 or y < 0:
            print("Only positive numbers allowed")
            return
        return func(x, y)
    return inner


@validate_positive
def add(x, y):
    print("Sum:", x + y)

add(5, 3)
add(-1, 5)

'''
🧠 Real Usage:-
API input validation,Financial calculations,ML data cleaning
'''

"""

6️⃣ ✅ Example 6 :-
Caching (Used in Large Systems)
If function takes time, store result.
"""
def simple_cache(func):
    cache = {}

    def inner(x):
        if x in cache:
            print("Fetching from cache")
            return cache[x]
        result = func(x)
        cache[x] = result
        return result

    return inner


@simple_cache
def square(n):
    print("Calculating...")
    return n * n


print(square(4))
print(square(4))
'''
🧠 Real Usage:
AI inference systems,Database queries,Web APIs,E-commerce search results
'''
"""


"""