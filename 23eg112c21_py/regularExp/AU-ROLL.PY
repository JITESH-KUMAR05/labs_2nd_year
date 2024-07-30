import re

def validate_roll(roll_no):
    pattern = r'^\d{2}[A-Z]{2}\d{3}[A-Z]{1}\d{2}'
    if re.fullmatch(pattern,roll_no):
        return True
    else:
        return False

roll_no = input("Enter your roll no :")
if validate_roll(roll_no):
    print("Roll no is valid")
else:
    print("not valid")
