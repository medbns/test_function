def get_user_name_from_input():
    """ Not empty string. No spaces. """
    user_name = input("Create your user name: ")
    if not user_name or ' ' in user_name:
        print("Invalid user name. Must not be empty or contain spaces.")
        return None
    return user_name


def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    password = input("Create your password: ")
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(not char.isalnum() for char in password):
        print("Invalid password. It must be at least 8 characters, contain at least one number, one letter, and one special character.")
        return None
    return password


def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")
    if "@" not in email or "." not in email:
        print('Email is not valid.')
        return None
    return email
