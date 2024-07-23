import random

bank_details = []

def create_account():
    user_details = {
        "Acc_no": "",
        "user_name": "",
        "balance": 0,
        "password":""
    }
    for i in range(10):
        n = str(random.randint(1,9))
        user_details["Acc_no"] += n
    user_details["user_name"] = input("Enter your name: ")
    user_details["balance"] = float(input("Enter your initial balance: "))
    print("Create a password for your account")
    user_details["password"] = input("Enter your password: ")
    bank_details.append(user_details)
    print("Account created successfully! Your account number is", user_details["Acc_no"])
    print("Please save your account number for further use")

def deposit():
    acc_no = input("Enter your account number: ")
    password =input("Enter your password")
    for user in bank_details:
        if user["Acc_no"] == acc_no:
            if user["password"] == password:
                amount = float(input("Enter amount to deposit: "))
                user["balance"] = user["balance"] + amount
                print("Deposit successful! Your new balance is", user["balance"])
                return
            else:
                print("Wrong password")
        else:
            print("Account not found!")

def withdraw():
    acc_no = input("Enter your account number: ")
    password =input("Enter your password")
    for user in bank_details:
        if user["Acc_no"] == acc_no:
            if user["password"] == password:
                amount = float(input("Enter amount to withdraw: "))
                if user["balance"] >= amount:
                    user["balance"] = user["balance"]-amount
                    print(f"Successfully withdraw of {amount} from {acc_no}\n")
                    print(f"Your current balance is {user["balance"]}")
                else:
                    print(f"balance Insufficient ")
            else:
                print("Wrong password")
        else:
            print("Invalid account number")

def check_balance():
    acc_no = input("Enter your account number: ")
    password =input("Enter your password")
    for user in bank_details:
        if user["Acc_no"] == acc_no:
            if user["password"] == password:
                print(f"your current balance is {user["balance"]}")
            else:
                print("Wrong password")
        else:
            print("invalid acc number")

def display_menu():
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice==4:
        check_balance()
    elif choice==5:
        break
    else:
        print("Invalid choice. Please try again.")