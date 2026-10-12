import hashlib


data = 'hi'.encode()
print(data)

hash_md5 = hashlib.md5(data).hexdigest()
print(hash_md5)


user_pass = 'hi'.encode()
hash_user_pass = hashlib.md5(user_pass).hexdigest()
if hash_user_pass == hash_md5:
    print('Password is correct')