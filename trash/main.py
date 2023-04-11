# import math
# import matplotlib.pyplot as plt
# import subprocess

# # Wczytaj zaszyfrowany plik
# with open('PS2_PROJEKT_MD_MT.zip', 'rb') as f:
#     data = f.read()

# # Oblicz entropię w bajtach
# def byte_entropy(byte_string):
#     entropy = 0
#     for byte in range(256):
#         frequency = float(byte_string.count(bytes([byte]))) / len(byte_string)
#         if frequency > 0:
#             entropy += - frequency * math.log(frequency, 2)
#     return entropy

# # Oblicz entropię każdego bajtu w pliku
# entropies = [byte_entropy(data[i:i+1]) for i in range(len(data))]

# # Wygeneruj histogram entropii
# plt.hist(entropies, bins=256)
# plt.xlabel('Entropia')
# plt.ylabel('Liczba wystąpień')
# plt.show()


import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


root = ctk.CTk()
root.geometry("800x600")

# Główna ramka
main_frame = ctk.CTkFrame(root, width=800, height=600)
main_frame.pack(fill="both", expand=True)

# Pierwsza ramka z polami tekstowymi
text_frame1 = ctk.CTkFrame(main_frame )
text_frame1.grid(row=0, column=0, rowspan=2, sticky="nsew")

# Umieszczanie widgetów w pierwszej ramce
text1 = ctk.CTkLabel(text_frame1 )
text1.pack(fill="both", expand=True)

text2 = ctk.CTkLabel(text_frame1 )
text2.pack(fill="both", expand=True)

# Druga ramka z polami tekstowymi
text_frame2 = ctk.CTkFrame(main_frame )
text_frame2.grid(row=0, column=1, rowspan=2, sticky="nsew")

# Umieszczanie widgetów w drugiej ramce
text3 = ctk.CTkLabel(text_frame2 )
text3.pack(fill="both", expand=True)

text4 = ctk.CTkLabel(text_frame2 )
text4.pack(fill="both", expand=True)

# Trzecia ramka z wykresem
graph_frame = ctk.CTkFrame(main_frame )
graph_frame.grid(row=0, column=2, rowspan=2, sticky="nsew")

# Tworzenie wykresu i umieszczenie go w ramce
fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).plot([1, 2, 3, 4], [10, 20, 30, 40])

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

toolbar = NavigationToolbar2Tk(canvas, graph_frame)
toolbar.update()
canvas.get_tk_widget().pack(fill="both", expand=True)

root.mainloop()

