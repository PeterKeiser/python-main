# requests_and_parammes

# https://www.google.com/search?

# q=american+marten
# rlz=1C1CHBF_en-GBGB977GB977
# oq=american+marten
# aqs=chrome..69i57j46i512j0i512l5j46i512j0i512l2.4901j0j15&sourceid=chrome&ie=UTF-8


# import requests

# response = requests.get(
#     "https://example.com?key1=value1&key2=value2"
# )


# import requests
# response = requests.get(
#     "https://example.com",
#     params={
#         "key1": "value1",
#         "key2": "value2"
#     }
# )



import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params = {"term": "cat", "limit": 1}
)

data = response.json()

# print(type(data))
print(data["results"])
# print(data["joke"])
# print(f"status: {data['status']}")






