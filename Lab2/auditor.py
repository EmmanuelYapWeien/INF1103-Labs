inventory = 0
failure = 0
while True:
    quantity = input("Enter the quantity of items to add to inventory (or type 'quit' to quit): ")
    if(quantity.lower() == 'quit'):
        print(f"Final inventory count: {inventory}")
        print(f"Number of invalid attempts: {failure}")
        break
    elif quantity.isdigit() and int(quantity) >= 0:
        if(inventory <= 500):
            inventory += int(quantity)
            if(inventory > 500):
                inventory -= int(quantity)
                print("Inventory limit reached.")
                break
    elif not quantity.isdigit():
        failure += 1
        print("Invalid input. Please enter a valid number or type 'quit' to exit.")