from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode

def pad(text):
    # Ensure input is bytes
    if isinstance(text, str):
        text = text.encode('utf-8')
    # Padding for AES block size
    padding = AES.block_size - len(text) % AES.block_size
    return text + bytes([padding] * padding)

def encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text))
    iv = b64encode(cipher.iv).decode('utf-8')
    encrypted_text = b64encode(cipher_text).decode('utf-8')
    return f"IV: {iv}\nEncrypted Text: {encrypted_text}"