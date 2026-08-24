def get_employee_details():
    name = input("Enter your name: ")
    monthly_salary = int(input("Enter your monthly salary: "))
    bonus_percentage = int(input("Enter your bonus percentage: "))
    annual_salary = int(monthly_salary * 12 + (monthly_salary * bonus_percentage / 100))
    return {
    "Name": name,
    "monthly_salary": monthly_salary,
    "Bonus": bonus_percentage,
    "annual_salary": annual_salary
    }

employees = []
choice = 'y'
while choice=='y':
    employee_details=get_employee_details()
    employees.append(employee_details)
    choice = input("Do you want to add another employee? (y/n): ").lower()
    if choice != 'y':
        break
with open("employees1.csv", "w")as file:
    file.write("Name,Monthly Salary,Bonus,Annual Salary\n")
    for employee in employees:
        file.write(
            f"{employee['Name']},{employee['monthly_salary']},{employee['Bonus']},{employee['annual_salary']}\n")
file.close()

