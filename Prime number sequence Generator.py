def prime_generator(max_value):
    # Function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Generate prime numbers up to max_value
    for num in range(2, max_value + 1):
        if is_prime(num):
            yield num

# Demonstration
max_value = int(input())
for number in prime_generator(max_value):
    print(number)