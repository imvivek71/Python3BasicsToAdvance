import requests


response = requests.get('https://icanhazdadjoke.com')

print(response.text)

response.ok
# print(response.headers)
#print(response.text)


