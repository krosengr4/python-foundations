class Employee:
    def __init__(self, first_name, last_name, role, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.salary = salary

    def calculate_weekly_pay(self):
        return self.salary / 52
        