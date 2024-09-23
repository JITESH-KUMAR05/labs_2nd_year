def convertAndDivide(n1,n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        print(n1/n2)
    except (ValueError,ZeroDivisionError):
        print("Either the second no is zero or you entered a string")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero.")
n1 = input("Enter the number: ")
n2 = input("Enter the second number: ")
convertAndDivide(n1,n2)