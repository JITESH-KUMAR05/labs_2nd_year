d = {
    "JK" : 19,
    "Kamal" : 20,
    "Niteesh" : 21,
    "Sam" : 22,
    "Mec" : 23,
}
try:
    name = input("Enter the name to get the age: ")
    age = d[name]
    print(age)
except KeyError:
    print("Cannot find person")