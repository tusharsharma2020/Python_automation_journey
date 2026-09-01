import requests
url = "https://dummyjson.com/users"
response = requests.get(url)
print(response.status_code)
data=response.json()
print(data["users"][0]["firstName"])
print(data["users"][0]["lastName"])
age = data["users"][1]["age"]
print(age)
print(data["users"][0]["firstName"] + " is " + str(data["users"][0]["age"]) + " years old and works as " + data["users"][0]["company"]["title"])
print(data["users"][0]["firstName"] + "works in the " + data["users"][0]["company"]["department"] + " at " + data["users"][0]["company"]["name"] )

for user in data["users"]:
    print(
        f"{user['firstName']} - {user['company']['title']}"
    )