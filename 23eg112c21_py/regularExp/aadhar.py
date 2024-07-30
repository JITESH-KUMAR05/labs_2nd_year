import re
'''
taking aadhar card number from the user in the format 4 digit 1 space 4 digit 1 space then 4 digit 
and dob in the format 2 digit then dot then 2 digit then dot then 4 digit 
using regular expressions 
'''
def validate_aadhar(aadhar_number):
    pattern = r'^\d{4}\s\d{4}\s\d{4}$'
    if re.fullmatch(pattern, aadhar_number):
        return True
    else:
        return False

def validate_dob(dob):
    pattern = r'^\d{2}\.\d{2}\.\d{4}$'
    if re.fullmatch(pattern, dob):
        return True
    else:
        return False
aadhar_number = input("Enter your Aadhar card number (XXXX XXXX XXXX): ")
dob = input("Enter your date of birth (DD.MM.YYYY): ")

if validate_aadhar(aadhar_number):
    print("Aadhar card number is valid.")
else:
    print("Aadhar card number is not valid.")

if validate_dob(dob):
    print("Date of birth is valid.")
else:
    print("Date of birth is not valid.")