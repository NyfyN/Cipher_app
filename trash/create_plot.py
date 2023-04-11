import os
import math
import numpy as np
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
import pyaes

key = os.urandom(16)
def AES_encrypt(plaintext,key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def AES_decrypt(ciphertext,key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext[16:])
    return plaintext


def create_histogram(file):
    # Load the encrypted file
    # with open(filename, 'rb') as f:
    #     ciphertext = f.read()

    # # Set the key and mode
    
    # mode = AES.MODE_EAX

    # # Create an AES cipher object and decrypt the data
    # cipher = AES.new(key, mode, nonce=ciphertext[:16])
    #plaintext = cipher.decrypt(ciphertext[16:])

    # Calculate the entropy of each byte in the plaintext
    entropies = []
    for byte in range(256):
        freq = float(plaintext.count(byte)) / len(plaintext)
        entropies.append(-freq * math.log(freq, 2))

    # Create a histogram with colored bars
    colors = np.linspace(0, 1, 256)
    fig, ax = plt.subplots()
    ax.bar(range(256), entropies, color=plt.cm.viridis(colors))
    ax.set_xlabel('Byte value')
    ax.set_ylabel('Entropy (bits)')

    # Return the plot object
    return fig

print(AES_encrypt("LOREM"))
print