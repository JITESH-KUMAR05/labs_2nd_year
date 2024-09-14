def divide_and_convert(num1,num2,string_value):
    div = num = 0
    try:
        div = num1/num2
    except ZeroDivisionError:
        print("num 2 should not be zero")
    except TypeError:
        print("you should only enter only integers")
    
    try : 
        for i in string_value:
            digit = int(i)
            num = num * 10 + digit
    except ValueError:
        print("you entered some wrong string only numbers ")
    return div , num

print(divide_and_convert(10,2,"123"))
print(divide_and_convert(10,0,"23"))
print(divide_and_convert("23",23,"it"))