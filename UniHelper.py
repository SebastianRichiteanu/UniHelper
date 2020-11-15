from classes import *
from tkinter import *

root = Tk()
root.title('UniHelper')
root.geometry("600x800")


def input_subject():
    lab = Label(root,text="Name Subject: "+name_text.get())
    lab.pack()



firstSubject = Label(root, text="First Subject")
firstSubject.pack()

# grid ( test.grid() )
name_text = Entry(root,width=50)
name_text.pack()

submit = Button(root,text="Submit",command = input_subject())
submit.pack()


root.mainloop()
