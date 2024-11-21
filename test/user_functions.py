# The simplest function to get the user email (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Tell me your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

