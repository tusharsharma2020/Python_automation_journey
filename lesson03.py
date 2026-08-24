def salary_hike_calculator():
    name = input("Enter your name: ")
    current_salary = int(input("Enter your current salary: "))
    years_of_experience = int(input("Enter your years of Experience: "))
    hike = 0
    if years_of_experience <0:
        return "Experience cannot be negative."
    elif years_of_experience <= 2:
        hike = 5
    elif years_of_experience <= 5:
        hike = 10
    else:
        hike = 20
    new_salary = int(current_salary + (current_salary * hike / 100))
    return f"""
    Employee Salary Review 
    --------------------------------
    name: {name}
    Experience: {years_of_experience} years
    \n
    Current Salary: ₹{current_salary}
    Hike Awarded: {hike}%
    new Salary: ₹{new_salary}
    --------------------------------
    """

print(salary_hike_calculator())