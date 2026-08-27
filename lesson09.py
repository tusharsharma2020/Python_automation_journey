import json

with open("employee.json", "r") as file:
    employees = json.load(file)

for employee in employees:
    print(f"Name: {employee['name']}")
    new_salary = int(employee["salary"] + (employee["salary"] * employee["bonus_percentage"] / 100))
    print(f"New Salary: {new_salary}")
    print()