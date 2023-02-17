import sys
import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from tkinter.messagebox import showinfo
from fileOperation import *

from RC4 import *
from conversion import *

sys.path.append(r"../")

window = Tk()
window.title("My Own Stream Cipher - File")
window.geometry('800x590')
window.configure(bg="#E0E1E9")

# file explorer window
def open_file():
    # ambil path
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                        ("JPG files",
                                                        "*.jpg*"),
                                                        ("JPEG files",
                                                        "*.jpeg*"),
                                                       ("all files",
                                                        "*.*"),
                                                        ))
      
    # Change label contents
    entry_message.insert(END, filename)
    return(filename)

def add_space(text):
    spacedText = " ".join(text[i:i + 5] for i in range(0, len(text), 5))
    return(spacedText)

def save_file():
    showinfo("File saved", "The output is already a file. Please check it !")

def clear_messageKey():
    entry_message.delete(0, END)
    entry_key.delete(0, END)

def click_back():
    from guiHome import mainPage
    mainPage(window)

# Encryption

def encrypt_file():
    path = entry_message.get()
    key = entry_key.get()

    S_array = generate_S_array()
    T_array = translateToASCII(key)
    KSA_result = KSA(S_array, T_array)
    modifeidRC4_Encryption_otherfile(path, KSA_result)

def decrypt_file():
    path = entry_message.get()
    key = entry_key.get()

    S_array = generate_S_array()
    T_array = translateToASCII(key)
    KSA_result = KSA(S_array, T_array)
    modifeidRC4_Decryption_otherfile(path, KSA_result)


title = Label(window, text = 'My Own Stream Cipher - File', font = ('Inter', 18), bd=15, bg="#E0E1E9")
title.grid(row=0, column=0)


# INPUT MESSAGE
label_text = Label (window, text = 'Enter your message', font = ('Inter ', 12), bg="#E0E1E9")
label_text.grid(row=1, column=0, stick='w', padx=15, pady=5)

label_keyword = Label (window, text = 'Enter your key', font = ('arial ', 12), bg="#E0E1E9") 
label_keyword.grid(row=4, column=0, stick='w', padx=15, pady=5)

message = StringVar()
key = StringVar()


entry_message = Entry(window, textvariable=message, width=50)
entry_message.grid(row=1, column=1, padx=10, ipady=5)
entry_key = Entry(window, textvariable=key, width=50)
entry_key.grid(row=4, column=1, ipady=5)

# Browse file
btn_browseFile = Button(window, height = 1 , width=10, text="Browse a file", font = ('arial ', 10), fg="black", bg="#D3C3B1", command=open_file)
btn_browseFile.grid(row=1, column=2)

# Clear key & message
btn_clear = Button(window, height =1 , width=20, text="Clear key & message", bg="#B8B8C7", fg="black", font = ('arial ', 10), command=clear_messageKey)
btn_clear.grid(row=5, columnspan=3, pady=2)

# Encryption & Decryption
label_option = Label(window, text="Choose one :", font = ('arial ', 12), bd=15, bg="#E0E1E9")
label_option.grid(row=6, columnspan=2, stick ='w')

btn_encrypt = Button(window, text="Encrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=encrypt_file)
btn_encrypt.grid(row=7, column=0)
btn_decrypt = Button(window, text="Decrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=decrypt_file)
btn_decrypt.grid(row=7, column=1)

#Save as File
btn_save = Button(window, text="Save as a file", width = "10", height = "2", font = ('arial ', 10), fg="white", bg="#251F4A", command=save_file)
btn_save.grid(row=11, columnspan=2)

#Back to Home
btn_back = Button(window, width=20, bg="#B8B8C7", text="Back to Homepage", command=click_back)
btn_back.place(relx = 0.01, rely = 0.90, anchor ='nw')