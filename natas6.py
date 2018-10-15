#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

# headers = { "Referer" : "http://natas5.natas.labs.overthewire.org/" }
# cookies = { "loggedin" : "1" }

url = 'http://%s.natas.labs.overthewire.org/' % username

# response = requests.get(url, auth = (username, password), headers = headers )
# response = session.get(url, auth = (username, password), cookies = cookies )

session = requests.Session()
# response = session.get(url + "index-source.html", auth = (username, password) )
response = session.post(url, data = {"secret": "FOEIUWGHFEEUHOFUOIU", "submit":"submit"}, auth = (username, password) )

content = response.text

# print content

print re.findall(' natas7 is (.*)', content)[0]
