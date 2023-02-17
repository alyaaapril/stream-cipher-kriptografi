import sys
import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from tkinter.messagebox import showinfo
from fileOperation import *

from RC4 import *
from conversion import *

global window
window = Tk()
window.title("My Own Stream Cipher - Teks atau .txt")
window.geometry('800x590')
window.configure(bg="#E0E1E9")

def open_file():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    print(filename)
    entry_text = readFile(filename)
    entry_message.insert(END, entry_text)
    filename.close()

def save_file():
    content = text_entry1.get(1.0, END)

    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    #content = str_to_binary(content)
    #content = binary_to_str(content)
    f.write(content)
    f.close()

def clear_messageKey():
    entry_message.delete(0, END)
    entry_key.delete(0, END)

def clear_text():
    text_entry1.delete('1.0', END)

def click_back():
    from guiHome import mainPage
    mainPage(window)

# Encryption

def encrypt_message():
    plaintext = entry_message.get()
    key = entry_key.get()

    S_array = generate_S_array()
    T_array = str_to_ascii(key)
    KSA_result = KSA(S_array, T_array)
    encryption = modifeidRC4_Encryption_text(plaintext, KSA_result)

    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)
    text_entry1.insert(END, encryption)
    text_entry2.insert(END, string_to_base64(encryption))

def decrypt_message():
    cipher = entry_message.get()
    key = entry_key.get()

    S_array = generate_S_array()
    T_array = str_to_ascii(key)
    KSA_result = KSA(S_array, T_array)
    decryption = modifeidRC4_Decryption_text(cipher, KSA_result)

    text_entry1.delete('1.0', END)
    text_entry2.delete('1.0', END)
    text_entry1.insert(END, decryption)
    text_entry2.insert(END, string_to_base64(decryption))

title = Label(window, text = 'My Own Stream Cipher - Teks atau .txt', font = ('Inter', 14), bd=15, bg="#E0E1E9")
title.grid(row=0, column=0)

note = Label(window, text = 'Note : Input dalam format string', font = ('arial', 9), fg="#000066", bg="#E0E1E9")
note.grid(row=1, column=0, stick='w', padx=15, pady=5)

# INPUT MESSAGE
label_text = Label (window, text = 'Enter your message', font = ('Inter ', 12), bg="#E0E1E9")
label_text.grid(row=2, column=0, stick='w', padx=15, pady=5)

label_keyword = Label (window, text = 'Enter your key', font = ('arial ', 12), bg="#E0E1E9") 
label_keyword.grid(row=5, column=0, stick='w', padx=15, pady=5)

message = StringVar()
key = StringVar()


entry_message = Entry(window, textvariable=message, width=50)
entry_message.grid(row=2, column=1, padx=10, ipady=5)
entry_key = Entry(window, textvariable=key, width=50)
entry_key.grid(row=5, column=1, ipady=5)

# Browse file
btn_browseFile = Button(window, height = 1 , width=10, text="Browse a file", font = ('arial ', 10), fg="black", bg="#D3C3B1", command=open_file)
btn_browseFile.grid(row=2, column=2)

# Clear key & message
btn_clear = Button(window, height =1 , width=20, text="Clear key & message", bg="#B8B8C7", fg="black", font = ('arial ', 10), command=clear_messageKey)
btn_clear.grid(row=6, columnspan=3, pady=2)

# OUTPUT MESSAGE
label_out = Label (window, text = "Here's your result:", font = ('arial', 12), bg="#E0E1E9")
label_out.grid(row=9, column=0, stick="w", padx=15, pady=5)

# No Space
label_out1 = Label (window, text = 'Result (string)', font = ('arial ', 12), bg="#E0E1E9")
label_out1.grid(row=10, column=0, stick="w", padx=15)

text_entry1 = Text(window, width=30, height=1, wrap=WORD)
text_entry1.grid(row=10, column=1, padx=10, pady=5, ipady=5)

# Group by 5
label_out2 = Label (window, text = 'Result (base64)', font = ('arial ', 12), bg="#E0E1E9")
label_out2.grid(row=11, column=0, stick="w", padx=15)

text_entry2 = Text(window, width=30, height=1, wrap=WORD)
text_entry2.grid(row=11, column=1, padx=10, pady=5, ipady=5)

# Encryption & Decryption
label_option = Label(window, text="Choose one :", font = ('arial ', 12), bd=15, bg="#E0E1E9")
label_option.grid(row=7, columnspan=2, stick ='w')

btn_encrypt = Button(window, text="Encrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=encrypt_message)
btn_encrypt.grid(row=8, column=0)
btn_decrypt = Button(window, text="Decrypt message!", width = "15", font = ('arial ', 10), fg="white", bg="#251F4A", command=decrypt_message)
btn_decrypt.grid(row=8, column=1)

#Save as File
btn_save = Button(window, text="Save as a file", width = "10", height = "2", font = ('arial ', 10), fg="white", bg="#251F4A", command=save_file)
btn_save.grid(row=12, columnspan=3)

#Clear
btn_clear = Button(window, height =1 , width=10, text="Clear result", bg="#B8B8C7", fg="black", font = ('arial ', 10), command=clear_text)
btn_clear.grid(row=13, columnspan=3, pady=2)

note_out = Label(window, text = 'Untuk dekripsi cipher, result perlu di-copy dengan mouse', font = ('arial', 9), fg="#000066", bg="#E0E1E9")
note_out.grid(row=14, column=0, stick='w', padx=15, pady=5)

note_out1 = Label(window, text = 'Ctrl + A menyebabkan penambahan karakter di akhir', font = ('arial', 9), fg="#000066", bg="#E0E1E9")
note_out1.grid(row=15, column=0, stick='w', padx=15)

#Back to homepage
btn_back = Button(window, width=20, bg="#B8B8C7", text="Back to Home Page", command=click_back)
btn_back.place(relx = 0.01, rely = 0.90, anchor ='nw')