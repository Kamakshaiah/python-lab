import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame()
frame1.pack()

frame2 = tk.Frame()
frame2.pack()

lab1 = tk.Label(master=frame1, text="Input text")
lab1.pack()

lab2 = tk.Label(master=frame2, text="Output text")
lab2.pack()

inputtext = tk.Entry(master=frame1)
inputtext.pack()

outputtext = tk.Entry(master=frame2)
outputtext.pack()

def printtext():
    inputtextvalue = inputtext.get()
    outputtext.delete(0, tk.END)
    outputtext.insert(0, inputtextvalue) 

button = tk.Button(window, text="Click", command=printtext)
button.pack()




    

window.mainloop()
