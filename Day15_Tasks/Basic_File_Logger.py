#4. Basic File Logger
#Scenario:
#A system logs user actions.
#Task:
#● Take user input
#● Store logs in a file
#● Use loop to allow multiple entries
#● Handle file errors using exception handling


try:
    with open("user_logs.txt", "a") as file:

    
        for i in range(3):

            action = input("Enter user action: ")

            file.write(action + "\n")

    print("\nLogs saved successfully.")

except FileNotFoundError:
    print("Error: File could not be found.")

except PermissionError:
    print("Error: You don't have permission to write to the file.")

except Exception as e:
    print("An error occurred:", e)

