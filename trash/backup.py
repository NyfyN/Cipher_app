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
        self.decode_cipher = AES.new(self.key, AES.MODE_EAX, nonce=self.decode_cipher.nonce)
        self.plaintext = self.decode_cipher.decrypt(ciphertext)
        return self.plaintext.decode('ascii')

    def AES_print(self, ciphertext: str):
        return (str(binascii.hexlify(ciphertext),'ascii'))

#AES_instace = ciphers.AES.AES_Cipher()

#ciphers.AES.AES_Cipher().AES_encode(b'Lorem')     ###example of a method call but against b'Lorem' must be binary value
                                                     #of textbox.get()

test_value = AES_Cipher().AES_encode(b'Lorem')
test_decode = AES_Cipher().AES_decode(test_value)
print(test_decode)