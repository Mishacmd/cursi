import jwt
import time
import datetime

JWT_SECRET = 'idk_how_to_name_secret_so_let\'s_just_make_it_a_super_secret'
NOT_SECRET = 'qwerty123456'
payload = {
    "sub": '4545',
    "iat": datetime.datetime.now(datetime.UTC),
    "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=60),

    "surname": 'Nedogonov',
    'group': 25082026,
    'subject': 'довільне значення' 
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

try:
    decode2 = jwt.decode(
        jwt=encode_jwt,
        key=NOT_SECRET,
        algorithms=['HS256'],  
        )

    print(decode2)
except jwt.InvalidSignatureError:
    print('Invalid secret')

try:
    time.sleep(60)

    decode3 = jwt.decode(
        jwt=encode_jwt,
        key=JWT_SECRET,
        algorithms=['HS256'],  
        )

    print(decode3)
except jwt.ExpiredSignatureError:
    print('Token has expired')
