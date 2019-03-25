import requests

url = ('https://www.google.com/')

response = requests.get(url)
print(response)

response.ok
print(response.headers)
print(response.text)


