import re
import os
import csv

from tkinter import *

from tkinter import filedialog 

def browseFiles():
    file = filedialog.askopenfile(initialdir = "/", title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
    text = file.read()

def  CreateMcqs(text):
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    
	

window = Tk() 

window.title('File Explorer') 

window.geometry("500x500") 

window.config(background = "white") 

label_file_explorer = Label(window, text = "Import Text File") 

button_explore = Button(window, text = "Browse Files", command = browseFiles)

button_convert = Button(window, text = "Create MCQs", command = CreateMcqs)
button_download = Button(window, text = "Download File")

button_exit = Button(window, text = "Exit", command = exit) 

label_file_explorer.grid(row= 0, column = 0)

button_explore.grid(row= 1, column = 0)
button_convert.grid(row= 2, column = 0)
button_download.grid(row= 3, column = 0)
button_exit.grid(row= 4, column = 0)

window.mainloop() 
