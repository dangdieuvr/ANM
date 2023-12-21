from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt(text, key):
    # Generate a random IV (Initialization Vector)
    iv = AES.new(key, AES.MODE_CBC).iv

    # Create a cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the text and encrypt it
    padded_text = pad(text.encode('utf-8'), AES.block_size)
    encrypted_text = cipher.encrypt(padded_text)

    # Return a tuple containing the encrypted text and IV
    return base64.b64encode(encrypted_text).decode('utf-8'), base64.b64encode(iv).decode('utf-8')