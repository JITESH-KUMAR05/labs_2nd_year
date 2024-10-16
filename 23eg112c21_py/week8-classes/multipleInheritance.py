# write a program that demonstrates multiple inheritance with classes person , worker and manager
# person class has attributes name and age
# worker class has attributes salary and experience and job
# manager class has attributes salary, department 

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class worker:
    def __init__(self, salary, experience, job):
        self.salary = salary
        self.experience = experience
        self.job = job

    def display(self):
        print("Salary: ", self.salary)
        print("Experience: ", self.experience)
        print("Job: ", self.job)

class manager(person, worker):
    def __init__(self, name, age, salary, experience, job, department):
        person.__init__(self, name, age)
        worker.__init__(self, salary, experience, job)
        self.department = department

    def display(self):
        person.display(self)
        worker.display(self)
        print("Department: ", self.department)