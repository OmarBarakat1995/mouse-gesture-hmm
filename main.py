from tkinter import *
import os
from classifier import *
from tkinter import messagebox
import save_load
import external

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.collect = Button(frame,
                             text="collect data", fg="#%02x%02x%02x"% (128, 192, 200),
                             command=self.collect)
        self.collect.pack(padx=5, pady=10, side=LEFT)

        self.create_c = Button(frame,
                             text="create & train classifier",fg="#%02x%02x%02x"% (128, 192, 200),
                             command=self.create_c)
        self.create_c.pack(padx=5, pady=20, side=LEFT)

        self.save_c = Button(frame,
                             text="Save classifier",fg="#%02x%02x%02x"% (128, 192, 200),
                             command=self.save_c)
        self.save_c.pack(padx=5, pady=20, side=LEFT)

        self.button_p = Button(frame,
                             text="Predict gestures",fg="#%02x%02x%02x"% (128, 192, 200),
                             command=quit)
        self.button_p.pack(padx=5, pady=20, side=LEFT)



    def collect(self):
        self.master.destroy()
        os.system('python gui_predict.py')

    def create_c(self):
        self.my_classifier = Classifier("dataset")
        self.my_classifier.create_models_train([5] * self.my_classifier.n_classes, no_epochs=1)
        messagebox.showinfo("Classifier created successfully")

    def save_c(self):
        save_load.save_to_disk(self.my_classifier, os.path.join("models", "0" + ".txt"))
        messagebox.showinfo("Classifier created successfully")

    def prediction(self):
        self.master.destroy()
        os.system('python gui_predict.py')






root = Tk()
app = App(root)
root.mainloop()