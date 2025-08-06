from company import Company
from employee import Employee

my_company = Company();

employee1 = Employee("Kevin", "Smith", "Manager", 75000)
employee2 = Employee("Sarah", "Cottinger", "Front desk", 50000)
employee3 = Employee("Bobert", "Brown", "Janitor", 34000)

my_company.add_employee(employee1)
my_company.add_employee(employee2)
my_company.add_employee(employee3)

my_company.display_employee_names()
my_company.pay_employees()

