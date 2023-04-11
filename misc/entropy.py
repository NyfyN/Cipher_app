import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_entropy_from_file(filename):
    # Read the bytes of the file
    with open(filename, 'rb') as f:
        data = f.read()

    # Calculate the frequency of occurrence of each byte
    freqs = {}
    for byte in data:
        freqs[byte] = freqs.get(byte, 0) + 1

    # Calculate the entropy of each byte value
    entropies = []
    for byte in freqs:
        freq = freqs[byte] / len(data)
        if freq > 0:
            entropies.append(-freq * math.log(freq, 2))
        else:
            entropies.append(0)
    while len(entropies) < 256:
        entropies.append(0)

    # Create a histogram with colored bars
    colors = np.linspace(0, 1, 256)
    fig, ax = plt.subplots()
    ax.bar(range(256), entropies, color=plt.cm.viridis(colors))
    ax.set_title(f"Entropy chart for the file {filename}")
    ax.set_xlabel('Byte value')
    ax.set_ylabel('Entropy (bits)')
    # plt.show()
    # Return the plot object
    return fig

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
    #plt.show()
    return fig

