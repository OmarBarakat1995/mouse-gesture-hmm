from tkinter import *
from classifier import *
from tkinter import messagebox
import save_load
import gui_predict
import gui_collect
import os

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
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
                             command=self.prediction)
        self.button_p.pack(padx=5, pady=20, side=LEFT)



    def collect(self):
        self.master.destroy()
        c_root = Tk()
        c_root.title("Collect training examples")
        gui_collect.Application(c_root)
        c_root.mainloop()

    def create_c(self):
        self.my_classifier = Classifier("dataset")
        self.my_classifier.create_models_train([5] * self.my_classifier.n_classes, no_epochs=1)
        messagebox.showinfo("Classifier created successfully")

    def save_c(self):
        save_load.save_to_disk(self.my_classifier, os.path.join("models", "0" + ".txt"))
        messagebox.showinfo("save", "Classifier saved successfully")

    def prediction(self):
        self.master.destroy()
        p_root = Tk()
        p_root.title("Draw")
        gui_predict.Application(p_root)
        p_root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()