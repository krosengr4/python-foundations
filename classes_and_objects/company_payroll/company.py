# This is how to import a class
from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employee_names(self):
        print('\nCurrent Employees:\n')
        for i in self.employees:
            print(i.first_name, i.last_name)
        print('_________________________________')

    def pay_employees(self):
        print('Pay employees...')
        for i in self.employees:
            print('Paycheck for:', i.first_name, i.last_name)
            print(f'Amount $:{i.calculate_paycheck():,.2f}')
            print('_________________________________')
