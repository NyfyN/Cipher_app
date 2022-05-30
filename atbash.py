def encryption(text):

    atbash = {'A':'Ż','Ą':'Ź','B':'Z','C':'Y','Ć':'X','D':'W','E':'V','Ę':'U',
          'F':'T','G':'Ś','H':'S','I':'R','J':'Q','K':'P','L':'Ó','Ł':'O',
          'M':'Ń','N':'N','Ń':'M','O':'Ł','Ó':'L','P':'K','Q':'J','R':'I',
          'S':'H','Ś':'G','T':'F','U':'Ę','V':'E','W':'D','X':'Ć','Y':'C',
          'Z':'B','Ź':'Ą','Ż':'A','a':'ż','ą':'ź','b':'z','c':'y','ć':'x',
          'd':'w','e':'v','ę':'u','f':'t','g':'ś','h':'s','i':'r','j':'q',
          'k':'p','l':'ó','ł':'o','m':'ń','n':'n','ń':'m','o':'ł','ó':'l',
          'p':'k','q':'j','r':'i','s':'h','ś':'g','t':'f','u':'ę','v':'e',
          'w':'d','x':'ć','y':'c','z':'b','ź':'ą','ż':'a'}  

    cipher = ''
    for i in text:
        if i == ' ':
            cipher += ' '
            
        elif i == ',':
            cipher += ','
            
        elif i == '.':
            cipher += '.'
            
        elif i == '!':
            cipher += '!'
            
        elif i == '?':
            cipher += '?'
            
        else:
            cipher += atbash[i]

    return cipher
