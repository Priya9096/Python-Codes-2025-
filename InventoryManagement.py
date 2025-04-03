# Define the Inventory class
class Inventory:
    def __init__(self):
        self.products = {}  # Initialize an empty dictionary to store product quantities

    def add_product(self, product_name, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be positive.")
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity
        print(f"{quantity} {product_name} added to inventory. Current quantity: {self.products[product_name]}")

    def remove_product(self, product_name, quantity):
        if product_name not in self.products:
            raise ValueError(f"Product {product_name} not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self.products[product_name]:
            raise ValueError("Not enough quantity available to remove.")
        self.products[product_name] -= quantity
        print(f"{quantity} {product_name} removed from inventory. Current quantity: {self.products[product_name]}")

# Create an instance of Inventory
inventory = Inventory()

# Function to process input safely
def process_input(input_str):
    try:
        # Expecting input in the format: "Apples 50"
        parts = input_str.split(' ')
        product_name = parts[0]
        quantity = int(parts[1])
        return product_name, quantity
    except (IndexError, ValueError):
        raise ValueError("Invalid input format. Use: '<Product> <Quantity>'")

# Add product
try:
    add_input = input()
    product_name, quantity = process_input(add_input)
    inventory.add_product(product_name, quantity)
except ValueError as e:
    print(f"Addition failed. {e}")

# Remove product
try:
    remove_input = input()
    product_name, quantity = process_input(remove_input)
    inventory.remove_product(product_name, quantity)
except ValueError as e:
    print(f"Removal failed. {e}")