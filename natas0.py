#!/usr/bin/env python

import requests
import re

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org' % username

reponse = requests.get(url, auth = (username, password))
content = reponse.text

print re.findall('<!--The password for natas1 is (.*) -->', content)[0]