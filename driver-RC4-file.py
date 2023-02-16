from RC4 import *
from conversion import *
from fileOperation import *

key = 'key'
S_array = generate_S_array()
T_array = translateToASCII(key)
KSA_result = KSA(S_array, T_array)
#print(KSA_result)
modifeidRC4Encryption_otherfile("D:\Picture\gojo.jpg", KSA_result)
#encryptBinaryExtendedVigenereCipher("D:\Picture\gojo.jpg", KSA_result)
S_array = generate_S_array()
T_array = translateToASCII(key)
KSA_result = KSA(S_array, T_array)
modifeidRC4Decryption_otherfile("D:\SEM6\Kriptografi dan Koding\Code\Tucil 2\stream-cipher-kriptografi\encryption.jpg", KSA_result)