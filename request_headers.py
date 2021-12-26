# request_headers


# import requests

# response = requests.get(
#     "http://www.example.com",
#     headers={
#         "header1": "value1",
#         "header2": "value2"
#     }
# )


# import requests
# url = "https://icanhazdadjoke.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})
# print(response.text)


# import requests
# url = "https://www.google.com/"

# response = requests.get(url, headers={"Accept": "text/plain"})
# print(response.text)


import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
# print(type(response.text))
data = response.json()

print(type(data))
print(data)
print(data["joke"])
print(f"status: {data['status']}")







