import requests
from datetime import datetime
import manager as mg

TOKEN = mg.TOKEN
USERNAME = mg.USERNAME
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

grap_config = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=grap_config, headers=headers)
# print(response.text)
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = datetime.now()
yesterday = datetime(year=2024, month=2, day=5)
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7.5"
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
update_pixel_endpoint = f"{post_pixel_endpoint}/{yesterday.strftime('%Y%m%d')}"
new_pixel = {
    "quantity": "10.2"
}
# response = requests.put(url=update_pixel_endpoint, json=new_pixel, headers=headers)
# print(response.text)

delete_pixel_endpoint = update_pixel_endpoint

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)