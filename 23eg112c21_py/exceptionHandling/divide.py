def div(n1,n2):
    try:
        div = n1/n2
        print(div)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except ValueError:
        print("Error: Invalid input")
ch = 'y'
while ch == 'y' or ch == 'Y':
    try:
        n1 = float(input("Enter the first number: "))   
        n2 = float(input("Enter the Second number: "))
        div(n1,n2)
        ch = input("do you want to run again y/Y for yes and n/N for no: ")
    except ValueError:
        print("Give some valid input")
    
    