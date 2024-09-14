
try:
    f1 = open("input.txt",'r')
    # l = f1.readline()
    # l = f1.read()
    l = f1.readlines()
    print(l)
# file exists error is called when we are tr
# except FileExistsError:
#     print("File does not exist")
except FileNotFoundError:
    print("File not found")