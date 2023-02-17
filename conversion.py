import base64

def str_to_ascii(str):
    ascii_array = []
    for i in range (len(str)):
        asciiText = ord(str[i])
        ascii_array.append(asciiText)
    #print(type(asciiText))
    return ascii_array

def str_to_binary(str):
    binary_string = []
    for i in range (len(str)):
        binary = format(ord(str[i]), 'b')
        binary_string.append(binary)
    #print(type(binary))
    #binary_string = ' '.join(format(ord(item), 'b') for item in Str)
    return binary_string

def string_to_base64(str):
    #pengecekan : https://calculla.com/base64_encoder
    
    b = base64.b64encode(bytes(str, 'utf-8'))
    base64_str = b.decode('utf-8') # convert bytes to string
    
    return base64_str

def base64_to_str(str):
    #pengecekan : https://calculla.com/base64_encoder
    b = base64.b64decode(str) # b'apa kabar'
    str_message = b.decode('utf-8')

    return str_message


'''
key = 'key' #[107, 101, 121]
T_array = str_to_ascii(key)
print(T_array)

binaryKey = str_to_binary(key)
print(binaryKey)

base64key = string_to_base64(key)
print(base64key)

message = base64_to_str(base64key)
print(message)
'''