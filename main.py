import sys
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from screeninfo import get_monitors
import winreg
#from entropy import calculate_entropy
from ciphers.AES import AES_Cipher, AES_instance
from ciphers.MD5 import MD5_hash
from ciphers.RSA import RSA_encrypt, RSA_decrypt
from ciphers.BWS import BWS_encrypt, BWS_decrypt
import misc.browse_file as bf
import misc.entropy as entropy


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("dark-blue") # Modes: "blue", "dark-blue", "green" 
        self.click_counter = 0
        
        # -------------------------------------------- CONFIGURE WINDOW
        self.title("Crypto")
        self.width = get_monitors()[0].width-500
        self.height = get_monitors()[0].height-150
        self.geometry(f"{self.width}x{self.height}+0+0") # grid 4x4
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.style = ttk.Style()
        # -------------------------------------------- FRAMES 

        self.generate_main_frame()
        self.generate_left_frame()
        #self.chart_generate()



    def test(self):
        self.command()
    
    def command(self):
        ciphers = ["AES","MD5","RSA","ECC","BWS","QKD","HME"]
        if self.cipher_selection_variable.get() in ciphers:
            if self.cipher_selection_variable.get() == "AES":
                print("AES")
                self.encrypted_data = AES_instance.AES_encode(bytes(self.plaintext_textbox.get('1.0','end'),'ascii'))
                self.decrypted_data = AES_instance.AES_decode(self.encrypted_data)
                if self.decrypted_data:
                    self.decrypt_print()
            elif self.cipher_selection_variable.get() == "MD5":
                print("MD5")
                self.encrypted_data = MD5_hash(self.plaintext_textbox.get('1.0','end'))
            elif self.cipher_selection_variable.get() == "RSA":
                print("RSA")
                self.encrypted_data = RSA_encrypt(self.plaintext_textbox.get('1.0','end'))
            elif self.cipher_selection_variable.get() == "ECC":
                print("ECC (#TODO)")
                pass
            elif self.cipher_selection_variable.get() == "BWS":
                print("BWS")
                self.encrypted_data = BWS_encrypt(bytes(self.plaintext_textbox.get('1.0','end'),'ascii'))
        else:
             tk.messagebox.showerror(title="Błąd szyfrowania", message="Nie wybrano żadnego szyfru!")
        if self.entropy_checkbox.get() == 1:
            self.entropy_from_textbox()

    def generate_left_frame(self):
        self.left_frame = ctk.CTkFrame(self, height=self.height, width=self.width/5)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nswe")
        self.left_frame.grid_propagate(False)




        # -------------------------------------------- RADIO BUTTONS VARIABLES
        # self.cipher_1_AES_variable = ctk.StringVar()
        # self.cipher_2_MD5_variable = ctk.StringVar()
        # self.cipher_3_RSA_variable = ctk.StringVar()
        # self.cipher_4_ECC_variable = ctk.StringVar()
        # self.cipher_5_BWS_variable = ctk.StringVar()
        # self.cipher_6_QKD_variable = ctk.StringVar()
        # self.cipher_7_HME_variable = ctk.StringVar()
        self.cipher_selection_variable = ctk.StringVar()


        # -------------------------------------------- LEFT_FRAME BUTTONS
        self.title = ctk.CTkLabel(self.left_frame, text="CryptoProject", font=("Consolas",32))
        self.title.grid(row=0, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_1_AES = ctk.CTkRadioButton(self.left_frame, text="AES", 
                                               variable=self.cipher_selection_variable,
                                               value="AES")
        self.cipher_1_AES.grid(row=1, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_2_MD5 = ctk.CTkRadioButton(self.left_frame, text="MD5", 
                                               variable=self.cipher_selection_variable,
                                               value="MD5")
        self.cipher_2_MD5.grid(row=2, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_3_RSA = ctk.CTkRadioButton(self.left_frame, text="RSA", 
                                               variable=self.cipher_selection_variable,
                                               value="RSA")
        self.cipher_3_RSA.grid(row=3, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_4_ECC = ctk.CTkRadioButton(self.left_frame, text="ECC", 
                                               variable=self.cipher_selection_variable,
                                               value="ECC")
        self.cipher_4_ECC.grid(row=4, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_5_BWS = ctk.CTkRadioButton(self.left_frame, text="Blowfish", 
                                               variable=self.cipher_selection_variable,
                                               value="BWS")
        self.cipher_5_BWS.grid(row=5, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_6_QKD = ctk.CTkRadioButton(self.left_frame, text="QKD", 
                                               variable=self.cipher_selection_variable,
                                               value="QKD")
        self.cipher_6_QKD.grid(row=6, column=0,padx=20, pady=20, sticky="nswe")
        self.cipher_7_HME = ctk.CTkRadioButton(self.left_frame, text="Homomorphic Encryption", 
                                               variable=self.cipher_selection_variable,
                                               value="HME")
        self.cipher_7_HME.grid(row=7, column=0,padx=20, pady=20, sticky="nswe")

        self.entropy_checkbox = ctk.CTkCheckBox(self.left_frame, text="Entropy diagram")
        self.entropy_checkbox.grid(row=8, column=0,padx=20, pady=20, sticky="nswe")
        

        self.encrypt_btn = ctk.CTkButton(self.left_frame, text="Encrypt",command=self.command)
        self.encrypt_btn.grid(row=15, column=0,padx=20, pady=20, sticky="nsew")

        self.file_options_label = ctk.CTkLabel(self.left_frame, text="File options")
        self.file_options_label.grid(row=16,column=0, padx=20, pady=10, sticky="nsew")

        self.save_btn = ctk.CTkButton(self.left_frame,text="Save file as", command=self.save_file)
        self.save_btn.grid(row=17, column=0, padx=20, pady=10, sticky="nsew")

        self.open_btn = ctk.CTkButton(self.left_frame,text="Open file", command=self.entropy_from_file)
        self.open_btn.grid(row=18, column=0, padx=20, pady=10, sticky="nsew")


        self.appearance_mode_label = ctk.CTkLabel(self.left_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=19,column=0,padx=20,pady=5)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.left_frame, values=["Light", "Dark", "System"],
                                                                       command=self.test)
        self.appearance_mode_optionemenu.grid(row=20,column=0,padx=20, pady=5, sticky="nswe")
        self.appearance_mode_optionemenu.set("System")

    def generate_main_frame(self):   #710,710,645   -------> plaintext and encrypted text
        self.main_frame = ctk.CTkFrame(self, height=self.height, width=self.width)
        self.main_frame.grid(row=0, column=1,padx=20, pady=20, sticky="nswe")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.entropy_frame = ctk.CTkFrame(self,height=self.height, width=self.width/3)
        self.entropy_frame.grid(row=0, column=2, sticky="e")

        # -------------------------------------------- PLAINTEXT
        self.plaintext_frame = ctk.CTkFrame(self.main_frame)
        self.plaintext_frame.grid(row=0, column=0,padx=20, pady=(50,1), sticky="nw")
        self.plaintext_label = ctk.CTkLabel(self.plaintext_frame, text="Plaintext", font=('Consolas', 20))
        self.plaintext_label.grid(row=0, column=0,padx=20, pady=5, sticky="nw")
        self.plaintext_textbox = ctk.CTkTextbox(self.plaintext_frame, height=self.height/3, width= self.width/3,
                                                font=('Consolas', 20))
        self.plaintext_textbox.grid(row=1, column=0,padx=20, pady=5, sticky="nw")

        # -------------------------------------------- DECRYPTED
        self.decrypted_frame = ctk.CTkFrame(self.main_frame, height=self.height, width= self.width)
        self.decrypted_frame.grid(row=1, column=0,padx=20, pady=10, sticky="nw")
        self.decrypted_label = ctk.CTkLabel(self.decrypted_frame, text="Decrypted", font=('Consolas', 20))
        self.decrypted_label.grid(row=0, column=0,padx=20, pady=5, sticky="nw")
        self.decrypted_field = ctk.CTkLabel(self.decrypted_frame, text="", font=('Consolas', 20),
                                            width= self.width/3, height=self.height/3)
        self.decrypted_field.grid(row=1, column=0,padx=20, pady=5, sticky="nw")



    def entropy_from_textbox(self):
        print("sduiofhgosduihfg")
        try:
            self.figure = entropy.calculate_entropy_from_line(self.encrypted_data)
            self.chart = FigureCanvasTkAgg(self.figure, self.entropy_frame)
            self.chart.get_tk_widget().grid(row=0, column=0, sticky="nsew")
            plt.close()
        except AttributeError as e:
            tk.messagebox.showerror(title="Błąd danych", message="Nie podano danych lub nie wybrano szyfru!")

    def entropy_from_file(self):
        try:
            self.figure = entropy.calculate_entropy_from_file(bf.open_file())
            self.chart = FigureCanvasTkAgg(self.figure, self.entropy_frame)
            self.chart.get_tk_widget().grid(row=0, column=0, sticky="nsew")
            plt.close()
        except AttributeError as e:
            tk.messagebox.showerror(title="Błąd danych", message="Nie wczytano pliku lub nie wybrano szyfru!")
        except FileNotFoundError as f_error:
            print("")


    def save_file(self):
        #bf.save_file(AES_instance.AES_encode(bytes(self.plaintext_textbox.get('1.0','end'),'ascii')))
        bf.save_file(self.encrypted_data)

    def decrypt_print(self): #TODO zawijanie tekstu
        print("AAAAAAA")
        self.decrypted_field = ctk.CTkLabel(self.decrypted_frame, text=self.decrypted_data, font=('Consolas', 20),
                                width= self.width/3, height=self.height/3, wraplength=self.width/3)
        self.decrypted_field.grid(row=1, column=0,padx=20, pady=5, sticky="nwse")
        # scrollbar = tk.Scrollbar(self.decrypted_frame, orient="vertical", command=self.decrypted_field.yview)
        # scrollbar.pack(side="right", fill="y")
def main():
    app = App()
    app.mainloop()
if __name__ == "__main__":
    main()
