from isort import stream
import requests

# Get web request 
# response = requests.get('https://wwww.google.com')
# print(response.text[:300])

response = requests.get('https://www.google.com')
# response.raise_for_status()
print(response.ok)
# print(response.status_code)