import pyotp
import qrcode
import base64


key = 'super_mega_tetra_secret'

secret = base64.b32encode(key.encode())

totp = pyotp.TOTP(secret)

uri = totp.provisioning_uri(name='Misha', issuer_name='Cursi', image='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaDZraHuFfzkctNTb0AUBWNkj3X-n_4RI_s387dDx0kQ&s=10')

print(uri)

qr = qrcode.make(uri)
qr.show()
