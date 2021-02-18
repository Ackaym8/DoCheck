from tkinter import *
from tkinter.constants import DISABLED, NORMAL
from programSave import programSave
from functools import partial

class programGUI:

    items = []
    root = Tk()
    save = object

    def __init__(self):
        self.save = programSave()
        self.items = self.save.getSaveData()
        self

    def run(self):

        self.placeInitialEle() # place initial elements
        self.placeListItems() # place list elements

        self.root.mainloop()

    def placeInitialEle(self):

        # window
        self.root.title("To-Do List Tracker")
        self.root.geometry("1000x600")
        self.root.wm_maxsize(width=1000, height=600)

        # title formatting
        title = Label(self.root, text="To-Do List", font=("Arial", 40))
        title.place(x=11, y=11)


    def placeListItems(self):

        def onFrameConfigure(event):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        # initial values
        yNum = 20
        itemID = 0
        frameHeight = 20

        # labeled frame
        listFrame = LabelFrame(self.root, text="To-do List", height=400, width=420)
        listFrame.place(x=9, y=93)

        # canvas for scrolling
        canvas = Canvas(self.root, height=350, width=400)
        canvas.place(x=15, y=125)

        # canvas frame for containing items
        canvasFrame = Frame(canvas, height=750, width=420)
        canvasFrame.place(x=9, y=0)

        # scrollbar for scrolling
        scrollbar = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.place(x=410, y=105, height=385)

        # scrollbar association with canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((4, 4), window=canvasFrame, anchor="nw", tags="canvasFrame")
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.bind(sequence="<Configure>", func=onFrameConfigure)

        # title frame
        titleFrame = Frame(self.root, width=400, height=25)
        titleFrame.place(x=450, y=72)

        # title box
        titleBox = Text(titleFrame, yscrollcommand=True)
        titleBox.place(x=0, y=0)

        # desc box
        descBox = Text(self.root, yscrollcommand=True)
        descBox.place(x=450, y=100)
        descText = descBox.get(index1=1.0, index2='end')

        # save button
        saveButton = Button(self.root, text="Save", command=self.saveClick)
        if descText == "\n":
            saveButton.configure(state=DISABLED)
        saveButton.place(x=450, y=500)

        # placing list items

        items_elements = []
        for item in self.items:
            if len(item) > 1:
                item_elements = []

                buttonText = item[0]
                if len(item[0]) > 50:
                    buttonText = buttonText[0:38]
                    buttonText += "..."

                button = Button(canvasFrame, text=buttonText, width="40", command=partial(self.itemButtonClick, titleBox, itemID, descBox))
                button.place(x=35, y=yNum)
                item_elements.append(buttonText)

                checkButton = Checkbutton(canvasFrame, variable=int(item[1]))
                checkButton.place(x=11, y=yNum + 2.5)
                if int(item[1]) == 1:
                    checkButton.select()
                item_elements.append(checkButton)

                item_elements.append(descText)

                yNum += 25
                itemID += 1
                frameHeight+=25
                canvasFrame.configure(height=frameHeight)
                items_elements.append(item_elements)

        # dynamically saves each list item's elements
        # self.dynamicSaving(items_elements)

        # resetting scroll region of canvas after list items are updated
        canvas.configure(scrollregion=canvas.bbox("all"))


    # dynamically saves each list item's elements (title, status, description)
    def dynamicSaving(self, items_ele):
        i=0

        for item in self.items:
            # WIP title editing
            item[1] = items_ele[i][1]
            item[2] = items_ele[i][2]

            i+=1
        self.save.saveData(self.items)

    def saveClick(self):
        self.root.destroy()
        self.root = Tk()
        self.run()

    def itemButtonClick(self, title, ID, desc):
        if len(self.items) >= ID:
            desc.replace(index1=1.0, index2='end', chars=self.items[ID][2])
            title.replace(index1=1.0, index2='end', chars=self.items[ID][0])
