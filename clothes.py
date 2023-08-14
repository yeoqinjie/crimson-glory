import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Frame):
    # variables
    gender = ""
    labeltext = ""
    radio_male = ""
    radio_female = ""
    label = ""
    choose_button = ""
    canvas = ""
    image = []

    def __init__(self, master=None):  # constructor
        super().__init__(master)
        self.master = master
        self.master.geometry("500x700")
        self.master.title("Clothes Chooser")
        self.gender = tk.IntVar()
        self.labeltext = tk.StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.radio_male = tk.Radiobutton(
            self, text="Male", variable=self.gender, value=1
        )
        self.radio_female = tk.Radiobutton(
            self, text="Female", variable=self.gender, value=2
        )
        self.label = tk.Label(self, textvariable=self.labeltext, width=10, height=2)
        self.choose_button = tk.Button(self, text="Choose", command=self.choose)
        self.canvas = tk.Canvas(self, width=300, height=450)
        self.image.append(ImageTk.PhotoImage(Image.open("clothes1.jpg")))
        self.image.append(ImageTk.PhotoImage(Image.open("clothes2.jpg")))
        self.canvas.create_image(20, 20, anchor=tk.NW, image=self.image[0])

        self.label.pack(side="bottom")
        self.radio_male.pack()
        self.radio_female.pack()
        self.choose_button.pack()

    def choose(self):
        gender = self.gender.get()
        if gender == 1:
            self.labeltext.set("Male")
        elif gender == 2:
            self.labeltext.set("Female")
        gender -= 1
        self.canvas.image = self.image[gender]
        self.canvas.pack()


window = tk.Tk()
app = Application(master=window)  # create object 'app'
app.mainloop()
