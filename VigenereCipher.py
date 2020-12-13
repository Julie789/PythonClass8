#VigenereCipher.py
import CaesarCipher

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def keywordToNumber(keyword):
    keyword = keyword.upper()
    keys = []
    for letter in keyword:
        key = alpha.find(letter)
        keys.append(key)

    return keys



def encode(message, keyword):
    secret = ""
    letterCount = 0
    keys = keywordToNumber(keyword)

    message = message.upper()
    for letter in message:
        key = keys[letterCount % len(keys)]

        #change each letter


    return secret
