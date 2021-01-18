import requests
import os
import sys
import json


from requests.structures import CaseInsensitiveDict

url = "https://5pnb424p5899tsf0.myfritz.net:8443/index.php/login?redirect_url=/ocs/v2.php/apps/serverinfo/api/v1/info?format=json"

headers = CaseInsensitiveDict()
headers["Authorization"] = "Basic YWRtaW5pc3RyYXRvci1uZXh0Y2xvdWQ6Z2VnZWtpa3V3b2ph"


resp = requests.get(url, headers=headers, verify=False)

data = resp.content

encoded_data = json.loads(data)

#print(resp.status_code)
#print(resp.content)

# load json data to variables 
nextcloud_ver = encoded_data["ocs"]["data"]["nextcloud"]["system"]["version"]
ram_free = encoded_data["ocs"]["data"]["nextcloud"]["system"]["mem_free"]
ram_total = encoded_data["ocs"]["data"]["nextcloud"]["system"]["mem_total"]
php_server_ver =
db_version = 
db_size =
active_users_1h =
num_users = 


# print out the variables
print("Nextcloud Version: {}".format(nextcloud_ver))
print("Arbeitsspeicher frei: {}".format(ram_free))
print("Arbeitsspeicher total: {}".format(ram_total))
print("Auslastung RAM: {:.2f}%".format(1 - (ram_free / ram_total)))


app_updates_available = encoded_data