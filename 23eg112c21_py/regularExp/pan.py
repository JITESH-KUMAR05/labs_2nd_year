import re

def validate_pan_card_number(pan_number):
    pattern = r'^[A-Z]{5}\d{4}[A-Z]$'
    if re.fullmatch(pattern, pan_number):
        return True
    else:
        return False

pan_number = input("Enter your PAN card number: ")
if validate_pan_card_number(pan_number):
    print("Valid PAN card number")
else:
    print("Invalid PAN card number")