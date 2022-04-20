import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master=window)
frame.pack()

textwig = tk.Text()
textwig.pack()

def PrintText():
    textwigText = textwig.get("1.0", tk.END)
    print(textwigText)

def DeleteText():
    textwig.delete("1.0", tk.END)
    print('The has been deleted successfully!')

butPrint = tk.Button(master = frame, text="Print", command = PrintText)
butPrint.pack()

butDel = tk.Button(master=frame, text="Delete", command = DeleteText)
butDel.pack()

##butClose = tk.Button(master = frame, text="Close", command = window.destroy())
##butClose.pack()

window.mainloop()
