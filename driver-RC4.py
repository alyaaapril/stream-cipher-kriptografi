from RC4 import *

plaintext = 'apa kabar'
key = 'key' #[107, 101, 121]

print('Coba Enkripsi :')
S_array = generate_S_array()
T_array = str_to_ascii(key)
KSA_result = KSA(S_array, T_array)
encrypt = modifeidRC4Encryption_text(plaintext, KSA_result)
print(encrypt)

print('Coba Dekripsi :')
key = 'key'
T_array = str_to_ascii(key)
S_array = generate_S_array()
KSA_result = KSA(S_array, T_array)
decrypt = modifeidRC4Decryption_text(encrypt, KSA_result)
#decrypt = modifeidRC4Decryption_text('ðÝ«º', KSA_result)
print(decrypt)