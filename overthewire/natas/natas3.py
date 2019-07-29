import re
import requests

level = 3
creds = ('natas3','sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14')
url = 'http://natas%s.natas.labs.overthewire.org/s3cr3t/users.txt' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text
print(re.findall('natas4:(.*)',data))
