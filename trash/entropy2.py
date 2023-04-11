import math
import numpy as np
import matplotlib.pyplot as plt
import ciphers.AES

def calculate_entropy_from_line(ciphertext):
    # Calculate the frequency of occurrence of each byte
    freqs = {}
    for byte in ciphertext:
        freqs[byte] = freqs.get(byte, 0) + 1

    # Calculate the entropy of each byte value
    entropies = []
    for byte in freqs:
        freq = freqs[byte] / len(ciphertext)
        if freq > 0:
            entropies.append(-freq * math.log(freq, 2))
        else:
            entropies.append(0)
    while len(entropies) < 256:
        entropies.append(0)

    # Create a histogram with colored bars
    colors = np.linspace(0, 1, len(entropies))
    colors = np.resize(colors, (256,))
    fig, ax = plt.subplots()
    ax.bar(range(256), entropies, color=plt.cm.viridis(colors))
    ax.set_title("Entropy chart for the ciphertext")
    ax.set_xlabel('Byte value')
    ax.set_ylabel('Entropy (bits)')
    plt.show()


# test_text = ciphers.AES.AES_instance.AES_encode(b"Hello World!")
# test_decode = ciphers.AES.AES_instance.AES_decode(test_text)
# calculate_entropy_from_line(test_text)