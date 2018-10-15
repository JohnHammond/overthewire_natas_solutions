#!/usr/bin/env python

import requests
import re

username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

reponse = requests.get(url, auth = (username, password))
content = reponse.text

# print content

print re.findall('natas4:(.*)', content)[0]
