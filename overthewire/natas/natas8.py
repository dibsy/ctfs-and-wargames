import re
import requests
import binascii
import base64

level =  8
creds = ('natas8','DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text



encodedSecret = '3d3d516343746d4d6d6c315669563362'
Hex2Bin = binascii.unhexlify(encodedSecret)
Reverse_String = Hex2Bin[::-1]
Base64 = base64.b64decode(Reverse_String)

formdata = {'secret':'oubWYf2kBq','submit':'submit'}

response = session.post(url,auth=creds,data=formdata)
data = response.text

print(re.findall('The password for natas9 is (.*)',data))