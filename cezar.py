def convert(entry, key=3):
    chars = [ord(char) for char in entry.strip()]
    new_sentence = ""
    for char in chars:
        if char in range(65,97):
            new_sentence+=chr((char+key-65)%26+65)
        elif char in range(97,123):
            new_sentence+=chr((char+key-97)%26+97)
    return new_sentence