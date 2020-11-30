from globals import *


def clear_window():
    l = root.winfo_children()
    for x in l:
        x.destroy()


def sort_hws(l):
    l.sort(key=lambda hm: hm.deadline)


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


def add_event(data, type, name):
    if data[0] == 'n':
        return
    if data not in events.keys():
        events[data] = ([], [], [])
    events[data][type].append(name)
    pickle.dump(events, open("save_ev.p", "wb"))


def remove_event(data, type, name):
    if data[0] == 'n':
        return
    events[data][type].remove(name)
    if (not events[data][0]) and (not events[data][1]) and (not events[data][2]):
        del events[data]
    pickle.dump(events, open("save_ev.p", "wb"))
