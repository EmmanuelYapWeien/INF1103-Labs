inventory = 0
failureCount = 0

def get_valid_input():
    stockQuantity = input("Enter the quantity of items to add to inventory (or type 'quit' to quit): ")
    if stockQuantity.isdigit() or (stockQuantity.startswith('-')):
        if int(stockQuantity) > 0:
            global inventory
            inventory = process_delivery(inventory, int(stockQuantity))
            return inventory
        elif int(stockQuantity) <= 0:
            global failureCount
            failureCount += 1
            print("Invalid input. Please enter a positive number or type 'quit' to exit.")
            return None
    elif stockQuantity.lower() != 'quit':
        failureCount += 1
        print("Invalid input. Please enter a positive number or type 'quit' to exit.")
    elif stockQuantity.lower() == 'quit':
        return 'quit'

def process_delivery(current_total, new_value):
    new_value -= calculate_tax(new_value)
    current_total += new_value
    print(f"Current inventory count: {current_total}")
    return current_total

def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    return (f"Final inventory count: {total_units}\n"
            f"Number of invalid attempts: {failed_attempts}")

while get_valid_input() != 'quit':
    pass
print(generate_report(inventory, failureCount))