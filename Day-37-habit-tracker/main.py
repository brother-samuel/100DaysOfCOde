import requests

USERNAME = "mrunderbald"
TOKEN = "kuga76iugfkja3e69r4eysi"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": "kuga76iugfkja3e69r4eysi",
    "username": "mrunderbald",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "min",
    "type": "float",
    "color": "sora",    
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response = requests.post(url=graph_endpoint, params=graph_params, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_params = {
    "date": "20250713",
    "quantity": "25",
}

pixel = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(pixel.text)