
mapping = {
  " ": 100,
  "a": 101,
  "A": 102,
  "b": 103,
  "B": 104,
  "c": 105,
  "C": 106,
  "d": 107,
  "D": 108,
  "e": 109,
  "E": 110,
  "f": 111,
  "F": 112,
  "g": 113,
  "G": 114,
  "h": 115,
  "H": 116,
  "i": 117,
  "I": 118,
  "j": 119,
  "J": 120,
  "k": 121,
  "K": 122,
  "l": 123,
  "L": 124,
  "m": 125,
  "M": 126,
  "n": 127,
  "N": 128,
  "o": 129,
  "O": 130,
  "p": 131,
  "P": 132,
  "q": 133,
  "Q": 134,
  "r": 135,
  "R": 136,
  "s": 137,
  "S": 138,
  "t": 139,
  "T": 140,
  "u": 141,
  "U": 142,
  "v": 143,
  "V": 144,
  "w": 145,
  "W": 146,
  "x": 147,
  "X": 148,
  "y": 149,
  "Y": 150,
  "z": 151,
  "Z": 152
}

reversed_mapping = {v: k for k, v in mapping.items()}

# def main(tekst, sposob, step):

def szyfrowanie(str, step=0):

    def dehash(char):
        return mapping[char] - step

    def hash(encoded_char, avg=0):
        return reversed_mapping[((((avg + encoded_char) % 100) + step) % 53) + 100]

    def encode(tekst):
        chars = list(tekst)
        return [mapping[key] for key in chars]

    str = encode(str)
    
    encoded = f"{hash(str[0])}"

    if len(str) < 2:
        return encoded

    zakres = [str[0]]
    for x in range(1, len(str)):
        avg = round(sum(zakres)/len(zakres))
        char = hash(str[x], avg)
        zakres.append(dehash(char))
        encoded += char
    return encoded

def deszyfrowanie(hashed, step=0):

    def dehash(char):
        return mapping[char] - step

    decoded = ""
    for x in range(len(hashed)-1, -1, -1):
        zakres_avg = hashed[:x] 
        if len(zakres_avg) > 0 :
            avg = round(sum([dehash(char) for char in zakres_avg]) / (len(zakres_avg)))
        else:
            avg = 0
        char_code = (dehash(hashed[x]) - avg) % 153
        if char_code < 100: char_code += 100
        decoded = reversed_mapping[char_code] + decoded
    return decoded
    
    # if sposob == "k":
    #     result = szyfrowanie(encode(tekst))
    # elif sposob == "o":
    #     result = deszyfrowanie(tekst)
    # else:
    #     return print("Zly wybor")
    # print(f"Rezultat: {result}")


# if __name__ == '__main__': 
#     """
#     > python3 file.py 'tekst_w_dolarach' <k/o> <step:int>
    
#     k - zakodowanie
#     o - odkodowanie
#     Przykład:
#     > python3 ZB.py 'Kryptografia' k 3
#     """
#     if len(argv) != 4:
#         print("Niepoprawna komenda")
#     else:        
#         string = argv[1]
#         sposob = argv[2]
#         step = int(argv[3])
#         print(f"Tekst: {string}")
#         print("Szyfrowanie" if sposob == "k" else "Deszyfrowanie")
#         print(f"Przesuniecie: {step}")
#         main(string, sposob, step)
# else:
#     string = input("Podaj ciąg znaków: ")
#     sposob = input("Kodowanie / odkodowanie (k/o): ")
#     step = int(input("Podaj przesuniecie: "))
#     main(string, sposob, step)


print(szyfrowanie("Lorem",3))
print(deszyfrowanie("nbYRa",3))