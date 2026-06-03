"""

🔥 1️⃣ Multiple Decorators

You can apply more than one decorator to a function.

✅ Example
"""
def logger(func):
    def wrapper(*args, **kwargs):
        print("Logging started")
        result = func(*args, **kwargs)
        print("Logging ended")
        return result
    return wrapper


def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Time taken:", end - start)
        return result
    return wrapper


@logger
@timer
def task():
    print("Task running...")

'''
🔎 Execution Flow

task = logger(timer(task))
So order becomes:-
timer wraps task
logger wraps result of timer
When calling task():
Logging started
Task running...
Time taken: 0.0001
Logging ended
🧠 Rule:
Decorator closest to function runs first internally.

'''

"""

🔥 2️⃣ Decorator Inside Decorator
(Decorator with Arguments)
Sometimes we want to pass parameters to decorator.
"""
def repeat(times):              # outer decorator
    def decorator(func):        # actual decorator
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello Roshan")

greet()
'''
🔎 Output
Hello Roshan
Hello Roshan
Hello Roshan
🔎 Internal Working
greet = repeat(3)(greet)
Step-by-step:
repeat(3) → returns decorator
decorator(greet) → returns wrapper
greet becomes wrapper

🧠 Real Use Case
Used in:
Retry mechanisms,Permission levels,Rate limiting APIs,Custom logging levels'''

"""

🔥 3️⃣ Class-Based Decorators
Instead of function, we can use a class.
We must use __call__() method.
"""
class Logger:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Logging started")
        result = self.func(*args, **kwargs)
        print("Logging ended")
        return result

@Logger
def greet():
    print("Hello Roshan")  
greet()
greet = Logger(greet)
'''
When calling greet():

Python calls:

Logger.__call__()

'''
"""

🔥 Why Class-Based Decorators?
They are useful when:-
You need to store state
You need configuration
You want more control

🔥 3️⃣  Example with State
"""
class CallCounter:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print("Called", self.count, "times")
        return self.func(*args, **kwargs)


@CallCounter
def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()
'''
🔎 Output
Called 1 times
Hello!
Called 2 times
Hello!
Called 3 times
Hello!
'''
"""

🎯 Interview Comparison
Type	When to Use
Simple decorator	Add basic functionality
Multiple decorators	Combine behaviors
Decorator with arguments	Configurable behavior
Class-based decorator	Need state or complex logic
🚀 Real Industry Example (Combined)
In real backend:-
@authentication
@logging
@retry(3)
@timer
def process_payment():
    pass
🔥 1️⃣ Multiple Decorators – Real IT Example (API Service)

You want:-
Authentication check,Logging,Execution time tracking

✅ Example
"""
import time

def authenticate(func):
    def wrapper(*args, **kwargs):
        print("Checking authentication...")
        user_authenticated = True
        if not user_authenticated:
            print("Authentication Failed")
            return
        return func(*args, **kwargs)
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print("Logging request...")
        result = func(*args, **kwargs)
        print("Logging completed.")
        return result
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start)
        return result
    return wrapper


@authenticate
@logger
@timer
def process_payment():
    print("Processing payment...")
    time.sleep(1)

'''
🔎 Internal Execution
process_payment = authenticate(logger(timer(process_payment)))
🔎 Output
Checking authentication...
Logging request...
Processing payment...
Execution time: 1.00
Logging completed.
🧠 Real Industry Use

Common in:

FinTech systems

Microservices

Banking APIs

Cloud backend services

'''

"""

🔥 2️⃣ Decorator Inside Decorator (Advanced IT Example)
Used when we need configuration.
Example: Retry with configurable attempts.

✅ Retry Decorator with Argument
"""
import time

def retry(attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed")
                    time.sleep(1)
            print("All attempts failed")
        return wrapper
    return decorator

@retry(3)
def connect_to_server():
    print("Connecting...")
    raise Exception("Server not responding")

connect_to_server()

'''
🔎 Output
Connecting...
Attempt 1 failed
Connecting...
Attempt 2 failed
Connecting...
Attempt 3 f=ailed
All attempts failed
🧠 Real IT Usage
Used in:
AWS service calls,Database connection retries,Payment gateway APIs,AI model API calls


'''

"""

🔥 3️⃣ Decorator Inside Decorator – Role-Based Access

"""
def require_role(role):
    def decorator(func):
        def wrapper(user):
            if user.get("role") == role:
                return func(user)
            else:
                print("Access Denied")
        return wrapper
    return decorator

@require_role("admin")
def delete_database(user):
    print("Database deleted by", user["name"])

'''
🧠 Used In
Admin panels,HR management systems,Banking approval systems
'''
"""


🔥 4️⃣ Class-Based Decorator – Real Production Example
Useful when storing state.
✅ API Rate Limiter
"""
class RateLimiter:

    def __init__(self, limit):
        self.limit = limit
        self.calls = 0

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.calls >= self.limit:
                print("Rate limit exceeded")
                return
            self.calls += 1
            return func(*args, **kwargs)
        return wrapper
    
@RateLimiter(3)
def send_request():
    print("Request sent")

send_request()
send_request()
send_request()
send_request()
'''
🔎 Output
Request sent
Request sent
Request sent
Rate limit exceeded
🧠 Real Usage
Used in:
API throttling,Cloud services,SaaS products,AI inference endpoints
'''

"""

🔥 5️⃣ Class-Based Decorator – ML Model Call Counter

"""
class ModelMonitor:

    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("Model called", self.calls, "times")
        return self.func(*args, **kwargs)

@ModelMonitor
def predict():
    print("Running model inference")

predict()
predict()
'''
🧠 Used In
AI inference tracking,Monitoring production ML models,Logging model usage
'''
"""







"""