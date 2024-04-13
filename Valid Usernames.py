def lenght_is_val(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def char_is_val(name):
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == '_'):
            return False
    return True


def no_red_sym(name):
    if " " in name:
        return False
    return True


def user_is_val(name):
    if lenght_is_val(name) and char_is_val(name) and no_red_sym(name):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if user_is_val(username):
        print(username)
