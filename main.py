from tkinter import *

root = Tk()
root.title('UniHelper')
root.geometry("400x600")

def testy():
    hello_label = Label(root,text="Hello " + testText.get())
    hello_label.pack()

test = Label(root,text="test:")
test.pack()
# grid ( test.grid() )

testText = Entry(root,width = 30)
testText.pack()

testButton = Button(root,text="Submit",command = testy)
testButton.pack()

root.mainloop()