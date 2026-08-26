import csv 

def load_employees():
    with open("employees1.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)

def show_all_employees():
    employees = load_employees()
    for employee in employees:
        print(employee)

def search_employee_by_name():
    employees = load_employees()
    employee_name = input("Enter employee name to search:").strip().lower()
    for employee in employees:
        name1 = employee["Name"].strip().lower()
        if name1 == employee_name:
            print(employee)
            found = True
            return 
    print(f"Employee with name '{employee_name}' not found.")

while True:
    print("""
    Employee Database
    --------------------------------
    1. Show All Employees
    2. Search Employee by Name
    3. Exit
    """)

    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        show_all_employees()

    elif choice == '2':
        search_employee_by_name()
        
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")