# Operasi write dan read file
def readFile(filename):
    try:
        f = open(filename,"r")
        file_content = f.read()
        f.close()
        return file_content
    except:
        print('File not found and can not be opened:', filename)
        exit()

def writeFile(filename, text):
    try:
        f = open(filename, "w")
        f.write(text)
        f.close()
    except:
        print('File not found and can not be opened:', filename)
        exit()

def readBinaryFile(filename):
    try:
        f = open(filename,"rb")
        file_content = f.read()
        f.close()
        return file_content
    except:
        #print('File not found and can not be opened:', filename)
        exit()
    

def writeBinaryFile(filename, text):
    try:
        f = open(filename, "wb")
        f.write(text)
        f.close()
    except:
        #print('File not found and can not be opened:', filename)
        exit()