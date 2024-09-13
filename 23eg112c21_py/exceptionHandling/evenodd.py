def evenOdd(n):
    try:
        n = int(n)
        if n%2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Invalid input given")

n = input("Enter a number: ")
evenOdd(n)