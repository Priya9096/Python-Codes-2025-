# Step 1: Define the repeat decorator
def repeat_decorator(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

# Step 2: Apply the decorator to a sample function
@repeat_decorator(3)
def say_hello():
    print("Hello, world!")

# Step 3: Use the decorated function
say_hello()