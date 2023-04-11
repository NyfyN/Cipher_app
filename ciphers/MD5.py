import hashlib

def MD5_hash(string):
    # Tworzymy obiekt hashlib md5 z przekazanego ciągu znaków
    hash_object = hashlib.md5(string.encode())

    # Zwracamy wynikowy hash jako string w formacie szesnastkowym
    return hash_object.hexdigest()