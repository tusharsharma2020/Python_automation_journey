from db import get_connection 

connection = get_connection()

cursor = connection.cursor()
name= input("Enter the name of the employee whose salary you want to update: ")
salary= input("Enter the new salary of the employee: ")
cursor.execute("UPDATE employees SET salary = %s WHERE name = %s;", (salary, name))

connection.commit()
print("Data updated successfully!")

connection.close()
