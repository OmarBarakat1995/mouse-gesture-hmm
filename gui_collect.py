from tkinter import *
from tkinter.colorchooser import askcolor
import save_load
import os


class SaveDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Gesture representative number :')
        self.myLabel.pack()
        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
        self.filepath = ""

    def send(self):
        self.filepath = self.myEntryBox.get()
        self.top.destroy()


class LoadDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        self.myLabel = Label(top, text='Gesture representative number')
        self.myLabel.pack()
        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.filepath = self.myEntryBox.get()
        self.top.destroy()


#  http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#  http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
#  http://zetcode.com/gui/tkinter/drawing/
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.toolsThickness = 10
        self.rgb = "#%02x%02x%02x" % (255, 0, 0)
        self.collected_data=[]
        self.coordinates=[]

        self.pack(expand=1, fill=BOTH)
        self.createWidgets()

        master.bind('+', self.thicknessPlus)
        master.bind('-', self.thicknessMinus)

    def createWidgets(self):
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

        self.leftFrame = Frame(self, bg=tk_rgb)
        self.leftFrame.pack(side=LEFT, fill=Y)

        # -----------------------------------------------
        self.entryFrame = Frame(self.leftFrame)
        self.entryFrame.grid(row=1, column=0,
                             sticky=NW, pady=20, padx=3)

        Button(self.leftFrame,text='Select Color', command=self.set_Color).grid(row=1, column=0,
                             sticky=NW, pady=20, padx=3)

        Label(self.leftFrame, text="no.of examples: " ).grid(row=2, column=0,
                                                   sticky=NW, pady=20, padx=3)
        self.n = IntVar()
        self.n.set(0)
        Label(self.leftFrame, textvariable = self.n ).grid(row=2, column=1,pady=20)


        # ----------------------------------------------

        self.labelThickness = Label(
            self.leftFrame,
            text="line thickness:")
        self.labelThickness.grid(row=3,
                                 column=0, pady=5, padx=3,sticky=NW)

        self.myScale = Scale(
            self.leftFrame, from_=1, to=25,
            orient=HORIZONTAL,
            command=self.setThickness
        )
        self.myScale.set(self.toolsThickness)
        self.myScale.grid(
            row=4, column=0,
            pady=20, padx=3, sticky=S,
        )


        self.undo = Button(self.leftFrame, text="dismiss example",
                                      command=self.dismiss_example)
        self.undo.grid(padx=3, pady=5,
                                  row=5, column=0,
                                  sticky=NW)

        self.sbutton = Button(self.leftFrame, text="Save collected training examples",
                                      command=self.SClick)
        self.sbutton.grid(padx=3, pady=5,
                                  row=6, column=0,
                                  sticky=NW)

        self.lbutton = Button(self.leftFrame, text="Load collected training examples file",
                                      command=self.LClick)
        self.lbutton.grid(padx=3, pady=5,
                                  row=7, column=0,
                                  sticky=NW)

        self.button_p = Button(self.leftFrame, text="Go to Prediction",
                              command=self.prediction)
        self.button_p.grid(padx=3, pady=5,
                          row=8, column=0,
                          sticky=NW)


        # ----------------------------------------------------------------------
        self.myCanvas = Canvas(self, width=800,
                               height=500, relief=RAISED, borderwidth=5)
        self.myCanvas.pack(side=RIGHT,expand=1, fill=BOTH)
        self.myCanvas.bind("<B1-Motion>", self.draw)
        self.myCanvas.bind("<Button-1>", self.setPreviousXY)
        self.myCanvas.bind("<ButtonRelease-1>", self.buttonReleased)

    # ----------------------------------------------------------------------
    def setThickness(self, event):
        print(self.myScale.get())
        self.toolsThickness = self.myScale.get()

    def setPreviousXY(self, event):
        print("now")
        self.previousX = event.x
        self.previousY = event.y

    def draw(self, event):
        self.myCanvas.create_line(self.previousX, self.previousY,
                                      event.x, event.y,
                                      width=self.toolsThickness,
                                      fill=self.rgb)
        self.previousX = event.x
        self.previousY = event.y
        self.coordinates.append([self.previousX, self.previousY])

    def SClick(self):
        sDialog = SaveDialog(root)
        root.wait_window(sDialog.top)
        print('File path : ', sDialog.filepath)
        self.save(sDialog.filepath)

    def LClick(self):
        lDialog = LoadDialog(root)
        root.wait_window(lDialog.top)
        print('File path : ', lDialog.filepath)
        self.load(lDialog.filepath)

    def delteAll(self):
        self.myCanvas.delete("all")

    def prediction(self):
        self.master.destroy()
        os.system('python gui_predict.py')

    def thicknessPlus(self, event):
        if self.toolsThickness < 25:
            self.toolsThickness += 1
            self.myScale.set(self.toolsThickness)

    def thicknessMinus(self, event):
        if 1 < self.toolsThickness:
            self.toolsThickness -= 1
            self.myScale.set(self.toolsThickness)

    def set_Color(self):
        color = askcolor()
        self.rgb=(color[1])

    def dismiss_example(self):
        self.collected_data = self.collected_data[:-1]
        print("Now you have : ", len(self.collected_data), "training examples")
        self.n.set(self.n.get() - 1)

    def save(self, g_number):
         # complete this function to save collected examples
         # note : self.collected_data is a list of all submitted coordinates lists
         #one coordinate list has the form ->  [ [X1,Y1],... [Xn,Yn] , integer_refering to gesture class ]
         #ie : gesture class of example m can be indexed as : self.collected_data[m][-1]

         save_load.save_to_disk(self.collected_data, os.path.join("dataset/", g_number +".txt"))
         self.collected_data = []
         self.n.set(0)

    def load(self, g_number):
        # complete this function to save collected examples
        # note : self.collected_data is a list of all submitted coordinates lists
        # one coordinate list has the form ->  [ [X1,Y1],... [Xn,Yn] , integer_refering to gesture class ]
        # ie : gesture class of example m can be indexed as : self.collected_data[m][-1]

        b = save_load.load_from_disk(os.path.join("dataset/", g_number + ".txt"))
        self.collected_data.extend(b)
        self.n.set(len(self.collected_data))

    def buttonReleased(self,event):
        #popup window (submit? , gesture_class?)
        #if submit==yes :
        print(self.coordinates)
        #self.coordinates.append(gesture_class) #ie:we can index it with self.coordinates[-1]
        self.collected_data.append(self.coordinates)
        self.coordinates=[]
        self.delteAll()
        print("Now you have : ",len(self.collected_data),"training examples")
        self.n.set(self.n.get()+1)


if __name__ == "__main__":
    root = Tk()
    root.title("Collect training examples")
    app = Application(root)
    root.mainloop()
