import base64


string = b'Hello, World!'
encode = base64.b64encode(string)
print(encode)

decoded = base64.b64decode(encode)
print(decoded)