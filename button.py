import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title('Window Title')

# create a new button
button = tk.Button(
    text='Click me',
    width=15,
    height=5
)

# put the button into the window
button.pack()

window.mainloop()
