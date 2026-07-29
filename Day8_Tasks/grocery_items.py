#3. Grocery List Manager
#A user wants to save grocery items in a file grocery.txt.
#Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line

file = open("grocery.txt", "w")
n = int(input("Enter the number of items: "))

for i in range(n):
    item = input("Enter item: ")
    file.write(item + "\n")

file.close()

print("Grocery items saved successfully.")
