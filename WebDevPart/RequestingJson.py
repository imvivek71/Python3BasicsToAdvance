# JSON is javascript object notation


import requests

response = requests.get('https://icanhazdadjoke.com/', headers  = {"Accept": "application/json"})  # for plain tect string formta


print(response.text)   # this will give the output in string format

print(type(response.text))  # class str

print(response.json())  # This will give the output in dictionary fromat

print(type(response.json()))


