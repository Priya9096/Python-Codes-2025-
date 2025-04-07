class Fibonacci:
    def __init__(self, max_value):
        # Initialize with max_value and set start values for the Fibonacci sequence
        self.max_value = max_value
        self.a, self.b = 0, 1

    def __iter__(self):
        # Return self to make this an iterator
        return self

    def __next__(self):
        # Implement logic to return the next Fibonacci number
        if self.a > self.max_value:
            return None
        else:
            current = self.a
            self.a, self.b = self.b, self.a + self.b
            return current

# Demonstration
max_value = int(input())
fibonacci_numbers = Fibonacci(max_value)

# Iterate through fibonacci_numbers and print each number
for number in fibonacci_numbers:
    if number is None:
        break
    print(number)