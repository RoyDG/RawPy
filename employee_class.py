class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_dep):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_dep = emp_dep

    def assign_dept(self, new_dept):
        self.emp_dep = new_dept

    def cal_salary(self, salary, working_hours):
        overtime_hours = max(working_hours - 50, 0)
        overtime_amount = (overtime_hours * (salary / 50))
        total_salary = salary + overtime_amount
        return total_salary

    def print_employee(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Salary: ${self.emp_salary}")
        print(f"Department: {self.emp_dep}")
        print()


# Sample Employee Data
ADAM = Employee("A2134", "ADAM", 78000, "Accounting")
JONAS = Employee("J2314", "JONAS", 56000, "Human Resources")
ASHLY = Employee("A7645", "ASHLY", 128000, "MARKETING")

# Using methods to manipulate and print employee details
ADAM.assign_dept("Finance")
print("Details for 1st Employee :")
ADAM.print_employee()

JONAS_salary = JONAS.cal_salary(JONAS.emp_salary, 60)
print(f"Total Salary for 2nd Employee (with overtime): ${JONAS_salary}")

print("Details for 3rd Employee :")
ASHLY.print_employee()
