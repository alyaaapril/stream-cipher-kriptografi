from RC4 import *
import random

S_array = generate_S_array()
print('S array : ')
print(S_array)
print("\n")

plaintext = 'apa kabar'
key = 'key' #[107, 101, 121]
T_array = translateToASCII(key)

print('Hasil pengulangan key (T array) : ')
print(repeat_T_array_key(len(S_array), T_array))
print("\n")

print('Hasil permutasi key dengan KSA : ')
swap = KSA(S_array, T_array)
print(swap)
print("\n")

print('Keystream PRGA: ')
PRGA(len(plaintext), swap)
keyStream = PRGA(len(plaintext), swap)
print(keyStream)
print("\n")

plaintextbytes = translateToASCII(plaintext)
keybytes = keyStream

print('Plain text dalam bytes: ')
print(plaintextbytes)
print("\n")

print('Hasil enkripsi: ')
encryption = crypt(plaintextbytes, keybytes)
print(encryption)
print("\n")

print('Hasil dekripsi: ')
decryption = crypt(encryption, keybytes)
print(decryption)
print("\n")