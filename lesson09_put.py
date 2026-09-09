import requests
new_user = {
    "firstName": "John",
    "lastName": "Doe",
    "age":30,
    "company":{
        "title":"Backend Developer",
    }
}
response = requests.post("https://dummyjson.com/users/add", json=new_user)

updated_user = {
    "age": "31",
    "company":{
        "title":"Senior Backend Developer",
    }
}
response1 = requests.get("https://dummyjson.com/users/search?q=Emily")
users = response1.json()["users"]
user_id = None
for user in users:
    if user["firstName"] == "Emily" and user["lastName"] == "Johnson":
        user_id = user["id"]
        print(f"User ID for Emily: {user_id}")
        break


response2 = requests.put(f"https://dummyjson.com/users/{user_id}", json=updated_user)
print(response2.status_code)
data = response2.json()
print(data)
