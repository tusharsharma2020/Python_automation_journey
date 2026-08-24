def employee_card():
    name = input("Enter Name:")
    department= input("Enter department:")
    employee_id= input("Enter id:")
    clean_name = name.lower().replace(" ", "_")
    company= input("Enter company name:")
    clean_company_name = company.lower().replace(" ", "_")
    email_id = f"{clean_name}.{employee_id}@{clean_company_name}.com"
    designation = input("Enter designation:")
    return f"""
    --------------------------------
    Employee Card 
    --------------------------------
    Name: {name}
    Department: {department}
    Employee ID: {employee_id}
    Email ID: {email_id}
    Designation: {designation}
    --------------------------------
    """

print(employee_card())
