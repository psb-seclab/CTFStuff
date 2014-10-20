#!/usr/bin/env python
# razor4x - tasteless
import requests,re
url="http://asis-ctf.ir:12443"
r=requests.Session()
for j in range(40):
	for i in range(8):
		c=r.post(url+"/send",data={'first':'0', 'second':'0'})
		print c.content
	c=r.get(url+"/")
	g=re.search('level (.+?)<', c.content)
	print g.group(1)