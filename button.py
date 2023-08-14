import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title("Window Title")

s = tk.StringVar()
label = tk.Label(textvariable=s, height=3)
intro = tk.Label(text="Please enter your name")
entry = tk.Entry()


def callback():
    s.set(f"Welcome to Python Course, {entry.get()}")


# create a new button
button = tk.Button(text="Click me", width=15, height=1, command=callback)

# put the button into the window
intro.pack()
entry.pack()
button.pack()
label.pack()


window.mainloop()
