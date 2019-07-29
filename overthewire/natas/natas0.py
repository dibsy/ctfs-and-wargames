import re
import requests

#/etc/natas_webpass/natas11
level = 0
creds = ('natas0','natas0')
url   = 'http://natas%s.natas.labs.overthewire.org' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text
print(re.findall('The password for natas1 is (.*) -->',data))