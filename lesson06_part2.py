import csv

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
