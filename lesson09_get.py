import requests 
url = "https://dummyjson.com/users?limit=1&skip=4"
response = requests.get(url)
data = response.json()
print( data["users"][0]["firstName"] + " is " + str(data["users"][0]["age"]) + " years old and works as " + data["users"][0]["company"]["name"])

url1 = "https://dummyjson.com/users/5" 
response1 = requests.get(url1)
data1 = response1.json()
print( data1["firstName"] + " is " + str(data1["age"]) + " years old and works as " + data1["company"]["title"])