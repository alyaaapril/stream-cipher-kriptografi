from RC4 import *
from fileOperation import *

key = 'key'
S_array = generate_S_array()
T_array = translateToASCII(key)
KSA_result = KSA(S_array, T_array)

modifeidRC4_Encryption_otherfile(r"D:\Picture\gojo.jpg", KSA_result)
#modifeidRC4_Decryption_otherfile("outputFile\encryption.jpg", KSA_result)