def square_numbers_generator(max_value):
    # Generate square numbers starting from 1
    current = 1
    
    # Continue yielding squares until the square exceeds max_value
    while current ** 2 <= max_value:
        yield current ** 2
        current += 1

# Demonstration
max_value = int(input())
for number in square_numbers_generator(max_value):
    print(number)