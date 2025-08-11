class ProfessionalDetails:
    @staticmethod
    def print_job_title(job_title):
        print(f"Job Title: {job_title}")
    @staticmethod
    def print_salary(salary):
        print(f"Salary: {salary}")
class PersonalDetails:
    @staticmethod
    def print_name(name):
        print(f"Employee Name: {name}")
    @staticmethod
    def print_age(age):
        print(f"Employee Age: {age}")

class Employee:
    def __init__(self, name, age, job_title, salary):
        self.name = name
        self.age = age
        self.job_title = job_title
        self.salary = salary

    def display_employee_details(self):
        print("Employee Details:")
        PersonalDetails.print_name(self.name)
        PersonalDetails.print_age(self.age)
        ProfessionalDetails.print_job_title(self.job_title)
        ProfessionalDetails.print_salary(self.salary)

# Example of using the combined single-class structure
emp1 = Employee("Alice", 30, "Engineer", 90000)
emp1.display_employee_details()
