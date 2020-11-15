from classes import *
from tkinter import *

root = Tk()
root.title('UniHelper v0.1')
root.geometry("600x800")

global l
l = []

def clear_window():
    l = root.winfo_children()
    for x in l:
        x.destroy()

def AddSubFct(name):
    newSub = Subject(name)
    l.append(newSub)
    print(l)
    main()

def AddSubWnd():
    clear_window()
    nameLabel = Label(root,text="Name of the Subject:")
    nameLabel.grid(row=0,column=0)
    nameText = Entry(root,width=50)
    nameText.grid(row=0,column=1)
    submit = Button(root,text="Submit",command= lambda: AddSubFct(nameText.get()))
    submit.grid(row=1,column=0)
    back = Button(root,text="Back",command=main)
    back.grid(row=2,column=1)

def EditSubFct(name,ind):
    l[ind].name = name
    main()

def EditSubWnd(ind):
    clear_window()
    nameLabel = Label(root, text="Current name of the Subject:" + l[ind].name)
    nameLabel.grid(row=0, column=0)
    nameLabel = Label(root, text="New name for the Subject:")
    nameLabel.grid(row=1, column=0)
    nameText = Entry(root, width=50)
    nameText.grid(row=1, column=1)
    submit = Button(root, text="Submit", command=lambda: EditSubFct(nameText.get(),ind))
    submit.grid(row=2, column=0)
    back = Button(root, text="Back", command=main)
    back.grid(row=3, column=1)

def RmvSubFct(ind):
    del l[ind]
    main()


def RmvSubWnd(ind):
    clear_window()
    nameLabel = Label(root, text="Are you sure you want to delete subject '" + l[ind].name + "' ?")
    nameLabel.grid(row=0, column=0)
    yes = Button(root, text="Yes", command=lambda: RmvSubFct(ind))
    yes.grid(row=1, column=0)
    no = Button(root, text="No", command=main)
    no.grid(row=1, column=1)

def main():
    clear_window()

    for i in range(len(l)):
        subLabel = Label(root, text="Name: " + l[i].name)
        subLabel.grid(row=i,column=0)
        EditSub = Button(root, text="Edit This Subject", command= lambda: EditSubWnd(i))
        EditSub.grid(row=i, column=1)
        RmvSub = Button(root, text="Remove This Subject", command=lambda: RmvSubWnd(i))
        RmvSub.grid(row=i, column=2)

    AddSub = Button(root, text="Add A Subject", command = AddSubWnd)
    AddSub.grid(row=len(l)+1,column=0)


    root.mainloop()

main()