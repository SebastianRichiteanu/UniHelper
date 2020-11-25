from classes import *
from tkinter import *
from tkinter import messagebox as prompt
from tkcalendar import *
import tkinter.font as font
import pickle
import datetime
import webbrowser

global l, row, myFont
l = []
row = 0
l = pickle.load(open("save.p", "rb"))
root = Tk()
root.title('UniHelper')
root.geometry("800x800")
root.configure(bg='#282a36')
root.resizable(False, False)
Font = font.Font(family='Helvetica', size=13, weight='bold')
