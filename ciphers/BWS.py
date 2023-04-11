from Crypto.Cipher import Blowfish
from Crypto import Random
import base64
import os

key = os.urandom(16)

def BWS_encrypt(message, key=key):
    """Funkcja szyfrująca wiadomość za pomocą klucza"""
    iv = Random.new().read(Blowfish.block_size)
    cipher = Blowfish.new(key, Blowfish.MODE_EAX, iv)
    return base64.b64encode(iv + cipher.encrypt(message))


def BWS_decrypt(ciphertext, key=key):
    """Funkcja odszyfrowująca wiadomość za pomocą klucza"""
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_EAX, iv)
    plaintext = cipher.decrypt(ciphertext[Blowfish.block_size:])
    return plaintext.rstrip(b"\0")

