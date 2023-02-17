import sys
import string
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


from tkinter.messagebox import showinfo
from fileOperation import *

#from PlayfairCipher import playfair

sys.path.append(r"../")
global window
window = Tk()
window.title("My Own Stream Cipher")
window.geometry('800x550')
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
    file_name = filedialog.asksaveasfile(initialdir = "/",
                                          title = "Save a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*"))).name
    text_file = open(file_name, "w")
    text_file.write(text_entry1.get(1.0, END))
    text_file.close()
    showinfo("File saved", "File saved, check your file!")
    text_entry1.delete('1.0', END)

def clear_messageKey():
    entry_message.delete(0, END)
    entry_key.delete(0, END)

def clear_text():
    text_entry1.delete('1.0', END)

# Encryption

def encrypt_message(plain, key):
    pass

def decrypt_message(cipher, key):
    pass


title = Label(window, text = 'My Own Stream Cipher', font = ('Inter', 18), bd=16, bg="#E0E1E9")
title.grid(row=0, column=0)



# INPUT MESSAGE
label_text = Label (window, text = 'Enter your message:', font = ('Inter ', 9), bg="#E0E1E9")
label_text.grid(row=1, column=0, stick='w', padx=15, pady=5)

label_keyword = Label (window, text = 'Enter your key:', font = ('arial ', 9), bg="#E0E1E9") 
label_keyword.grid(row=4, column=0, stick='w', padx=15, pady=5)

message = StringVar()
key = StringVar()

entry_message = Entry(window, textvariable=message, width=90)
entry_message.grid(row=2, column=0, padx=15, ipady=30)
entry_key = Entry(window, textvariable=key, width=90)
entry_key.grid(row=5, column=0, padx=5, ipady=5)

# Browse file
btn_browseFile = Button(window, width=20, text="Browse a file", font = ('arial ', 9), fg="black", bg="#D3C3B1", command=open_file)
btn_browseFile.grid(row=2, column=1, padx=15, ipady=30)

# Clear key & message
btn_clear = Button(window, height =1 , width=20, text="Clear key & message", bg="#B8B8C7", fg="black", font = ('arial ', 9), command=clear_text)
btn_clear.grid(row=5, column=1, pady=2)

# OUTPUT MESSAGE
label_out = Label (window, text = "Here's your result:", font = ('arial', 9), bg="#E0E1E9")
label_out.grid(row=9, column=0, stick="w", padx=15, pady=5)

text_entry1 = Text(window, width=68, height=5, wrap=WORD)
text_entry1.grid(row=10, column=0, padx=15, pady=5)

# Encryption & Decryption
label_option = Label(window, text="Choose one:", font = ('arial ', 9), bd=15, bg="#E0E1E9")
label_option.grid(row=6, columnspan=2, stick ='w')

btn_encrypt = Button(window, text="Encrypt message!", width = "15", font = ('arial ', 9), fg="white", bg="#251F4A", command=encrypt_message(message, key))
btn_encrypt.grid(row=7, column=0)
btn_decrypt = Button(window, text="Decrypt message!", width = "15", font = ('arial ', 9), fg="white", bg="#251F4A", command=decrypt_message(message, key))
btn_decrypt.grid(row=8, column=0)

#Save as File
btn_save = Button(window, text="Save as a file", width = "20", height = "5", font = ('arial ', 9), fg="white", bg="#251F4A", command=save_file)
btn_save.grid(row=10,column=1)

#Clear
btn_clear = Button(window, height =1 , width=10, text="Clear result", bg="#B8B8C7", fg="black", font = ('arial ', 9), command=clear_text)
btn_clear.grid(row=11, column=0)

window.mainloop()

