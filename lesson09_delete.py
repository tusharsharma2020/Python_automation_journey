import requests
response1 = requests.get("https://dummyjson.com/users/search?q=Emily")
users = response1.json()["users"]
user_id = None
for user in users:
    if user["firstName"] == "Emily" and user["lastName"] == "Johnson":
        user_id = user["id"]
        print(f"User ID for Emily: {user_id}")
        break


response2 = requests.delete(f"https://dummyjson.com/users/{user_id}")
print(response2.status_code)
data = response2.json()
print(data)
