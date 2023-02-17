from RC4 import *
from fileOperation import *

key = 'key'
S_array = generate_S_array()
T_array = translateToASCII(key)
KSA_result = KSA(S_array, T_array)

#modifeidRC4_Encryption_otherfile(r"C:\Users\ACER\Downloads\ReduceImageSize.net_50kb_21650.jpg", KSA_result)
modifeidRC4_Decryption_otherfile("D:\SEM6\Kriptografi dan Koding\Code\Tucil 2\encryption.jpg", KSA_result)