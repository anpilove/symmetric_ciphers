import random

dict = {(i - ord('a')): chr(i) for i in range(ord('a'), ord('z')+1)}
print(dict)
def encrypt_vernama(m: str):
    encrypt_str = ''
    global keys
    keys = []
    for char in m:
        key = random.randint(0,2)
        keys.append(key)
        encrypt_str += dict[(ord(char) + key - ord('a')) % len(dict)]

    print(encrypt_str)
    print('Keys encrypt',keys)
    return encrypt_str

def decrypt_vernama(c: str):
    decrypt_str = ''
    for i,char in enumerate(c):
        decrypt_str += dict[(ord(char) - keys[i] - ord('a')) % len(dict)]

    print(decrypt_str)


encrypt_word = encrypt_vernama('zzz')

decrypt_vernama(encrypt_word)