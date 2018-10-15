#!/usr/bin/env python

import requests
import re

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
response = session.post(url, data = {"secret": "oubWYf2kBq", "submit":"submit" }, auth = (username, password) )

content = response.text

# print content

print re.findall('natas9 is (.*)', content)[0]