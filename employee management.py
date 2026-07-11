# Parent Class: Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

    def take_break(self):
        print(f"{self.name} is taking a break")


# Child Class: Teacher
class Teacher(Employee):
    def teach(self):
        print(f"{self.name} is teaching")


# Child Class: Programmer
class Programmer(Employee):
    def code(self):
        print(f"{self.name} is coding")


# Bonus Challenge: Doctor
class Doctor(Employee):
    def treat_patient(self):
        print(f"{self.name} is treating a patient")

# Create the Following Objects
teacher = Teacher("Ali", 500)
programmer = Programmer("Sara", 1000)
doctor = Doctor("Dr. Reza", 1500)   
# Test Your Program
print("--- Teacher ---")
teacher.work()
teacher.teach()
teacher.take_break()

print("\n--- Programmer ---")
programmer.work()
programmer.code()
programmer.take_break()

print("\n--- Doctor (Bonus) ---")
doctor.work()
doctor.treat_patient()
doctor.take_break()

# Print teacher.name and programmer.salary
print(f"\nteacher.name: {teacher.name}")
print(f"programmer.salary: {programmer.salary}")