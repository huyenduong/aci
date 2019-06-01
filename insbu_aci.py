#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import json
import re
import time

def getToken(ipaddress,username,password):
    url = "https://" + ipaddress + "/api/v1/auth/login"
    data = {
        "username": username,
        "password": password
    }  
    payload = json.dumps(data)
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'accept-encoding': "gzip, deflate",
        'content-length': "59",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    token = json.loads(response.text)
    return token

