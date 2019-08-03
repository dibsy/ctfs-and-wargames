import re
import requests

level = 20
creds = ('natas20','eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
url   = 'http://natas%s.natas.labs.overthewire.org/index-source.html' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

print(data)