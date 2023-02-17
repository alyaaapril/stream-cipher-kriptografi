from RC4 import LFSR

KSA_result = [1,1,1,1]

#permutation = expandPermutation(5, KSA_array)
#permutation
#print(permutation

array_keluaran = []
length = 1000

print(LFSR(length, KSA_result))
'''
length = 15
for i in range(length):
    target_index1 = i % len(KSA_result)
    target_index2 = (len(KSA_result)-(i % len(KSA_result))-1)
    print(f"Target index ke-{i} : {target_index1} dan {target_index2}")
'''
    