from classes import *
from tkinter import *
from tkinter import messagebox as prompt
from tkcalendar import *
import tkinter.font as font
import pickle
import datetime
import webbrowser

global l, row, myFont,colors,height,width,nsy 
l = []
row = 0
l = pickle.load(open("save.p", "rb"))
root = Tk()
root.title('UniHelper')
root.geometry("800x800")
root.configure(bg='#282a36')
root.resizable(False, False)
Font = font.Font(family='Helvetica', size=13, weight='bold')

nsy = "not set yet"

colors = {  
    "bg":"#282a36",
    "add":"#626AA4",
    "open":"#AE8ABE",
    "edit":"#379c1a",
    "remove":"#ff5555",
    "submit":"#379c1a",
    "back":"#ff5555",
    "yes":"#379c1a",
    "no":"#ff5555",
	"link":"#6272a4",
    "label_fg":"white",
    "exam":"red",
    "test":"orange",
    "homework":"yellow",
    "chk_fg":"white",
    "chk_sel":"black"}

height = {  
    "top":1,
    "down":1,
    "mid":1,
	"canvas_top":50,
    "canvas_down":50,
	"canvas_half":400}

width = {
    "main":40,
    "open_sub":40,
    "open_sub_mid":16,
    "add_sub":39,
    "edit_sub":39,
    "add_hw":39,
    "edit_hw":39,
    "full":800,
    "yes_no":16
}
