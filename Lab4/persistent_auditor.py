inventory = 0
failureCount = 0
inventoryList = []
fileName = "inventory.txt"

def get_valid_input():
    productName = input("Enter Product Name: ")
    stockQuantity = input("Enter Quantity: ")
    global inventory
    if(len(inventoryList) > 0 and inventory == 0):
        for item in inventoryList:
            inventory += int(item[1])
    if (stockQuantity.isdigit() and inventory < 500) or (stockQuantity.startswith('-')):
        if int(stockQuantity) > 0:
            inventory = process_delivery(inventory, int(stockQuantity))
            print("\nNew Order Added:\n" + productName + ", " + stockQuantity)
            inventoryList.append([productName, stockQuantity])
            return inventory
        elif int(stockQuantity) <= 0:
            global failureCount
            failureCount += 1
            print("Invalid input. Please enter a positive number or type 'quit' to exit.")
            return None
    elif productName.lower() == 'quit' or stockQuantity.lower() == 'quit' or inventory >= 500:
        return 'quit'
    else:
        failureCount += 1
        print("Invalid input. Please enter a positive number or type 'quit' to exit.")

def process_delivery(current_total, new_value):
    current_total += new_value
    print(f"Current inventory count: {current_total}")
    return current_total

def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    return (f"Final inventory count: {total_units}\n"
            f"Number of invalid attempts: {failed_attempts}")

def load_inventory():
    try:
        with open(fileName, "r") as file:
            print("Current Orders:\n")
            x=1001
            lines = file.readlines()
            for line in lines:
                if("Final inventory count" in line):
                    break
                inventoryList.append(line.strip().split(", "))
                print(f"{x}, {line.strip()}")
                x += 1
        print("\n")
    except:
        print("No previous inventory log found.")

def save_inventory(listInventory):
    with open(fileName, "w") as file:
        for item in listInventory:
            file.write(f"{item[0]}, {item[1]}\n")
        file.write(f"Final inventory count: {inventory}\n")
    print("Orders successfully saved to " + fileName)

with open(fileName, "a") as file:
    load_inventory()
while get_valid_input() != 'quit':
    pass
save_inventory(inventoryList)
print(generate_report(inventory, failureCount))
print(f"Calculated tax on final inventory: ${calculate_tax(inventory):.2f}, and the total inventory value is: ${inventory + calculate_tax(inventory):.2f}")