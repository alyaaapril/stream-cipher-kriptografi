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

def crypt(plainTextbytes, keybytes):
    ciphertext = []
    for i in range (len(plainTextbytes)):
        cipherbytes = plainTextbytes[i] ^ keybytes[i]
        ciphertext.append(cipherbytes)

    return ciphertext