from customtkinter import filedialog
import misc.entropy as entropy

def save_file(file_text):
    filetypes = (("All Files", "*.*"),)
    filename = filedialog.asksaveasfilename(filetypes=filetypes)
    with open(filename, 'wb') as f:
        f.write(file_text)

def open_file():
    filetypes = (("All Files", "*.*"),)
    filename = filedialog.askopenfilename(filetypes=filetypes)
    return filename