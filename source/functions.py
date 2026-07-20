#import os
#from dotenv import load_dotenv
#load_dotenv()
#api_key = os.environ.get("API_KEY")
#print(api_key)

def load_dotenv(*args, **kwargs):
        return False
def main():
    greet_user("Alice")

def greet_user(user):
    return f"Hello {user}"

greet = greet_user("Alice")
print(greet)
stored_password = "password"
stored_user = "admin"

def login(
    user,
    password: str,
) -> bool:
    if user == stored_user and password == stored_password:
        return True
    else:
        return False

status = login("admin", "password1")
print(f"Status: {status}")

def args_function(*args):
    for arg in args:
        if arg == 3:
            print("Found 3!")

    # print(args)

args_function(1, 2, 3, 4, 5)

if __name__ == "__main__":
    main()
