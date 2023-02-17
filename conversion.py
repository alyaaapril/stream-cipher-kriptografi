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
    return binary_string

def binary_to_str(text):
    chr_string = []
    for i in range (len(text)):
        char = chr(int(text[i], base=10))
        chr_string.append(char)
    return ("".join(chr_string))

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