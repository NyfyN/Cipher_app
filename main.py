from src import atbash as at
from src import baconian as bc
from src import beaufort as bf
from src import cezar as cz
from src import polibiusz as pb
from src import ZB as zb
from src import transposition as tr

from tkinter import *

class CryptGUI(object):
	
	"""docstring for CryptGUI"""

	def __init__(self):
		super(CryptGUI, self).__init__()
		self.label_counter = 0
		self.root = Tk()
		self.root.title("Algorytmy kryptograficzne")
		self.draw_main_window()
		self.root.mainloop()

	def __ceasar_on_closing__(self):
		self.label_counter = 0
		self.ceasar_root.destroy()

	def __baconian_on_closing__(self):
		self.label_counter = 0
		self.ceasar_root.destroy()

	def __beaufort_on_closing__(self):
		self.label_counter = 0
		self.beaufort_root.destroy()

	def __atbash_on_closing__(self):
		self.label_counter = 0
		self.atbash_root.destroy()

	def __polybius_on_closing__(self):
		self.label_counter = 0
		self.polybius_root.destroy()

	##MAIN PROGRAM
	def draw_main_window(self):
		self.main_window_label = Label(self.root, text="Szyfry", font=("Comic Sans",72)).pack()
		self.help_btn = Button(self.root,text="?",font=("Comic Sans",20),command=self.help_window)

		##CEASAR'S CIPHER
		self.ceasar_frame = Frame(self.root)
		self.ceasar_label = Label(self.ceasar_frame,text="Szyfr Cezara",font=("Comic Sans", 45)).pack(side=LEFT)
		self.ceasar_button = Button(self.ceasar_frame,text="Kliknij...",font=("Comic Sans",35), 
			command=self.ceasar_window).pack(side=RIGHT)

		##BEAUFOURT'S CIPHER
		self.beaufort_frame = Frame(self.root)
		self.beaufort_label = Label(self.beaufort_frame,text="Szyfr Beaufort'a",font=("Comic Sans",45)).pack(side=LEFT)
		self.beaufort_button = Button(self.beaufort_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.beaufort_window).pack(side=RIGHT)

		##ATBASH CIPHER
		self.atbash_frame = Frame(self.root)
		self.atbash_label = Label(self.atbash_frame,text="Szyfr AtBash",font=("Comic Sans",45)).pack(side=LEFT)
		self.atbash_button = Button(self.atbash_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.atbash_window).pack(side=RIGHT)

		##POLYBIUS CIPHER
		self.polybius_frame = Frame(self.root)
		self.polybius_label = Label(self.polybius_frame,text="Szyfr Polibiusza",font=("Comic Sans",45)).pack(side=LEFT)
		self.polybius_button = Button(self.polybius_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.polybius_window).pack(side=RIGHT)

		##BACONIAN CIPHER
		self.baconian_frame = Frame(self.root)
		self.baconian_label = Label(self.baconian_frame,text="Szyfr Baconian",font=("Comic Sans",45)).pack(side=LEFT)
		self.baconian_button = Button(self.baconian_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.baconian_window).pack(side=RIGHT)

		##ZB CIPHER
		self.zb_frame = Frame(self.root)
		self.zb_label = Label(self.zb_frame,text="Szyfr ZB",font=("Comic Sans",45)).pack(side=LEFT)
		self.zb_button = Button(self.zb_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.zb_window).pack(side=RIGHT)
		##TRANSPOSITION CIPHER
		self.tr_frame = Frame(self.root)
		self.tr_label = Label(self.tr_frame,text="Szyfr kolumnowy",font=("Comic Sans",45)).pack(side=LEFT)
		self.tr_button = Button(self.tr_frame,text="Kliknij...",font=("Comic Sans",35),
			command=self.tr_window).pack(side=RIGHT)
		##PACK PART
		self.ceasar_frame.pack(fill=BOTH, expand=YES)
		self.beaufort_frame.pack(fill=BOTH, expand=YES)
		self.atbash_frame.pack(fill=BOTH, expand=YES)
		self.polybius_frame.pack(fill=BOTH, expand=YES)
		self.baconian_frame.pack(fill=BOTH, expand=YES)
		self.zb_frame.pack(fill=BOTH, expand=YES)
		self.tr_frame.pack(fill=BOTH, expand=YES)
		self.help_btn.pack(anchor=SE)

	def help_window(self):
		self.help_root = Tk()
		self.title_help_label = Label(self.help_root,text="POMOC",font=("Comic Sans",72))
		self.help_frame = Frame(self.help_root)
		self.help_label = Label(self.help_frame,text="""
Program testujący działanie opisanych szyfrów. 
Kliknij przycisk, a następnie wypełnij opisane pola.


Jeżeli należy podać klucz, to  zawsze jest to liczba.
Zdanie klucz, należy wpisać zdanie lub słowo.""",font=("Comic Sans",36))
		self.copyright_label = Label(self.help_root,text="v.alpha-0.1 \u00A9 2022 Mateusz Dziedzic, All rights reserved.",
			font=("Times New Roman",6))
		self.title_help_label.pack()
		self.help_frame.pack()
		self.help_label.pack()
		self.copyright_label.pack()
		self.help_root.mainloop()

	def ceasar_window(self):
		self.ceasar_root = Tk()
		self.ceasar_root.title("Szyfr Cezara")
		ceasar_entry_label = Label(self.ceasar_root, text="Podaj zdanie ",font=("Comic Sans",20))
		self.ceasar_entry = Entry(self.ceasar_root)
		self.ceasar_key_entry = Entry(self.ceasar_root)
		ceasar_key_label = Label(self.ceasar_root, text="Podaj klucz",font=("Comic Sans",20))
		ceasar_button = Button(self.ceasar_root,text="Kliknij...",font=("Comic Sans",20),command=self.ceasar_encryption)
		ceasar_entry_label.pack()
		self.ceasar_entry.pack()
		ceasar_key_label.pack()
		self.ceasar_key_entry.pack()
		ceasar_button.pack()
		self.convert_text_area = Text(self.ceasar_root,height=10,width=25,font=("Comic Sans",20))
		self.convert_text_area.tag_configure("center",justify="center")
		self.convert_text_area.pack()
		self.ceasar_root.protocol("WM_DELETE_WINDOW",self.__ceasar_on_closing__)

	def ceasar_encryption(self):
		self.convert_text_area.delete(1.0,END)
		ceasar_text = self.ceasar_entry.get()
		ceasar_key = self.ceasar_key_entry.get()
		convert_text = cz.convert(ceasar_text,int(ceasar_key))
		self.convert_text_area.tag_configure("center",justify='center')
		self.convert_text_area.insert(INSERT,"Zaszyfrowany tekst: "+convert_text)
		self.convert_text_area.tag_add("center",1.0,"end")

	def beaufort_window(self):
		self.beaufort_root = Tk()
		self.beaufort_root.title("Szyfr Beaufort'a")
		self.beaufort_entry_label = Label(self.beaufort_root, text="Podaj zdanie",font=("Comic Sans",20))
		self.beaufort_entry = Entry(self.beaufort_root)
		self.beaufort_pattern_label = Label(self.beaufort_root, text="Podaj zdanie-klucz",font=("Comic Sans",20))
		self.beaufort_shift_pattern = Entry(self.beaufort_root)
		beaufort_encryption_button = Button(self.beaufort_root,text="Szyfruj!",font=("Comic Sans",20),
			command=self.beaufort_encryption)
		self.beaufort_entry_label.pack()	
		self.beaufort_entry.pack()
		self.beaufort_pattern_label.pack()
		self.beaufort_shift_pattern.pack()
		beaufort_encryption_button.pack()
		self.convert_text_area = Text(self.beaufort_root,height=10,width=25,font=("Comic Sans",20))
		self.convert_text_area.tag_configure("center",justify="center")
		self.convert_text_area.pack()
		self.beaufort_root.protocol("WM_DELETE_WINDOW",self.__beaufort_on_closing__)

	def beaufort_encryption(self):
		self.convert_text_area.delete(1.0,END)
		beaufort_text = self.beaufort_entry.get()
		beaufort_pattern = self.beaufort_shift_pattern.get()
		convert_text = bf.encryption(beaufort_text,beaufort_pattern)
		self.convert_text_area.tag_configure("center",justify='center')
		self.convert_text_area.insert(INSERT,"Zaszyfrowany tekst: "+convert_text)
		self.convert_text_area.tag_add("center",1.0,"end")

	def atbash_window(self):
		self.atbash_root = Tk()
		self.atbash_root.title("Szyfr AtBash")
		self.atbash_entry_label = Label(self.atbash_root, text="Podaj zdanie do zaszyfrowania",font=("Comic Sans",20))
		self.atbash_entry = Entry(self.atbash_root)
		atbash_encryption_button = Button(self.atbash_root, text="Szyfruj!",font=("Comic Sans",20),command=self.atbash_encryption)
		self.atbash_text_box = Text(self.atbash_root,height=10,width=25,font=("Comic Sans",20))
		self.atbash_entry_label.pack()
		self.atbash_entry.pack()
		atbash_encryption_button.pack()
		self.atbash_text_box.pack()
		self.atbash_root.protocol("WM_DELETE_WINDOW",self.__atbash_on_closing__)

	def atbash_encryption(self):
		self.atbash_text_box.delete(1.0,END)
		self.label_counter = 0
		atbash_text = self.atbash_entry.get()
		convert_text = at.encryption(atbash_text)
		self.atbash_text_box.tag_configure("center",justify='center')
		self.atbash_text_box.insert(END,"Zaszyfrowany tekst: "+convert_text)
		self.atbash_text_box.tag_add("center",1.0,"end")

	def polybius_window(self):
		self.polybius_root = Tk()
		self.polybius_root.title("Szyfr Polibiusza")
		self.polybius_encrypt_enter_label = Label(self.polybius_root, text="Podaj zdanie do zaszyfrowania",font=("Comic Sans",20))
		self.polybius_encrypt_entry = Entry(self.polybius_root)
		polybius_encryption_button = Button(self.polybius_root, text="Szyfruj!",font=("Comic Sans",20)
			,command=self.polybius_encryption)
		self.polybius_decrypt_enter_label = Label(self.polybius_root, text="Podaj zdanie do odszyfrowania",font=("Comic Sans",20))
		self.polybius_decrypt_entry = Entry(self.polybius_root)
		polybius_decryption_button = Button(self.polybius_root, text="Deszyfruj!",font=("Comic Sans",20)
			,command=self.polybius_decryption)
		self.polybius_text_box = Text(self.polybius_root,height=10,width=25,font=("Comic Sans",20))
		self.polybius_encrypt_enter_label.pack()
		self.polybius_encrypt_entry.pack()
		polybius_encryption_button.pack()
		self.polybius_decrypt_enter_label.pack()
		self.polybius_decrypt_entry.pack()
		polybius_decryption_button.pack()
		self.polybius_text_box.pack()
		self.polybius_root.protocol("WM_DELETE_WINDOW",self.__polybius_on_closing__)

	def polybius_encryption(self):
		self.polybius_text_box.delete(1.0,END)
		self.label_counter = 0
		polybius_text = self.polybius_encrypt_entry.get()
		convert_text = pb.encryption(polybius_text)
		self.polybius_text_box.tag_configure("center",justify='center')
		self.polybius_text_box.insert(END,"Zaszyfrowany tekst: "+convert_text)
		self.polybius_text_box.tag_add("center",1.0,"end")

	def polybius_decryption(self):
		self.polybius_text_box.delete(1.0,END)
		self.label_counter = 0
		polybius_text = self.polybius_decrypt_entry.get()
		convert_text = pb.decryption(polybius_text)
		self.polybius_text_box.tag_configure("center",justify='center')
		self.polybius_text_box.insert(END,"Odszyfrowany tekst: "+convert_text)
		self.polybius_text_box.tag_add("center",1.0,"end")

	def baconian_window(self):
		self.baconian_root = Tk()
		self.baconian_root.title("Szyfr bekonowy")
		self.baconian_encrypt_enter_label = Label(self.baconian_root, text="Podaj zdanie do zaszyfrowania",font=("Comic Sans",20))
		self.baconian_encrypt_entry = Entry(self.baconian_root)
		baconian_encrypt_button = Button(self.baconian_root,text="Szyfruj",font=("Comic Sans",20),command=self.baconian_encrypt)
		self.baconian_decrypt_enter_label = Label(self.baconian_root, text="Podaj zdanie do odszyfrowania",font=("Comic Sans",20))
		self.baconian_decrypt_entry = Entry(self.baconian_root)
		baconian_decrypt_button = Button(self.baconian_root,text="Deszyfruj",font=("Comic Sans",20),command=self.baconian_decrypt)
		self.baconian_text_box = Text(self.baconian_root,height=10,width=25,font=("Comic Sans",20))
		self.baconian_encrypt_enter_label.pack()
		self.baconian_encrypt_entry.pack()
		baconian_encrypt_button.pack()
		self.baconian_decrypt_enter_label.pack()
		self.baconian_decrypt_entry.pack()
		baconian_decrypt_button.pack()
		self.baconian_text_box.pack()
		self.baconian_root.mainloop()

	def baconian_encrypt(self):
		self.baconian_text_box.delete(1.0,END)
		self.label_counter = 0
		baconian_text = self.baconian_encrypt_entry.get()
		convert_text = bc.encrypt(baconian_text.upper())
		self.baconian_text_box.tag_configure("center",justify='center')
		self.baconian_text_box.insert(END,"Zaszyfrowany tekst: "+convert_text)
		self.baconian_text_box.tag_add("center",1.0,"end")

	def baconian_decrypt(self):
		self.baconian_text_box.delete(1.0,END)
		self.label_counter = 0
		baconian_text = self.baconian_decrypt_entry.get()
		convert_text = bc.decrypt(baconian_text.lower())
		self.baconian_text_box.tag_configure("center",justify='center')
		self.baconian_text_box.insert(END,"Odszyfrowany tekst: "+convert_text)
		self.baconian_text_box.tag_add("center",1.0,"end")
		
	def zb_window(self):
		self.zb_root = Tk()
		self.zb_root.title("Szyfr Zietnik")
		self.zb_encrypt_enter_label = Label(self.zb_root, text="Podaj zdanie do zaszyfrowania",font=("Comic Sans",20))
		self.zb_encrypt_entry = Entry(self.zb_root)
		self.zb_encrypt_enter_key_label = Label(self.zb_root, text="Podaj klucz",font=("Comic Sans",20))
		self.zb_encrypt_entry_key = Entry(self.zb_root)
		zb_encrypt_button = Button(self.zb_root,text="Szyfruj",font=("Comic Sans",20),command=self.zb_encrypt)
		self.zb_decrypt_enter_label = Label(self.zb_root, text="Podaj zdanie do odszyfrowania",font=("Comic Sans",20))
		self.zb_decrypt_entry = Entry(self.zb_root)
		self.zb_decrypt_enter_key_label = Label(self.zb_root, text="Podaj klucz",font=("Comic Sans",20))
		self.zb_decrypt_entry_key = Entry(self.zb_root)
		zb_decrypt_button = Button(self.zb_root,text="Deszyfruj",font=("Comic Sans",20),command=self.zb_decrypt)
		self.zb_text_box = Text(self.zb_root,height=10,width=25,font=("Comic Sans",20))
		self.zb_encrypt_enter_label.pack()
		self.zb_encrypt_entry.pack()
		self.zb_encrypt_enter_key_label.pack()
		self.zb_encrypt_entry_key.pack()
		zb_encrypt_button.pack()
		self.zb_decrypt_enter_label.pack()
		self.zb_decrypt_entry.pack()
		self.zb_decrypt_enter_key_label.pack()
		self.zb_decrypt_entry_key.pack()
		zb_decrypt_button.pack()
		self.zb_text_box.pack()
		self.zb_root.mainloop()

	def zb_encrypt(self):
		self.zb_text_box.delete(1.0,END)
		self.label_counter = 0
		zb_text = self.zb_encrypt_entry.get()
		zb_key = self.zb_encrypt_entry_key.get()
		convert_text =zb.szyfrowanie(zb_text,int(zb_key))
		self.zb_text_box.tag_configure("center",justify='center')
		self.zb_text_box.insert(END,"Zaszyfrowany tekst: "+convert_text)
		self.zb_text_box.tag_add("center",1.0,"end")

	def zb_decrypt(self):
		self.zb_text_box.delete(1.0,END)
		self.label_counter = 0
		zb_text = self.zb_decrypt_entry.get()
		zb_key = self.zb_decrypt_entry_key.get()
		convert_text =zb.deszyfrowanie(zb_text,int(zb_key))
		self.zb_text_box.tag_configure("center",justify='center')
		self.zb_text_box.insert(END,"Odszyfrowany tekst: "+convert_text)
		self.zb_text_box.tag_add("center",1.0,"end")

	def tr_window(self):
		self.tr_root = Tk()
		self.tr_root.title("Szyfr kolumnowy przestawieniowy")
		self.tr_encrypt_enter_label = Label(self.tr_root, text="Podaj zdanie do zaszyfrowania",font=("Comic Sans",20))
		self.tr_encrypt_entry = Entry(self.tr_root)
		self.tr_encrypt_enter_key_label = Label(self.tr_root, text="Podaj klucz",font=("Comic Sans",20))
		self.tr_encrypt_entry_key = Entry(self.tr_root)
		tr_encrypt_button = Button(self.tr_root,text="Szyfruj",font=("Comic Sans",20),command=self.tr_encrypt)
		self.tr_decrypt_enter_label = Label(self.tr_root, text="Podaj zdanie do odszyfrowania",font=("Comic Sans",20))
		self.tr_decrypt_entry = Entry(self.tr_root)
		self.tr_decrypt_enter_key_label = Label(self.tr_root, text="Podaj klucz",font=("Comic Sans",20))
		self.tr_decrypt_entry_key = Entry(self.tr_root)
		tr_decrypt_button = Button(self.tr_root,text="Deszyfruj",font=("Comic Sans",20),command=self.tr_decrypt)
		self.tr_text_box = Text(self.tr_root,height=10,width=25,font=("Comic Sans",20))
		self.tr_encrypt_enter_label.pack()
		self.tr_encrypt_entry.pack()
		self.tr_encrypt_enter_key_label.pack()
		self.tr_encrypt_entry_key.pack()
		tr_encrypt_button.pack()
		self.tr_decrypt_enter_label.pack()
		self.tr_decrypt_entry.pack()
		self.tr_decrypt_enter_key_label.pack()
		self.tr_decrypt_entry_key.pack()
		tr_decrypt_button.pack()
		self.tr_text_box.pack()
		self.tr_root.mainloop()

	def tr_encrypt(self):
		self.tr_text_box.delete(1.0,END)
		self.label_counter = 0
		tr_text = self.tr_encrypt_entry.get()
		tr_key = self.tr_encrypt_entry_key.get()
		convert_text =tr.encryption(tr_text,int(tr_key))
		self.tr_text_box.tag_configure("center",justify='center')
		self.tr_text_box.insert(END,"Zaszyfrowany tekst: "+convert_text)
		self.tr_text_box.tag_add("center",1.0,"end")

	def tr_decrypt(self):
		self.tr_text_box.delete(1.0,END)
		self.label_counter = 0
		tr_text = self.tr_decrypt_entry.get()
		tr_key = self.tr_decrypt_entry_key.get()
		convert_text =tr.decryption(tr_text,int(tr_key))
		self.tr_text_box.tag_configure("center",justify='center')
		self.tr_text_box.insert(END,"Odszyfrowany tekst: "+convert_text)
		self.tr_text_box.tag_add("center",1.0,"end")

start = CryptGUI()