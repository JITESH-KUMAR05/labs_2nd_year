class car:
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

c1 = car("maruti",20,2024)
c2 = car("Tata", "2i",2023)
print(c1.make)
print(c2.make)
try:
    print(c1.color)
except AttributeError:
    print("Not an attribute")