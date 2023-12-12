from Crypto.Cipher import AES
from base64 import b64decode


def decrypt(encrypted_text, key):
    parts = encrypted_text.split("\n")
    iv = b64decode(parts[0].split(": ")[1])
    cipher_text = b64decode(parts[1].split(": ")[1])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher.decrypt(cipher_text).rstrip(b'\0').decode('utf-8')
    return decrypted_text
