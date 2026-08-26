import csv

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
        with open("employees1.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row) 
    elif choice == '2':
        with open("employees1.csv", "r") as file:
            reader = csv.DictReader(file)
            employee_name = input("Enter employee name to search:").strip().lower()
            found = False
            for row in reader:
                name1 = row.get("Name").strip().lower()
                if name1 == employee_name:
                    print(row)
                    found = True
                    break
            if not found:
                print(f"Employee with name '{employee_name}' not found.")

    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")