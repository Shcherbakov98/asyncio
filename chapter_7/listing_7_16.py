"""Хеширование паролей с помощью алгоритма scrypt"""
import hashlib
import os
import string
import time
import random


def random_password(length: int) -> bytes:
    ascii_lowercase = string.ascii_lowercase.encode()  # b'abcdefghijklmnopqrstuvwxyz'
    return b''.join(bytes(random.choice(ascii_lowercase)) for _ in range(length))


passwords = [random_password(10) for _ in range(10000)]


def hash_(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


start = time.time()


for password_ in passwords:
    hash_(password_)

end = time.time()

print('total_time = ', end - start)
# total_time =  37.052085638046265
