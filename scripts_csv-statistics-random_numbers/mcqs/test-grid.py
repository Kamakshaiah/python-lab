import tkinter

master=tkinter.Tk()
master.title("place() method")
master.geometry("450x350")

button1=tkinter.Button(master, text="button1")
button1.place(x=0, y=100)

button2=tkinter.Button(master, text="button2")
button2.place(x=0, y=125)

button3=tkinter.Button(master, text="button3")
button3.place(x=0, y=150)

master.mainloop()
