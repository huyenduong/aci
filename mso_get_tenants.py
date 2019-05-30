import requests
import sys
import json
import re
import time

# change x.y.z.t to your MSO address
# your_password is your MSO password
base_url = "https://x.y.z.t/api/v1/"
payload = "{\n    \"username\": \"admin\",\n    \"password\": \"your_password\"\n}"
bearer = ""
access_token = ""
headers = {
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
           #'Host': "10.66.124.9",
            'accept-encoding': "gzip, deflate",
            'content-length': "59",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

# Get login token
def getToken():
    # Getting the oauth token first.
    try:
        url = base_url + "auth/login"
        response = requests.request("POST", url, data=payload, headers=headers, verify=False)
        token = json.loads(response.text)
        return token

    except:
        print 'Bad token generation'
        sys.exit()

# Get tenant information
token = getToken()
access_token = str(token["token"])

def getTenant():
    bearer = "Bearer" + " " + access_token
    headers['Authorization'] = bearer
    url = base_url + "tenants"
    response = requests.request("GET", url, data=payload, headers=headers, verify = False)
    tenants = json.loads(response.text)
    return tenants

data = []
longest_names = {'Tenant': len('Tenant'),
                 'ID': len('Scope')}

def check_longest_name(item, title):
    """
    Check the longest name
    :param item: String containing the name
    :param title: String containing the column title
    """
    if len(item) > longest_names[title]:
        longest_names[title] = len(item)

# start main
tenants = getTenant()
list_tenants = tenants["tenants"]

for tenant in list_tenants:
    data.append((tenant["name"], tenant["id"]))

# Display the data downloaded
template = '{0:' + str(longest_names["Tenant"]) + '} ' \
            '{1:' + str(longest_names["ID"]) + '} '

print(template.format("Tenant", "ID"))
                          
print(template.format('-' * longest_names["Tenant"],
                      '-' * longest_names["ID"]))
for rec in sorted(data):
    print(template.format(*rec))







