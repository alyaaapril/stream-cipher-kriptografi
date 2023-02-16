import base64

str = 'apa kabar'
print('Encode to Base64 with utf-8 :')
b = base64.b64encode(bytes(str, 'utf-8')) # b'YXBhIGthYmFy'
base64_str = b.decode('utf-8') # YXBhIGthYmFy
print(base64_str)
print('Decode to String with utf-8 :')
encoding = base64_str
b = base64.b64decode(encoding) # b'apa kabar'
b = b.decode('utf-8') #'apa kabar'
print(b)

str = 'ê¾©ä¬%◄s'
print('Encode to Base64 with utf-8 :')
b = base64.b64encode(bytes(str, 'utf-8')) # b'w6rCvsKpw6TCrCXil4Rz'
base64_str = b.decode('utf-8') # w6rCvsKpw6TCrCXil4Rz
print(base64_str)
print('Decode to String with utf-8 :')
encoding = base64_str
b = base64.b64decode(encoding) # b'ê¾©ä¬%◄s'
b = b.decode('utf-8') #'ê¾©ä¬%◄s'
print(b)