import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="hello!",
                    bg = "gray",
                    fg = "black",
                    width=100,
                    height=100
                    )

greeting.pack()
window.mainloop()
