import re
import requests

level = 1
creds = ('natas1','gtVrDuiDfck831PqWsLEZy5gyDz1clto')
url = 'http://natas%s.natas.labs.overthewire.org' % level
session = requests.Session()
response = requests.get(url,auth=creds)
data = response.text
print(re.findall('The password for natas2 is (.*) -->',data))