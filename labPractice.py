import os
import requests
import json

texts = os.listdir('data/feedback')

# saving text feedback into dictionary 
feedback = []
keys = ["title", "name", "date", "feedback"]
for text in texts:
    # strilizing
    f = open('data/feedback/'+text, "r")
    line = f.read().splitlines()
    obj =  dict(zip(keys, line))
    feeding =  json.dumps(obj)
    feedback.append(obj)
    
for data in feedback:
    print(data)

for feed in feedback:
    response = requests.post("http://localhost/feedback/", data=feed)
    if response.ok:
        print('success')
    else:
        print(f"Error: {response.status_code}")




    
    
    
    
    
