import requests
from requests.auth import HTTPBasicAuth
import base64
from Crypto.Util.number import bytes_to_long,long_to_bytes
c = HTTPBasicAuth("natas11","U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK")
header = "?bgcolor="
bgc = "%23bbbbbc"
r = requests.get("http://natas11.natas.labs.overthewire.org/",auth=c)
print(r.text)
c1 = (r.cookies.get_dict())['data']

r = requests.get("http://natas11.natas.labs.overthewire.org/"+header+bgc,auth=c)
print(r.text)
c2 = (r.cookies.get_dict())['data']

print(c1,c2)
c1 = c1[:-3]+"="
c2 = c2[:-3]+"="

c1 = base64.b64decode(c1)
c2 = base64.b64decode(c2)

d1 = c1[-9:-2]
d2 = c2[-9:-2]
p1 = b"#ffffff"
p1 = bytes_to_long(p1)
p2 = b"#bbbbbc"
p2 = bytes_to_long(p2)
aa1=(bytes_to_long(d1)^p1)
aa2 = (bytes_to_long(d2)^p2)
print(long_to_bytes(aa1))
print(long_to_bytes(aa2))

key = b"qw8J"
out = b""
for i in range(len(c1)):
    out+=chr(c1[i]^key[i%len(key)]).encode()
print(out)
out = b""
b = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
for i in range(len(b)):
    out+=chr(b[i]^key[i%len(key)]).encode()
print(base64.b64encode(out))