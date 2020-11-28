from globals import *

def clear_window():
    l = root.winfo_children()
    for x in l:
        x.destroy()

def sort_hws(l):
    l.sort(key = lambda hm: hm.deadline)

def format_date(sir):
    if sir[0] == 'n':
        return sir
    else:
        sir2 = sir[6]+sir[7]+sir[2]+sir[3]+sir[4]+sir[5]+sir[0]+sir[1]
        return sir2

def return_date(sir):
    if sir[0] == 'n':
        return -1
    t = [0, 0, 0]
    t[0] = int(sir[6]) * 10 + int(sir[7])
    t[1] = int(sir[3]) * 10 + int(sir[4])
    t[2] = int(sir[0]) * 10 + int(sir[1]) + 2000
    return t


def prompt_error(sir="Not enough parameters changed"):
    prompt.showerror("Error", sir)


def split(sir):
    s = ""
    while len(sir) > 35:
        s += sir[:40] + "\n"
        sir = sir[40:]
    s += sir
    return s

def verif_site(sir):
    if sir[:4] == "http" or sir[:3] == "www":
        return 1
    return 0

def access_site(sir):
    webbrowser.open_new(sir)


def create_date(sir):
    if sir[0] == 'n':
        return -1
    d = int(sir[6]) * 10 + int(sir[7])
    m = int(sir[3]) * 10 + int(sir[4])
    y = int(sir[0]) * 10 + int(sir[1])
    y += 2000
    dat = datetime.date(y, m, d)
    return dat


def add_event(dict, date, col):
    if date[0] != 'n':
        dict[date] = col


def load_events_color(dict):
    for sub in l:
        for hm in sub.hws:
            if hm.deadline not in dict:
                add_event(dict, hm.deadline, 1)
        if sub.test not in dict or (sub.test in dict and dict[sub.test] < 2):
            add_event(dict, sub.test, 2)
        if sub.exam not in dict or (sub.exam in dict and dict[sub.exam] < 3):
            add_event(dict, sub.exam, 3)


def load_events_text(dict):
    for sub in l:
        if sub.exam[0] != 'n':
            sir = ""
            if sub.exam in dict.keys():
                sir = dict[sub.exam] + '\n'
            sir += "Exam for " + sub.name
            dict[sub.exam] = sir
    for sub in l:
        if sub.test[0] != 'n':
            sir = ""
            if sub.test in dict.keys():
                sir = dict[sub.test] + '\n'
            sir += "Partial test for " + sub.name
            dict[sub.test] = sir
    for sub in l:
        for i in range(len(sub.hws)):
            hm = sub.hws[i]
            sir = ""
            if hm.deadline != 'n':
                if hm.deadline in dict.keys():
                    sir = dict[hm.deadline] + '\n'
                sir += "Homework " + str(i + 1) + " for " + sub.name
                dict[hm.deadline] = sir
