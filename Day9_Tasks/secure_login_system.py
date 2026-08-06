#13. Secure Login System (Decorators)
#A web application wants to ensure that users are authenticated before accessing sensitive functions.
#Create a decorator that checks whether the user is logged in before allowing access to a function.

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied! Please login first.")
    return wrapper

@login_required
def view_profile():
    print("Welcome! You can access your profile.")

logged_in = True
view_profile()
