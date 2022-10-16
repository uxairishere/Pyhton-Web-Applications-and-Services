import requests

p = {
    "search": "uxair abbas",
    "maxResults": 10
}
url = "https://www.google.com"

# get request 
response = requests.get("https://www.google.com", params=p)
if response.ok == True:
    print(response.request.url)
else:
    print("There was an error")
    
# post request
response = requests.post("https://www.google.com", data=p)
print(response.status_code)
print(response.request.body)
