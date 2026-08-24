def salary_calculator():
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

print(salary_calculator())