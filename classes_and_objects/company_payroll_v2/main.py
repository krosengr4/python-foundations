from company import Company, Employee, HourlyEmployee, SalaryEmployee, CommissionEmployee

my_company = Company();

employee1 = SalaryEmployee("Kevin", "Smith", 75000)
employee2 = HourlyEmployee("Rachel", "Boobenheimer", 40, 18)
employee3 = SalaryEmployee("Sarah", "Cottinger", 50000)
employee4 = CommissionEmployee("Mike", "Jones", 30000, 40, 25.99)

my_company.add_employee(employee1)
my_company.add_employee(employee2)
my_company.add_employee(employee3)
my_company.add_employee(employee4)

my_company.display_employee_names()
my_company.pay_employees()

