class employee:
    def __init__(self, name, salary, join_year):
        self.name = name
        self.salary = salary
        self.year = join_year

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Join Year: ", self.year)
    
    def calc_expperience(self):
        exp =  2024 - self.year
        print("Experience: ", exp)

Rahul = employee("Rahul", 50000, 2019)
Rahul.display()
Rahul.calc_expperience()
JK = employee("JK", 60000, 2018)
JK.display()
JK.calc_expperience()
jy = employee("jy", 70000, 2017)
jy.display()
jy.calc_expperience()