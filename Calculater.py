from Tkinter import *

class Calc():
    def __init__(self):
        self.gui()

    def modIt(self):
        firstitem = self.firstItemEntry.get()
        seconditem = self.secondItemEntry.get()
        modRes = firstitem % seconditem
        self.reVar.set(modRes)

        return modRes

    def plusIt(self):
        firstItem = self.firstItemVar.get()
        secondItem = self.SecondItemVar.get()
        plusRes = int(firstItem) + int(secondItem)
        self.resVar.set(plusRes)

        return plusRes




    def gui(self):
        root = Tk()
        root.title("Calculater")
        self.resVar = StringVar()
        self.resEntry = Entry(textvariable = self.resVar, width = 20)
        self.resEntry.grid(row=0,column=0,columnspan=2)
        self.firstItemLabel = Label(text = "First item", width = 10)
        self.firstItemLabel.grid(row=1,column=0)
        self.firstItemVar = StringVar()
        self.firstItemEntry=Entry(textvariable = self.firstItemVar, width = 10)
        self.firstItemEntry.grid(row=1,column=1)
        self.SecondItemLabel = Label(text="Second item", width=10)
        self.SecondItemLabel.grid(row=2, column=0)
        self.SecondItemVar = StringVar()
        self.SecondItemEntry = Entry(textvariable=self.SecondItemVar, width=10)
        self.SecondItemEntry.grid(row=2, column=1)
        self.modButton = Button(text = "Enter",command = self.modIt, width = 20)
        self.modButton.grid(row=3,column=0)
        self.plusButton = Button(text = "plus", command =self.plusIt, width=10)
        self.plusButton.grid(row=3,column=1)
        root. mainloop()

calc = Calc()

