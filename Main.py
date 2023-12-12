from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, END
from Encrypt import  encrypt
from Decrypt import  decrypt

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("AES Encryption App")

        self.label = Label(master, text="Enter Text:")
        self.label.pack()

        self.text_entry = Entry(master, width=40)
        self.text_entry.pack()

        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack()

        self.result_label = Label(master, text="Result:")
        self.result_label.pack()

        self.result_text = Text(master, height=5, width=40, wrap="word")
        self.result_text.pack()

        self.scrollbar = Scrollbar(master, command=self.result_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=self.scrollbar.set)

        # Generate a random key for encryption and decryption
        self.key = get_random_bytes(AES.block_size)

    def encrypt_text(self):
        plain_text = self.text_entry.get()
        encrypted_text = encrypt(plain_text, self.key)
        self.display_result(encrypted_text)

        # Automatically decrypt the encrypted text
        decrypted_text = decrypt(encrypted_text, self.key)
        self.display_result(decrypted_text)

    def decrypt_text(self):
        encrypted_text = self.text_entry.get()
        decrypted_text = decrypt(encrypted_text, self.key)
        self.display_result(decrypted_text)

    def display_result(self, result):
        self.result_text.delete(1.0, END)
        self.result_text.insert(END, result)

if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.mainloop()