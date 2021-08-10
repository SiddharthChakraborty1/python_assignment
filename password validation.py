password_list = [str(x) for x in input('Enter comma separated password values: ').split(',')]
special_characters = ['$', '#', '@']


def checkValidity(password: str):
    lower = False
    upper = False
    numeric = False
    size = False
    special = False

    if(len(password) >= 6 and len(password)<= 12):
        size = True

    for char in password:
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isdigit():
            numeric = True
        if char in special_characters:
            special = True

    if size and lower and upper and numeric and special:
        return True
    else:
        return False

for password in password_list:
    if checkValidity(password):
        print(password)


