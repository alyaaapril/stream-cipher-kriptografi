from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Button, Label

# Declare the Button
def click_input_teks():
    window.destroy()
    import guiStreamCipherTeks
    guiStreamCipherTeks(window)

def click_input_file():
    window.destroy()
    import guiStreamCipherFile
    guiStreamCipherFile(window)

def mainPage(screen=None):
    if (screen != None):
        screen.destroy()
    global window
    window = Tk()
    window.title("Classical Cipher")
    window.geometry("800x500")
    window.configure(bg="#E0E1E9")

    # JUDUL
    title = Label(window, text = 'My Own Stream Cipher', font = ('Inter', 18), bd=15, bg="#E0E1E9")
    title.grid(row=0, column=0, stick='w', padx = 50, pady=60)

    # PILIH INPUT
    Input_Teks = Button(window, text="Input teks atau .txt", width = "20", height = "5", font = ('arial ', 16), fg="white", bg="#251F4A", command=click_input_teks)
    Input_Teks.grid(row=1, column=0, stick='w', padx = 50)

    Input_File = Button(window, text="Input File lain", width = "20", height = "5", font = ('arial ', 16), fg="white", bg="#251F4A", command=click_input_file)
    Input_File.grid(row=1, column=1, stick='w', padx=50)

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    mainPage()