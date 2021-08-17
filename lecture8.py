import tkinter as tk


window = tk.Tk()
sv = tk.StringVar()

# this is the default text we give our string variable class
sv.set("Hello World")

label = tk.Label(textvariable=sv)
entry = tk.Entry()

label.pack()
entry.pack()


def callback():
    sv.set(entry.get())


button = tk.Button(text="Click Here", command=callback)
button.pack()

window.mainloop()
