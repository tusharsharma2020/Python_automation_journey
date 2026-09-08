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
print(response.status_code)
data = response.json()
print(data)
