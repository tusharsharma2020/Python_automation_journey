import requests
choice = input("press 1 to list first 5 users, press 2 to search for user by first name, press 3 to add a new user , press 4 to update a user, press 5 to delete a user , press 6 to exit: ")
if choice == "1":
    url = "https://dummyjson.com/users"
    response = requests.get(url)
    data = response.json()
    for user in data["users"][:5]:
        print(user["firstName"] + " - " + user["company"]["title"])
elif choice == "2":
    first_name= str(input("Enter the first name of the user you want to search for: "))
    url1 = f"https://dummyjson.com/users/search?q={first_name}"
    response1= requests.get(url1)
    data1= response1.json()
    user_id = None
    for user in data1["users"]:
        if user["firstName"] == first_name:
            user_id = user["id"]
            print(user["firstName"] + "(ID: " + str(user["id"]) + ")" )
            break
elif choice == "3":
    first_name = input("Enter the first name of the new user: ")
    last_name = input("Enter the last name of the new user: ")
    age = int(input("Enter the age of the new user: "))
    company_title = input("Enter the company title of the new user: ")
    new_user = {
        "firstName": first_name,
        "lastName": last_name,
        "age": age,
        "company":{
            "title": company_title,
        }
    }
    url2 = "https://dummyjson.com/users/add"
    response2 = requests.post(url2, json=new_user)
    data2 = response2.json()
    print(data2["id"])
elif choice == "4":
    first_name = input("Enter the first name of the user you want to update: ")
    title = input("Enter the new title of the user: ")
    url3 = f"https://dummyjson.com/users/search?q={first_name}"
    response3 = requests.get(url3)
    users = response3.json()["users"]
    user_id = None
    for user in users:
        if user["firstName"] == first_name:
            user_id = user["id"]
            updated_user = {
                "company":{
                    "title": title,
                }
            }
            response4 = requests.put(f"https://dummyjson.com/users/{user_id}", json=updated_user)
            response4_data = response4.json()
            print(response4_data["company"]["title"])
            break
elif choice == "5":
    first_name = input("Enter the first name of the user you want to delete: ")
    url5 = f"https://dummyjson.com/users/search?q={first_name}"
    response5 = requests.get(url5)
    users = response5.json()["users"]
    user_id = None
    for user in users:
        if user["firstName"] == first_name:
            user_id = user["id"]
            response6 = requests.delete(f"https://dummyjson.com/users/{user_id}")
            response6_data = response6.json()
            print(response6_data)
            break
elif choice == "6":
    print("Exiting the program.")
else:
    print("Invalid choice. Please try again.")





