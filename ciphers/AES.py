from Crypto.Cipher import AES
import os
import binascii

class AES_Cipher():
    def __init__(self):
        super().__init__()
        self.key = os.urandom(16)

    def AES_encode(self, plaintext: str):
        self.cipher = AES.new(self.key, AES.MODE_EAX)
        self.ciphertext, self.tag = self.cipher.encrypt_and_digest(plaintext)
        return self.ciphertext


    def AES_decode(self, ciphertext: str):
        self.cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.cipher.nonce)
        self.plaintext = self.cipher.decrypt(ciphertext)
        return self.plaintext.decode('ascii')

    def AES_print(self, ciphertext: str):
        return (str(binascii.hexlify(ciphertext),'ascii'))



AES_instance = AES_Cipher()
# cipher_text = cipher_test.AES_encode(b'Lorem')
# print(cipher_text)
# c = cipher_test.AES_print(cipher_text)
# print(c)
# print(cipher_test.AES_decode(cipher_text))
# hex_data = binascii.hexlify(cipher_text)
# string_data = str(hex_data,'ascii')
# print(string_data)
# plain_text = cipher_test.AES_decode(cipher_text)
# print(plain_text.decode('ascii'))