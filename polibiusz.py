"""Szyfr Polibiusza"""

szyfrowanie = {'A':'11','B':'12','C':'13','D':'14','E':'15','F':'21','G':'22','H':'23','IJ':'24','K':'25','L':'31','M':'32','N':'33','O':'34','P':'35','Q':'41','R':'42','S':'43','T':'44','U':'45','W':'51','X':'52','Y':'53','Z':'54',' ':'0'}
deszyfrowanie = {'11':'A','12':'B','13':'C','14':'D','15':'E','21':'F','22':'G','23':'H','24':'IJ','25':'K','31':'L','32':'M','33':'N','34':'O','35':'P','41':'Q','42':'R','43':'S','44':'T','45':'U','51':'W','52':'X','53':'Y','54':'Z','00':' '}

def encryption(text):
   lista = []
   lista[:] = text.upper()
   lista1 = []
   #print(lista)
   for i in range(len(lista)):
      if lista[i] in szyfrowanie:
         lista1.append(szyfrowanie.get(lista[i]))
   result = ''.join(lista1)
   return result


def decryption(text2):
   rozdzielony = []
   lista = []
   lista[:] = str(text2)
   result = []

   for i in range(len(lista)):
      if lista[i] == '0':
         lista[i] = '00'
   lista1 = ''.join(lista)
   for i in range(0, len(lista1), 2):
      rozdzielony.append(lista1[i : i + 2])
   #print(rozdzielony)
   for i in range(len(rozdzielony)):
      if rozdzielony[i] in deszyfrowanie:
         result.append(deszyfrowanie.get(rozdzielony[i]))
   result2 = ''.join(result)
   return result2
