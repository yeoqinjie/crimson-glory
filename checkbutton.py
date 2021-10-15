import tkinter as tk

window = tk.Tk()

# sets the window size to 500px x 300px
window.geometry("500x300")
window.title('Window Title')

python = tk.BooleanVar()
cplusplus = tk.BooleanVar()
# create a new checkbutton
python_checkbox = tk.Checkbutton(text="Python", variable=python)
cplusplus_checkbox = tk.Checkbutton(text="C++", variable=cplusplus)

label = tk.Label(text="Hello World",
                 width=10,  # width of 10 'o'
                 height=10,  # height of 10 'o'
                 foreground="white",  # text color
                 background="black")  # background color

label.text = f''

python_checkbox.pack()
cplusplus_checkbox.pack()
label.pack()

window.mainloop()
