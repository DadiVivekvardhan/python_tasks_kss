#3. Shopping Cart System
#Scenario: A user adds items to a shopping cart.
#Task:
#● Store items in a list
#● Convert to set to remove duplicates
#● Use loop + condition to calculate total cost
#● Handle invalid input using try-except

cart = ["Apple", "Milk", "Bread", "Apple", "Eggs"]

print("Original Cart:")
print(cart)

unique_items = set(cart)

print("\nCart after removing duplicates:")
print(unique_items)

prices = {
    "Apple": 50,
    "Milk": 30,
    "Bread": 40,
    "Eggs": 60
}

total = 0

for item in unique_items:
    if item in prices:
        total = total + prices[item]
    else:
        print("Price not available for:", item)

print("\nTotal cost:", total)

try:
    quantity = int(input("\nEnter quantity: "))

    if quantity <= 0:
        print("Invalid quantity. Please enter a positive number.")
    else:
        final_cost = total * quantity
        print("Final cost:", final_cost)

except ValueError:
    print("Invalid input! Please enter a number.")
