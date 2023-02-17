# File Extended Vigenere Cipher

def isEqualLength(plaintext, key):
    # input : plaintext(str), key(str)
    if (len(plaintext) == len(key)) :
        return True
    else : 
        return False

def repeatKey(plaintextLength, key) :
    # input : plaintextLength(integer), key(str)
    #key = list(key)
    actualKey = []
    for i in (range(plaintextLength)):
        actualKey.append(key[i % len(key)])

    return actualKey

def encryptExtendedVigenereCipher(plaintext, key):
    # input : plaintext(string 'char ASCII'), key(list of 'integer')
    # output : string 'char ASCII'
    #print(f"panjang kunci : {len(key)}")
    #print(f"panjang plaintext : {len(plaintext)}")
    encryptedText = []

    plaintext = list(plaintext)
    
    if (not(isEqualLength(plaintext, key))):
        key = repeatKey(len(plaintext), key)
    #print(f"panjang kunci sesudah diulang: {len(key)}")
   
    for i in range (len(plaintext)):
        encryptedValue = "" + chr((ord(plaintext[i]) + key[i]) % 256)
        encryptedText.append(encryptedValue)
    return("".join(encryptedText))

def decryptExtendedVigenereCipher(encryptedText, key):
    # input : encryptedtext(string 'char ASCII'), key(list of integer)
    # output : string 'char ASCII'
    decryptedText = []
    encryptedText = list(encryptedText)

    if (not(isEqualLength(encryptedText, key))):
        key = repeatKey(len(encryptedText), key)

    for i in range (len(encryptedText)):
        decryptedValue ="" + chr((ord(encryptedText[i]) - (key[i]) + 256) % 256)
        decryptedText.append(decryptedValue)
    return("".join(decryptedText))