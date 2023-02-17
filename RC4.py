#File RC4.py
#Berisi fungsi-fungsi yang akan digunakan dalam algoritma RC4

import fileOperation
from conversion import *
from extendedVigenereCipher import *
from pathlib import Path

#S_array =  state vector array
#T_array = key array (temporary vector)

def translateToASCII(text):
    # input : str
    # fungsi : translate string to ASCII rray
    # output : list

    ascii_array = []
    for i in range (len(text)):
        asciiText = ord(text[i])
        ascii_array.append(asciiText)
    return ascii_array

def generate_S_array() :
    # input : -
    # fungsi : generate S_array [0, 1, ..., 255]
    # output : list

    s_array = []
    for i in range(256):
        s_array.append(i)
    return s_array
    
def repeat_T_array_key(length_S_array, key) :
    # input : length_S_array (int), key(any)
    # fungsi : pengulangan hingga sepanjang length_S_array
    # output : list

    list_key = list(key)
    T_Array = []
    for i in (range(length_S_array)):
        T_Array.append(list_key[i % len(list_key)])
    return T_Array

def KSA(S_array, T_array): 
    # imput : S_array (list), T_array(list)
    # fungsi : permutation
    # output : list

    if (len(T_array) < len(S_array)):
        T_array = repeat_T_array_key(len(S_array), T_array)

    i = swap_index = 0
    #while (i < len(S_array)):
    for i in range (len(S_array)):
        swap_index = (swap_index + S_array[i] + T_array[i]) % 256 # 256 = len(S_array)
        temp = S_array[i]
        S_array[i] = S_array[swap_index]
        S_array[swap_index] = temp
    return S_array

def LFSR(jumlah_permutasi, PRGA_result):
    # input : jumlah_permutasi(int), KSA_result(list of 'int')
    # fungsi : generate keystream sepanjang plaintext
    # output : list 'int'

    array_keluaran = []
    for i in range(jumlah_permutasi):
        lengthArray = len(PRGA_result)
        
        target_index1 = 0 #i % lengthArray
        target_index2 = lengthArray-1 #lengthArray-(i % lengthArray)-1
        
        hasil_XOR = PRGA_result[target_index1] ^ PRGA_result[target_index2]
        PRGA_result.insert(0, hasil_XOR) # tambahkan hasil XOR sbg elemen pertama

        bit_keluaran = PRGA_result[lengthArray-1] #lengthArray-(i % (lengthArray))-1
        PRGA_result.pop() # buang elemen terakhir

        array_keluaran.append(bit_keluaran)

    return array_keluaran

  
def PRGA(plaintext, KSA_result): 
    # input : plaintext(any), KSA_result(list of 'int')
    # fungsi : generate keystream sepanjang plaintext
    # output : list 'int'

    i = j = 0
    keystream = []

    for i in range (len(plaintext)):
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

# Fungsi Enkripsi & Dekripsi untuk 'Teks' dan '.txt'
def modifeidRC4_Encryption_text(plaintext, KSA_result):
    # input : plaintext (str), KSA_result : hasil permutasi KSA (list of int)
    # fungsi : enkripsi teks
    # output : str

    # PRGA-kan hasil KSA
    keystream = PRGA(plaintext, KSA_result)
    # LFSR-kan hasil PRGA
    lfsr_permutation = LFSR(len(plaintext), keystream) # panjang plaintext dan encryptedText sama so, aman
    print(f'proses lfsr enkripsi dari prga selesai dengan nilai {lfsr_permutation}')

    cipher = encryptExtendedVigenereCipher(plaintext, lfsr_permutation)
    return cipher

def modifeidRC4_Decryption_text(encryptedtext, KSA_result):
    # input : plaintext (str), KSA_result : hasil permutasi KSA (list of int)
    # fungsi : dekripsi teks
    # output : str

    # PRGA-kan hasil KSA
    keystream = PRGA(encryptedtext, KSA_result)
    # LFSR-kan hasil PRGA
    lfsr_permutation = LFSR(len(encryptedtext), keystream) # panjang plaintext dan encryptedText sama so, aman
    print(f'proses lfsr dekripsi dari prga selesai dengan nilai {lfsr_permutation}')
  
    decrypt = decryptExtendedVigenereCipher(encryptedtext, lfsr_permutation)
    return decrypt

# Fungsi Enkripsi & Dekripsi untuk selain 'Teks' dan '.txt'
def modifeidRC4_Encryption_otherfile(pathFile, KSA_result):
    # input : file, kKSA_result(list of integer)
    # fungsi : enkripsi file
    # output : file

    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1")
    encryptedFile = encryptExtendedVigenereCipher(binary, KSA_result)
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"encryption{file_extension}", encryptedFile.encode("ISO-8859-1"))

def modifeidRC4_Decryption_otherfile(pathFile, KSA_result):
    # input : file, kKSA_result(list of integer)
    # fungsi : enkripsi file
    # output : file
    f = fileOperation.readBinaryFile(pathFile) 
    binary = f.decode("ISO-8859-1")
    decryptedFile = decryptExtendedVigenereCipher(binary, KSA_result)
    file_extension = Path(pathFile).suffix
    fileOperation.writeBinaryFile(f"decryption{file_extension}", decryptedFile.encode("ISO-8859-1"))