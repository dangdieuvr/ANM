from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt(encrypted_text, key, iv):
    try:
        # Decode the base64-encoded cipher text and IV
        cipher_text = base64.b64decode(encrypted_text)
        iv_bytes = base64.b64decode(iv)

        # Create a cipher object with the key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv_bytes)

        # Decrypt the text and unpad it
        decrypted_text = unpad(cipher.decrypt(cipher_text), AES.block_size)

        # Return the decoded plaintext
        return decrypted_text.decode('utf-8')
    except Exception as e:
        print(f"Error during decryption: {e}")
        return None