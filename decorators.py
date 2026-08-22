import re

def validate_phone(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                value = func(*args, **kwargs)
                if not re.match( r"^(09\d{9}|\+989\d{9})$" ,value):
                    raise ValueError("not valid phone number")
                else:
                    break
            except:
                print("please enter a correct phone number")
    return wrapper


def validate_n_id(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                value = func(*args, **kwargs)
                if not re.match( r"^(\d{10})$" ,value):
                    raise ValueError("national id is not valid")
                else:
                    break
            except:
                print("please enter a correct national ID")
    return wrapper
