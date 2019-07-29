import re
import requests
import base64
import binascii
import json
from urllib.parse import unquote
import codecs

level = 11
creds = ('natas11','U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK')
url   = 'http://natas%s.natas.labs.overthewire.org/' % level

session = requests.Session()
response = session.get(url,auth=creds)
data = response.text

cookie1 = re.findall('<Cookie data=(.*) for',str(response.cookies))[0]
cookie1 = unquote(unquote(cookie1))
cookie1 = base64.b64decode(cookie1)
cookie1 = binascii.hexlify(cookie1)

print(cookie1)

default = '{"showpassword":"no","bgcolor":"#ffffff"}'
cookie2 = binascii.hexlify(default.encode())

print(cookie2)

key = hex(int(cookie1,16)^int(cookie2,16))

print("Key => " + key[2::])

print("Key => " + codecs.decode(key[2::],"hex").decode('ascii'))

"""
<?php

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    echo base64_encode($outText);
}
$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
xor_encrypt(json_encode($defaultdata))

?>

"""


#new_cookies = '{"showpassword":"yes","bgcolor":"#ffffff"}'
new_cookies = {'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}
formdata = {'bgcolor':'#ffffff','submit':'submit'}

session2 = requests.Session()
response2 = session2.get(url,auth=creds,cookies=new_cookies,data=formdata)
data = response2.text

print(re.findall('The password for natas12 is (.*)\n',data))

