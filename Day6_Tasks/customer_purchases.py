# Develop a Python program for a small shop to process customer purchases.
#Store product names and prices in a dictionary

products={"Laptop": 50000,"Mouse": 500,"Keyboard": 1200,"Headphones": 2000}

#items added to the cart in a list.

cart=[]

#product categories in a set]

categories= {"Electronics", "Accessories"}

#product details using tuples

product_details=(("Laptop", "Electronics"),("Mouse", "Accessories"),("Keyboard", "Accessories"),("Headphones", "Electronics"))


#Create functions to display products, add items to the cart, andcalculate the total bill. Use a recursive function to compute the total price of all items in the cart.
#Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
#(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
#name entered by the user does not exist).

def calculate_total(cart, index):
    if index == len(cart):
        return 0
    return cart[index] + calculate_total(cart, index + 1)


def display_products():
    print("\nAvailable Products")
    for product, price in products.items():
        print(product, ":", price)



def add_to_cart():
    try:
        product = input("Enter product name: ")

        if product not in products:
            raise NameError

        quantity = int(input("Enter quantity: "))

        price = products[product]

        total_price = price * quantity

        if not isinstance(total_price, int):
            raise TypeError

        cart.append(total_price)

        print("Item added to cart.")

    except ValueError:
        print("Error: Enter numeric quantity only.")

    except NameError:
        print("Error: Product does not exist.")

    except TypeError:
        print("Error: Invalid data type.")


def calculate_bill():
    try:
        if len(cart) == 0:
            average = 10 / len(cart)
        else:
            average = 10 / len(cart)

        total = calculate_total(cart, 0)

        print("Total Bill =", total)

    except ZeroDivisionError:
        print("Error: Cart is empty.")

    except TypeError:
        print("Error: Invalid cart data.")


while True:
    print("\n1. Display Products")
    print("2. Add to Cart")
    print("3. Calculate Bill")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        calculate_bill()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")


