import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title = 'Window Title'

# create a new label
label = tk.Label(text="Hello World",
                 width=10,  # width of 10 'o'
                 height=10,  # height of 10 'o'
                 foreground="white",  # text color
                 background="black")  # background color

# put the label into the window
label.pack()

window.mainloop()
