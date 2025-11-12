"""
SINGLE RESPONSIBILITY PRINCIPLE
A class should have only one job and therefore it
should have only a single reason to change.
"""


# BAD EXAMPLE FIRST

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        # Calculate the salary
        pass

    def save_to_database(self):
        # Save the employee data to the database
        pass


"""
### WHY IS IT BAD?
In this example, the Employee class has two responsibilities: calculating the salary and
 saving the employee data to the database. If there are changes in the database structure,
  it will affect the Employee class, violating the Single Responsibility Principle.
"""


#############################################################################################
#############################################################################################
# GOOD EXAMPLE NOW
#############################################################################################
#############################################################################################

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        # Calculate the salary
        pass


class EmployeeDatabase:
    def save_to_database(self, employee:Employee):
        # Save the employee data to the database
        pass


"""
### WHY IS IT GOOD?
In the improved example, the Employee class is responsible only for representing an employee,
 and a new class EmployeeDatabase is introduced to handle the database-related operations.
  This adheres to the Single Responsibility Principle, as each class now has only one reason
   to change. If there are changes in the database, it won't affect the Employee class
"""
