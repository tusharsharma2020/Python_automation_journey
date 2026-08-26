import csv

with open("employees1.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row) 
        name1 = row.get("Name")
        print(name1)
        salary1 = row.get("Monthly Salary")
        print(salary1)