#File RC4.py
#Berisi fungsi-fungsi yang akan digunakan dalam algoritma RC4

import fileOperation
from conversion import *
from extendedVigenereCipher import *
from pathlib import Path

#S_array =  state vector array
#T_array = key array (temporary vector)
def translateToASCII(text):
    ascii_array = []
    for i in range (len(text)):
        asciiText = ord(text[i])
        ascii_array.append(asciiText)
    return ascii_array

def generate_S_array() :
    s_array = []
    for i in range(256):
        s_array.append(i)
    return s_array
    
def repeat_T_array_key(length_S_array, key) :
    list_key = list(key)
    T_Array = []
    for i in (range(length_S_array)):
        T_Array.append(list_key[i % len(list_key)])
    return T_Array

def KSA(S_array, T_array): 
    #fungsi : permutation
    if (len(T_array) < len(S_array)):
        T_array = repeat_T_array_key(len(S_array), T_array)

    i = swap_index = 0
    while (i < len(S_array)):
        swap_index = (swap_index + S_array[i] + T_array[i]) % len(S_array)
        temp = S_array[i]
        S_array[i] = S_array[swap_index]
        S_array[swap_index] = temp
        i+=1
    return S_array

'''
def PRGA(length_plaintext, KSA_result): 
    #fungsi : generate keystream sepanjang plaintext
    i = j = 0
    keystream = []
    #print('jumlah pengulangan', length_plaintext)
    #print('\n')
    while (i < length_plaintext):
        i = (i + 1) % 256
        #print('i :', i)
        j = (j + KSA_result[i]) % 256
        #print('j :', j)

        # swap
        temp = 0
        temp = KSA_result[i]
        KSA_result[i] = KSA_result[j]
        KSA_result[j] = temp

        t = (KSA_result[i] + KSA_result[j]) % 256
        #print('k :', KSA_result[t])
        keystream.append(KSA_result[t])

    return keystream
'''
def PRGA(plaintext, KSA_result): 
    #fungsi : generate keystream sepanjang plaintext
    #output : list 'int'
    i = j = 0
    keystream = []

    while (i < len(plaintext)):
        i = (i + 1) % 256
        j = (j + KSA_result[i]) % 256

        # swap
        temp = 0
        temp = KSA_result[i]
        KSA_result[i] = KSA_result[j]
        KSA_result[j] = temp

        t = (KSA_result[i] + KSA_result[j]) % 256
        keystream.append(KSA_result[t])

    return keystream

'''
def crypt(plainTextbytes, keybytes):
    ciphertext = []
    for i in range (len(plainTextbytes)):
        cipherbytes = plainTextbytes[i] ^ keybytes[i]
        ciphertext.append(cipherbytes)

    return ciphertext
'''

def modifeidRC4Encryption_text(plaintext, KSA_result):
    # input : plaintext, KSA_result : hasil permutasi KSA
    keystream = PRGA(plaintext, KSA_result)
    print(f"Panjang keystream : {len(keystream)}")
    cipher = encryptExtendedVigenereCipher(plaintext, keystream)
    return cipher

def modifeidRC4Decryption_text(encryptedtext, KSA_result):
    # input : plaintext, KSA_result : hasil permutasi KSA
    keystream = PRGA(encryptedtext, KSA_result)
    decrypt = decryptExtendedVigenereCipher(encryptedtext, keystream)
    return decrypt

def modifeidRC4Encryption_otherfile(pathFile, KSA_result):
    # input : file, kKSA_result(list of integer)
    # output : file
    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1")
    keystream = PRGA(binary, KSA_result)
    print(keystream)
    encryptedFile = encryptExtendedVigenereCipher(binary, keystream)
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"encryption{file_extension}", encryptedFile.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai

def modifeidRC4Decryption_otherfile(pathFile, KSA_result):
    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1")
    keystream = PRGA(binary, KSA_result)
    decryptedFile = decryptExtendedVigenereCipher(binary, keystream)
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"decryption{file_extension}", decryptedFile.encode("ISO-8859-1")) # ubah kembali file ke file extension yang sesuai
