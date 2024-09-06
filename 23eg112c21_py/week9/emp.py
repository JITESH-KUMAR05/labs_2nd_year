# 1. create a class Employee that stores an employee's name and ID. Both the name and ID should
# be publicly accessible. Implement a method get_details() that returns a string containing the
# employee's name and ID.



class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.emp_id}"

# Example usage
employee1 = Employee("Alice", "E001")
employee2 = Employee("Bob", "E002")

print(employee1.get_details())
print(employee2.get_details())