from RC4 import *
from conversion import *
from extendedVigenereCipher import *

plaintext = 'apa kabar'
key = 'key' #[107, 101, 121]

S_array = generate_S_array() #256
T_array = str_to_ascii(key) # 3
KSA_result = KSA(S_array, T_array) #256
print("Enkripsi :")
encrypt = modifeidRC4_Encryption_text(plaintext, KSA_result)
print(encrypt)

S_array = generate_S_array() #256
T_array = str_to_ascii(key) # 3
KSA_result = KSA(S_array, T_array)
print("Dekripsi :")
print(modifeidRC4_Decryption_text(encrypt, KSA_result))
