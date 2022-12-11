
def encrypt_сaesar(k, m: str):
    encrypt_str = ''
    for char in m:
        if ord(char) + k > 122:
            new_char = chr(ord(char) - 26 + k)

        else:
            new_char = chr(ord(char)+k)

        encrypt_str += new_char

    print(encrypt_str)


def decrypt_сaesar(k, c: str):
    decrypt_str = ''
    for char in c:
        if ord(char) - k > 122:
            new_char = chr(ord(char) - 26 - k)

        else:
            new_char = chr(ord(char) - k)

        decrypt_str += new_char

    print(decrypt_str)


encrypt_сaesar(5,'kirill')
decrypt_сaesar(5, 'pnwnqq')