import os
import math
import numpy as np
import matplotlib.pyplot as plt
from Crypto.Cipher import AES

def entropy():
    # Ścieżka do pliku wejściowego
    input_file = './trash/lorem.txt'

    # Ścieżka do pliku wyjściowego
    output_file = 'output.txt'

    # Klucz szyfrowania
    key = os.urandom(16)

    # Utwórz obiekt szyfrujący
    cipher = AES.new(key, AES.MODE_EAX)

    # Otwórz plik wejściowy
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Zaszyfruj plik
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return ciphertext, tag

def create_char(file,cipher)
    # Zapisz zaszyfrowany plik
    with open(file, 'wb') as f:
        [f.write(x) for x in (cipher.nonce, tag, ciphertext)]

    # Oblicz entropię pliku
    with open(file, 'rb') as f:
        data = f.read()
        entropy = 0
        for byte in data:
            p = data.count(byte) / len(data)
            if p > 0:
                entropy -= p * math.log2(p)

    # Wyświetl entropię
    print(f'Entropia pliku wynosi: {entropy:.2f}')

    # Stwórz histogram entropii
    bins = np.linspace(0, 8, 50)
    hist = plt.hist(list(data), bins=bins, alpha=0.5, color='b')
    plt.xlabel('Wartość bajtu')
    plt.ylabel('Poziom entropii')
    plt.title('Histogram entropii zaszyfrowanego pliku')


