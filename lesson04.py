def get_employee_details():
    name = input("Enter your name: ")
    monthly_salary = int(input("Enter your monthly salary: "))
    bonus_percentage = int(input("Enter your bonus percentage: "))
    annual_salary = int(monthly_salary * 12 + (monthly_salary * bonus_percentage / 100))
    return f"""
    Salary Summary for {name}
    --------------------------------
    Name: {name}
    Monthly Salary: {monthly_salary}
    Bonus Percentage: {bonus_percentage}%
    Annual Salary: {annual_salary}
    """

employees = []
choice = 'y'
while choice=='y':
    employee_details=get_employee_details()
    employees.append(employee_details)
    choice = input("Do you want to add another employee? (y/n): ").lower()
    if choice != 'y':
        break
file = open("employees.csv", "w")
for employee in employees:
    file.write(employee + "\n")
file.close()

