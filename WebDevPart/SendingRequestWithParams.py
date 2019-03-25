# Query string
# A way to pass data to the server as part of a GET request
# JSON is javascript object notation


import requests

response = requests.get('https://icanhazdadjoke.com/search',
                        headers  = {"Accept": "application/json"},
                        params={"term":"cat"}
                        )

print(response.json())



