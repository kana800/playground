# encryption

from itertools import cycle

def VigenereCipherDecrypt(letter,key_letter):
    return chr((((ord(letter) - ord(key_letter))+26) % 26)+ (ord('A') if letter.isupper() else ord('a')))


def VigenereCipher(text,key):
    encrypted_text = ""
    temp_text = list(text)
    iterkey = cycle(key)
    for i in temp_text:
        if i == " ":
            encrypted_text += " "
            pass
        else:
            p = next(iterkey)
            print(i,p)
            encrypted_text += VigenereCipherDecrypt(i,p)
    return encrypted_text

def VernamCipher(text,key):
    if len(text) != len(key):
        raise NotImplementedError
    else:
        encrypted_text = ""
        for i in range(len(text)):
            keymessage= (ord(text[i]) -ord('A')) - (ord(key[i])-ord('A'))
            encrypted_text += chr((keymessage % 26 ) + ord('A'))
    return encrypted_text


def CaesarCipher(text,shift):
    encrypted_text = ""
    for i in text:
        if i == " ":
            encrypted_text += " "
            pass
        else:
            encrypted_text += chr((((ord(i)-ord('A')) - shift)%26)+ord('A'))
    return encrypted_text
