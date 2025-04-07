# Step 1: Define the logger decorator
def logger_decorator(func):
    def wrapper():
        # Log start of the function
        print("Starting function execution...")
        
        # Execute the wrapped function
        func()
        
        # Log end of the function
        print("Function execution complete.")
    return wrapper

# Step 2: Apply the decorator to a sample function
@logger_decorator
def say_hello():
    print("Hello, world!")

# Step 3: Use the decorated function
say_hello()