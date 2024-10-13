import re

pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-z0-9]+\.[a-zA-z0-9]+$'
email = input("Enter your email: ")
if re.fullmatch(pattern, email):
    print("Email is valid.")
else:
    print("Email is not valid.")
