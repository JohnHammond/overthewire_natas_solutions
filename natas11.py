#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import urllib
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )
cookies = { "data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK" }
response = session.get(url, auth = (username, password), cookies = cookies )


# print base64.b64decode(urllib.unquote(session.cookies['data'])).encode('hex')


content = response.text


print content