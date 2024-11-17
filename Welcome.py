import datetime

def welcome_message():
    print("Welcome to the DevOps project!")

def current_datetime():
    now = datetime.datetime.now()
    print("Current date and time: ", now)

if __name__ == "__main__":
    welcome_message()
    current_datetime()