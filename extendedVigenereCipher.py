import fileOperation
from pathlib import Path

def isEqualLength(plaintext, key):
    # input : plaintext(str), key(str)
    if (len(plaintext) == len(key)) :
        return True
    else : 
        return False

def repeatKey(plaintextLength, key) :
    # input : plaintextLength(integer), key(str)
    key = list(key)
    actualKey = []
    for i in (range(plaintextLength)):
        actualKey.append(key[i % len(key)])

    return actualKey

def encryptExtendedVigenereCipher(plaintext, key):
    # input : plaintext(string 'char ASCII'), key(list of 'integer')
    # output : string 'char ASCII'
    encryptedText = []

    plaintext = list(plaintext)

    if (not(isEqualLength(plaintext, key))):
        key = repeatKey(len(plaintext), key)
   
    for i in range (len(plaintext)):
        asciiText = ord(plaintext[i])
        asciiKey  = key[i]
        encryptedValue = "" + chr(((asciiText + asciiKey) % 256) )
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

'''
def encryptBinaryExtendedVigenereCipher(pathFile, key):
    # input : file, key(list of integer)
    # output : file
    f = fileOperation.readBinaryFile(pathFile)
    binary = f.decode("ISO-8859-1") # decode ke string of 'char'
    encryptedText = encryptExtendedVigenereCipher(binary, key) # enkripsi dengan fungsi enkripsi 256 ASCII
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"encryption{file_extension}", encryptedText.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai
    print(f" Nama file enkripsi adalah encryption{file_extension}\n")
 
def decryptBinaryExtendedVigenereCipher(pathFile, key):
    # input : file, key(list of integer)
    # output : file
    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1") # decode ke string of 'char'
    decryptedText = decryptExtendedVigenereCipher(binary, key) # dekripsi dengan fungsi enkripsi 256 ASCII
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"decryption{file_extension}", decryptedText.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai
    print(f" Nama file enkripsi adalah encryption{file_extension}\n")
'''