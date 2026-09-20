from db import get_connection 

connection = get_connection()
cursor = connection.cursor()


def view_employees():
    cursor.execute("SELECT name, salary FROM employees;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Name:{row[0]}, Salary:{row[1]}")

def add_employee():
    name = input("Enter the name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s);", (name, salary))
    connection.commit()
    print("Employee added successfully!")
    

def update_employee_salary():
    name = input("Enter the name of the employee whose salary you want to update: ")
    salary = int(input("Enter the new salary of the employee: "))
    cursor.execute("UPDATE employees SET salary = %s WHERE LOWER(name) = LOWER(%s);", (salary, name))
    connection.commit()
    print("Employee salary updated successfully!")
    

def delete_employee():
    name= input("enter the name of the employee you want to delete: ")
    cursor.execute("DELETE FROM employees WHERE LOWER(name) = LOWER(%s);", (name,))
    connection.commit()
    print("Employee deleted successfully!")
    if cursor.rowcount == 0:
        print("No employee found with that name.")

    
running = True

while running == True:
    choice = input(f"""
 =========HR Employee Management System=========
 1.View all Employees
 2.Add Employee
 3.Update Employee Salary
 4.Delete Employee
 5.Exit
 Enter your choice: 
 """)
    if choice == '1':
        view_employees()
    elif choice == '2':
        add_employee()
    elif choice == '3':
        update_employee_salary()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        print("Exiting the program.")
        connection.close()
        running = False
    else:
        print("Invalid choice! Please try again.")
    



