import psycopg

connection = psycopg.connect(
    host="localhost",
    dbname="python_automation",
    user="postgres",
    password="tushar123"
)

cursor = connection.cursor()
name= input("Enter the name of the employee whose salary you want to update: ")
salary= input("Enter the new salary of the employee: ")
cursor.execute("UPDATE employees SET salary = %s WHERE name = %s;", (salary, name))

connection.commit()
print("Data updated successfully!")

connection.close()
