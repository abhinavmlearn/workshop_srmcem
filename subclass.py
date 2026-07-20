class Employee:
    no_of_employees = 0
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        Employee.no_of_employees += 1
    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
    def get_salary(self):
        self.salary = self.salary + (self.salary * 10 / 100)
        print("Salary:", self.salary)
class SoftwareDeveloper(Employee):
    def __init__(self, emp_id, name, salary, project, project_bonus):
        super().__init__(emp_id, name, "Development", salary)
        self.project = project
        self.project_bonus = project_bonus
    def display(self):
        super().display()
        print("Project:", self.project)
        print("Project Bonus:", self.project_bonus)
    def total_salary(self):
        print("Total Salary:", self.salary + self.project_bonus)
class Manager(Employee):
    def __init__(self, emp_id, name, salary, hr_bonus):
        super().__init__(emp_id, name, "Management", salary)
        self.hr_bonus = hr_bonus
    def display(self):
        super().display()
        print("HR Bonus:", self.hr_bonus)
    def total_salary(self):
        print("Total Salary:", self.salary + self.hr_bonus)

# Objects
dev1 = SoftwareDeveloper(101, "Abhinav", 50000, "Banking App", 8000)
mgr1 = Manager(201, "Aman", 70000, 10000)
print("Software Developer")
dev1.display()
dev1.total_salary()
print()
print("Manager")
mgr1.display()
mgr1.total_salary()
print()
print("Total Employees =", Employee.no_of_employees)