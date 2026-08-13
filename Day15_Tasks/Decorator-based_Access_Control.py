#8. Decorator-based Access Control
#Scenario:
#Restrict access to certain functions.
#Task:
#● Create a decorator to check user role
#● Use condition inside decorator
#● Apply decorator to multiple functions
#● Store roles in a dictionary

roles = {
    "Vivek": "admin",
    "Rahul": "user",
    "Anu": "guest"
}

def admin_required(function):

    def wrapper(username):
        user_role = roles.get(username)

        if user_role == "admin":
            return function(username)
        else:
            print("Access Denied:", username)
            print("Your role is:", user_role)

    return wrapper

@admin_required
def delete_user(username):
    print(username, "can delete users")


@admin_required
def view_reports(username):
    print(username, "can view reports")

username = input("Enter your name: ")

delete_user(username)
view_reports(username)
