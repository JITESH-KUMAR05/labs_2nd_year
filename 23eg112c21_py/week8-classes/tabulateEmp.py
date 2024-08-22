from tabulate import tabulate

class Employee:
    def __init__(self, name, salary, join_year):
        self.name = name
        self.salary = salary
        self.join_year = join_year

    def get_experience(self):
        return 2024 - self.join_year

# Create employee instances
employees = [
    Employee("Rahul", 50000, 2019),
    Employee("JK", 60000, 2018),
    Employee("jy", 70000, 2017)
]

# Prepare data for tabulate
table = []
for emp in employees:
    table.append([emp.name, emp.join_year, emp.salary, f"{emp.get_experience()} years"])

# Print the table
headers = ["Name", "Join Year", "Salary", "Experience"]
print(tabulate(table, headers, tablefmt="grid"))