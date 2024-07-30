import re


# pattern = r'^[A-Z]{5}\d{4}\[A-Z]{1}$'
pattern = r'^\d{3}$'
pat = input("Enter a expression: ")
if re.fullmatch(pattern, pat):
    print("Valid")
else:
    print("not valid")


def pan_validdation(pan_no):
    pattern = r'^[A-Z]{5}\d{4}\[A-Z]{1}'
    if re.fullmatch(pattern, pan_no):
        print("valid")
    else:
        print("Not Valid")