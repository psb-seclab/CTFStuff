

import requests

# test get
r = requests.get('https://api.github.com/events')
print type(r)
print r.encoding
print r.content
print r.status_code
print r.headers
#for entry in r.json():
#	print entry
#print r.text.encode('utf-8')

# test post
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text
print 20*'=='

