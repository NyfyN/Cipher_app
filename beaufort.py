import string

def encryption(text,key):
    # tekst=t
    # klucz=k
    index=0
    cipher=""
    alphabet = list(string.ascii_lowercase)

    for i in text:
        if i in alphabet:
            shift=ord(key[index])-ord("a")
            cipher1 = chr((-ord(i) + ord("a")+shift)%26+ord("a"))
            cipher=cipher+cipher1
            index=(index +1) %len(key)
        else:
            cipher=cipher+i
    return cipher

def decryption(cipher,key):
    # szyfr=s
    # klucz=k
    index=0
    text=""
    alphabet = list(string.ascii_lowercase)

    for i in cipher:
        if i in alphabet:
            shift=ord(key[index])-ord("a")
            text1 = chr((-ord(i) + ord("a")+shift)%26+ord("a"))
            text=text+text1
            index=(index +1) %len(key)
        else:
            text=text+i
    return text

#print(encryption("lorem","merol"))