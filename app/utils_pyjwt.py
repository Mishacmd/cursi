import jwt
from time import sleep
import datetime

JWT_SECRET = 'idk_how_to_name_secret_so_let\'s_just_make_it_a_super_secret'

payload = {
    "sub": '4545',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=60),

    "userName": 'Misha',
    'age': 13,
    'is_admin': True
}

encode_jwt = jwt.encode(
    payload=payload,
    key=JWT_SECRET,
    algorithm='HS256'
)
print(encode_jwt)

decode = jwt.decode(
    jwt=encode_jwt,
    key=JWT_SECRET,
    algorithms=['HS256'],
    
)

print(decode)