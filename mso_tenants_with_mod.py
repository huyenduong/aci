#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import json
import re
import time
from insbu_aci import *
bearer = ""
access_token = ""

headers = {
            'Content-Type': "application/json",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'accept-encoding': "gzip, deflate",
            'content-length': "59",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

mso_ip_address = str(raw_input("MSO IP Address:"))
mso_username = str(raw_input("MSO Username:"))
mso_password = str(raw_input("MSO Password:"))

#print(mso_ip_address)

# Get access token
print("Get acccess token:")
token = getToken(mso_ip_address,mso_username,mso_password)
print(token)
access_token = token["token"]

base_url = "https://" + mso_ip_address + "/api/v1/"

def getTenant(ipaddress,username,password):
    url = "https://" + ipaddress + "/api/v1/tenants"
    bearer = "Bearer" + " " + access_token
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        'content-length': "59",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    headers['Authorization'] = bearer
    
    data = {
        "username": username,
        "password": password
    }  
    payload = json.dumps(data)
    response = requests.request("GET", url, data=payload, headers=headers, verify = False)
    tenants = json.loads(response.text)
    return tenants

# format data
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
# end of format data

# start main
tenants = getTenant(mso_ip_address,mso_username,mso_password)
list_tenants = tenants["tenants"]

for tenant in list_tenants:
    data.append((tenant["name"], tenant["id"]))

# Display the result in data format
template = '{0:' + str(longest_names["Tenant"]) + '} ' \
            '{1:' + str(longest_names["ID"]) + '} '

print(template.format("Tenant", "ID"))
                          
print(template.format('-' * longest_names["Tenant"],
                      '-' * longest_names["ID"]))
for rec in sorted(data):
    print(template.format(*rec))