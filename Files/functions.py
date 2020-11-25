from globals import *


def clear_window():
    l = root.winfo_children()
    for x in l:
        x.destroy()


def sort_hws(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i].deadline[0] == 'n' and l[j].deadline[0] != 'n':
                l[i], l[j] = l[j], l[i]
            elif l[i].deadline[0] != 'n' and l[j].deadline[0] != 'n':
                zi = int(l[i].deadline[0]) * 10 + int(l[i].deadline[1])
                zj = int(l[j].deadline[0]) * 10 + int(l[j].deadline[1])
                li = int(l[i].deadline[3]) * 10 + int(l[i].deadline[4])
                lj = int(l[j].deadline[3]) * 10 + int(l[j].deadline[4])
                yi = int(l[i].deadline[6]) * 10 + int(l[i].deadline[7])
                yj = int(l[j].deadline[6]) * 10 + int(l[j].deadline[7])
                if yi > yj:
                    l[i], l[j] = l[j], l[i]
                elif yi == yj and li > lj:
                    l[i], l[j] = l[j], l[i]
                elif yi == yj and li == lj and zi > zj:
                    l[i], l[j] = l[j], l[i]


def return_date(sir):
    if sir[0] == 'n':
        return -1
    t = [0, 0, 0]
    t[0] = int(sir[0]) * 10 + int(sir[1])
    t[1] = int(sir[3]) * 10 + int(sir[4])
    t[2] = int(sir[6]) * 10 + int(sir[7])
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


def access_site(sir):
    webbrowser.open_new(sir)


def create_date(sir):
    if sir[0] == 'n':
        return -1
    d = int(sir[0]) * 10 + int(sir[1])
    m = int(sir[3]) * 10 + int(sir[4])
    y = int(sir[6]) * 10 + int(sir[7])
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
