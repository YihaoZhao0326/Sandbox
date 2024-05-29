PASSWORD_LENGTH = 6
password = input("password: ")
while len(password) < PASSWORD_LENGTH:
    print(f"Your password shouldn't less than {PASSWORD_LENGTH}")
    password = input("password: ")
print("*" * len(password))
