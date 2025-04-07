class Factorial:
    def __init__(self, max_value):
        # Initialize with max_value and set start value
        self.max_value = max_value
        self.current = 0
        self.factorial = 1
    
    def __iter__(self):
        # Return self to make this an iterator
        return self
    
    def __next__(self):
        # Check if we've exceeded max_value
        if self.current > self.max_value:
            raise StopIteration
        
        # For 0th factorial
        if self.current == 0:
            self.current += 1
            return 1
        
        # Calculate factorial for subsequent values
        self.factorial *= self.current
        result = self.factorial
        self.current += 1
        
        return result

# Demonstration
max_value = int(input())
factorial_numbers = Factorial(max_value)
# Iterate through factorial_numbers and print each value
for number in factorial_numbers:
    print(number)