from functions import *


def AddSubFct(name, test, exam, v1, v2):
    if len(name) > 40:
        prompt_error("The name is too long (Max. 40 characters)")
        return
    if name == "":
        prompt_error("Name can't be null")
        return
    if v1.get():
        test = nsy
    if v2.get():
        exam = nsy

    newSub = Subject(name=name, test=test, exam=exam)
    l.append(newSub)
    pickle.dump(l, open("save.p", "wb"))
    add_event(exam, 0, name)
    add_event(test, 1, name)
    main()


def AddSubWnd():
    clear_window()

    submit = Button(root, text="Submit", width=width['add_sub'], height=height['top'], font=Font, bg=colors['submit'],
                    command=lambda: AddSubFct(nameText.get(), testCal.get_date(), examCal.get_date(), v1, v2))
    submit.grid(row=0, column=0)

    back = Button(root, text="Back", width=width['add_sub'],
                  height=height['top'], font=Font, bg=colors['back'], command=main)
    back.grid(row=0, column=1)

    nameLabel = Label(root, text="Name of the Subject:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    nameLabel.grid(row=1, column=0, pady=10)

    nameText = Entry(root, width=width['add_sub'], font=Font)
    nameText.grid(row=1, column=1)

    testLabel = Label(root, text="Date of the partial test:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    testLabel.grid(row=2, column=0, pady=10)

    testCal = Calendar(root, selectmode="day", date_pattern=dp)
    testCal.grid(row=2, column=1, pady=10, sticky="nsew")

    examLabel = Label(root, text="Date of the exam:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    examLabel.grid(row=3, column=0)

    examCal = Calendar(root, selectmode="day", date_pattern=dp)
    examCal.grid(row=3, column=1, pady=10, sticky="nsew")

    v1 = IntVar()
    testChk = Checkbutton(root, text="Partial " + nsy, variable=v1, bg=colors['bg'], fg=colors['chk_fg'],
                          selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=4, column=0, pady=10)

    v2 = IntVar()
    testChk = Checkbutton(root, text="Exam " + nsy, variable=v2, bg=colors['bg'], fg=colors['chk_fg'],
                          selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=4, column=1, pady=10)


def EditSubFct(name, test, exam, ind, v1, v2):
    if name == "":
        prompt_error("Name can't be null")
        return
    if name == l[ind].name and test == l[ind].test and exam == l[ind].exam:
        prompt_error()
        return

    if v1.get() == 1:
        test = l[ind].test
    else:
        remove_event(l[ind].test, 1, name)
        add_event(test, 1, name)
    if v2.get() == 1:
        exam = l[ind].exam
    else:
        remove_event(l[ind].exam, 0, name)
        add_event(exam, 0, name)

    l[ind].name = name
    l[ind].test = test
    l[ind].exam = exam
    pickle.dump(l, open("save.p", "wb"))

    OpenSub(ind)


def EditSubWnd(ind):
    clear_window()

    submit = Button(root, text="Submit", width=width['edit_sub'], height=height['top'], font=Font, bg=colors['submit'],
                    command=lambda: EditSubFct(nameText.get(), testCal.get_date(), examCal.get_date(), ind, v1, v2))
    submit.grid(row=0, column=0)

    back = Button(root, text="Back", width=width['edit_sub'], height=height['top'],
                  font=Font, bg=colors['back'], command=lambda: OpenSub(ind))
    back.grid(row=0, column=1)

    curNameLabel = Label(root, text="Current name of the Subject:",
                         background=colors['bg'], fg=colors['label_fg'], font=Font)
    curNameLabel.grid(row=1, column=0, pady=5)
    curNameLabel2 = Label(
        root, text=l[ind].name, background=colors['bg'], fg=colors['label_fg'], font=Font)
    curNameLabel2.grid(row=1, column=1)

    nameLabel = Label(root, text="New name for the Subject:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    nameLabel.grid(row=2, column=0)

    nameText = Entry(root, width=width['edit_sub'], font=Font)
    nameText.insert(END, l[ind].name)
    nameText.grid(row=2, column=1)

    curTestLabel = Label(root, text="Current date of the Partial Test:",
                         background=colors['bg'], fg=colors['label_fg'], font=Font)
    curTestLabel.grid(row=3, column=0, pady=7)
    curTestLabel2 = Label(root, text=format_date(
        l[ind].test), background=colors['bg'], fg=colors['label_fg'], font=Font)
    curTestLabel2.grid(row=3, column=1)

    testLabel = Label(root, text="New date for the partial test:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    testLabel.grid(row=4, column=0)

    c = return_date(l[ind].test)
    if c != -1:
        testCal = Calendar(root, selectmode="day",
                           date_pattern=dp, day=c[0], month=c[1], year=c[2])
    else:
        testCal = Calendar(root, selectmode="day", date_pattern=dp)
    testCal.grid(row=4, column=1, pady=10, sticky="nsew")

    curExamLabel = Label(root, text="Current date of the Exam:", background=colors['bg'],
                         fg=colors['label_fg'], font=Font)
    curExamLabel.grid(row=5, column=0)
    curExamLabel2 = Label(root, text=format_date(
        l[ind].exam), background=colors['bg'], fg=colors['label_fg'], font=Font)
    curExamLabel2.grid(row=5, column=1)

    examLabel = Label(root, text="New date for the exam:",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    examLabel.grid(row=6, column=0)

    c = return_date(l[ind].exam)
    if c != -1:
        examCal = Calendar(root, selectmode="day",
                           date_pattern=dp, day=c[0], month=c[1], year=c[2])
    else:
        examCal = Calendar(root, selectmode="day", date_pattern=dp)
    examCal.grid(row=6, column=1, pady=10, sticky="nsew")

    v1 = IntVar()
    testChk = Checkbutton(root, text="Keep the old date for Partial Test", variable=v1, bg=colors['bg'], fg=colors['chk_fg'],
                          selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=7, column=0, pady=20)

    v2 = IntVar()
    testChk = Checkbutton(root, text="Keep the old date for Exam", variable=v2, bg=colors['bg'], fg=colors['chk_fg'],
                          selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=7, column=1, pady=20)


def RmvSubFct(ind):
    remove_event(l[ind].exam, 0, l[ind].name)
    remove_event(l[ind].test, 1, l[ind].name)
    del l[ind]
    pickle.dump(l, open("save.p", "wb"))
    main()


def RmvSubWnd(ind):
    clear_window()

    nameLabel = Label(root, text="Are you sure you want to delete subject '" + l[ind].name + "' ?",
                      background=colors['bg'], fg=colors['label_fg'], font=Font)
    nameLabel.grid(row=0, column=0, pady=10)

    canvas_ans = Canvas(
        root, width=width['full'], height=height["canvas_top"], highlightthickness=0, bg=colors['bg'])
    canvas_ans.grid_propagate(False)
    canvas_ans.grid(row=1, column=0, pady=30)

    yes = Button(canvas_ans, text="Yes", width=width['yes_no'], height=height['mid'], font=Font, bg=colors['yes'],
                 command=lambda ind=ind: RmvSubFct(ind))
    yes.grid(row=0, column=0, padx=120)

    no = Button(canvas_ans, text="No", width=width['yes_no'], height=height['mid'], font=Font, bg=colors['no'],
                command=lambda ind=ind: OpenSub(ind))
    no.grid(row=0, column=1, padx=100)


def AddHwFct(ind, deadline, exerc, submit, v1):
    if v1.get() == 1 and exerc == "" and submit == "":
        prompt_error()
        return
    if v1.get() == 1:
        deadline = nsy
    if submit == "":
        submit = nsy
    if exerc == "":
        exerc = nsy

    newHw = Homework(deadline, exerc, submit)
    l[ind].hws.append(newHw)
    sort_hws(l[ind].hws)
    pickle.dump(l, open("save.p", "wb"))
    add_event(deadline, 2, l[ind].name)
    OpenSub(ind)


def AddHwWnd(ind):
    clear_window()

    submit = Button(root, text="Submit", width=width['add_hw'], height=height['top'], font=Font, bg=colors['submit'],
                    command=lambda ind=ind: AddHwFct(ind, deadlineCal.get_date(), exercText.get(), submitText.get(),
                                                     v1))
    submit.grid(row=0, column=0)

    back = Button(root, text="Back", width=width['add_hw'], height=height['top'],
                  font=Font, bg=colors['back'], command=lambda ind=ind: OpenSub(ind))
    back.grid(row=0, column=1)

    deadlineLabel = Label(root, text="Deadline: ",
                          background=colors['bg'], fg=colors['label_fg'], font=Font)
    deadlineLabel.grid(row=1, column=0)

    deadlineCal = Calendar(root, selectmode="day", date_pattern=dp)
    deadlineCal.grid(row=1, column=1, sticky="nsew", pady=20)

    exercLabel = Label(root, text="Subjects (web link or plain text): ",
                       background=colors['bg'], fg=colors['label_fg'], font=Font)
    exercLabel.grid(row=2, column=0, pady=20)

    exercText = Entry(root, width=width['add_hw'], font=Font)
    exercText.grid(row=2, column=1, pady=20)

    submitLabel = Label(root, text="Where to Submit (web link or plain text): ", background=colors['bg'], fg=colors['label_fg'],
                        font=Font)
    submitLabel.grid(row=3, column=0, pady=20)

    submitText = Entry(root, width=width['add_hw'], font=Font)
    submitText.grid(row=3, column=1, pady=20)

    v1 = IntVar()
    testChk = Checkbutton(root, text="Date " + nsy, variable=v1, bg=colors['bg'], fg=colors['chk_fg'],
                          selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=4, column=0, pady=20)


def EditHwFct(i, j, dl, ex, sub, v1):
    if (v1.get() == 1 or dl == l[i].hws[j].deadline) and ex == "" and sub == "":
        prompt_error()
        return
    if v1.get() == 1:
        dl = l[i].hws[j].deadline
    else:
        remove_event(l[i].hws[j].deadline, 2, l[i].name)
        add_event(dl, 2, l[i].name)
    if ex == "":
        ex = l[i].hws[j].exerc
    if sub == "":
        sub = l[i].hws[j].submit
    l[i].hws[j].deadline = dl
    l[i].hws[j].exerc = ex
    l[i].hws[j].submit = sub
    sort_hws(l[i].hws)
    pickle.dump(l, open("save.p", "wb"))
    OpenSub(i)


def EditHwWnd(hw, i, j):
    clear_window()

    submit = Button(root, text="Submit", width=width['edit_hw'], height=height['top'], font=Font, bg=colors['submit'],
                    command=lambda i=i: EditHwFct(i, j, deadlineCal.get_date(), exercText.get(), submitText.get(), v1))
    submit.grid(row=0, column=0)

    back = Button(root, text="Back", width=width['edit_hw'], height=height['top'],
                  font=Font, bg=colors['back'], command=lambda i=i: OpenSub(i))
    back.grid(row=0, column=1)

    deadlineLabel = Label(root, text="Current deadline: " + format_date(hw.deadline), background=colors['bg'],
                          fg=colors['label_fg'], font=Font)
    deadlineLabel.grid(row=1, column=0)

    c = return_date(l[i].hws[j].deadline)
    if c != -1:
        deadlineCal = Calendar(root, selectmode="day",
                               date_pattern=dp, day=c[0], month=c[1], year=c[2])
    else:
        deadlineCal = Calendar(root, selectmode="day", date_pattern=dp)
    deadlineCal.grid(row=1, column=1, sticky="nsew", pady=20)

    label_inter1 = Label(root, text="Subjects:",
                         background=colors['bg'], fg=colors['label_fg'], font=Font)
    label_inter1.grid(row=2, column=0)

    if verif_site(hw.exerc):
        exercLabel = Label(root, text=split(
            hw.exerc), background=colors['bg'], fg=colors['link'], font=Font)
        exercLabel.bind("<Button-1>", lambda e: access_site(hw.exerc))
    else:
        exercLabel = Label(
            root, text=hw.exerc, background=colors['bg'], fg=colors['label_fg'], font=Font)
    exercLabel.grid(row=3, column=0, pady=20)

    exercText = Entry(root, width=width['edit_hw'], font=Font)
    exercText.insert(END, l[i].hws[j].exerc)
    exercText.grid(row=3, column=1, pady=20)

    label_inter1 = Label(root, text="Where to Submit:",
                         background=colors['bg'], fg=colors['label_fg'], font=Font)
    label_inter1.grid(row=4, column=0)

    if verif_site(hw.submit):
        submitLabel = Label(root, text=split(
            hw.submit), background=colors['bg'], fg=colors['link'], font=Font)
        submitLabel.bind("<Button-1>", lambda e: access_site(hw.submit))
    else:
        submitLabel = Label(
            root, text=hw.submit, background=colors['bg'], fg=colors['label_fg'], font=Font)
    submitLabel.grid(row=5, column=0, pady=20)

    submitText = Entry(root, width=width['edit_hw'], font=Font)
    submitText.insert(END, l[i].hws[j].submit)
    submitText.grid(row=5, column=1, pady=20)

    v1 = IntVar()
    testChk = Checkbutton(root, text="Keep the old deadline", variable=v1, bg=colors['bg'],
                          fg=colors['chk_fg'], selectcolor=colors['chk_sel'], font=Font)
    testChk.grid(row=6, column=0, pady=20)


def RmvHwFct(ind, j):
    remove_event(l[ind].hws[j].deadline, 2, l[ind].name)
    del l[ind].hws[j]
    pickle.dump(l, open("save.p", "wb"))
    OpenSub(ind)


def RmvHwWnd(ind, j):
    clear_window()

    nameLabel = Label(root,
                      text="Are you sure you want to delete homework no." +
                      str(j + 1) + " from subject '"
                      + l[ind].name + "'?", background=colors['bg'], fg=colors['label_fg'], font=Font)
    nameLabel.grid(row=0, column=0, pady=10)

    canvas_ans = Canvas(
        root, width=width['full'], height=height['canvas_top'], highlightthickness=0, bg=colors['bg'])
    canvas_ans.grid_propagate(False)
    canvas_ans.grid(row=1, column=0, pady=30)

    yes = Button(canvas_ans, text="Yes", height=height['mid'], width=width['yes_no'],
                 font=Font, bg=colors['yes'], command=lambda: RmvHwFct(ind, j))
    yes.grid(row=1, column=0, padx=120)

    no = Button(canvas_ans, text="No", height=height['mid'], width=width['yes_no'],
                font=Font, bg=colors['no'], command=lambda: OpenSub(ind))
    no.grid(row=1, column=1, padx=100)


def OpenSub(ind):
    clear_window()

    canvas_top = Canvas(
        root, width=width['full'], height=height['canvas_top'], highlightthickness=0, bg=colors['bg'])
    canvas_top.pack()

    but_AddHw = Button(canvas_top, text="Add A Homework",
                       width=width['open_sub'], height=height['top'], font=Font, bg=colors['add'])
    but_AddHw.configure(command=lambda ind=ind: AddHwWnd(ind))
    but_AddHw.grid(row=0, column=0)

    but_Back = Button(canvas_top, text="Back",
                      width=width['open_sub'], height=height['top'], font=Font, bg=colors['open'], command=main)
    but_Back.grid(row=0, column=1)

    main_frame = Frame(root, bg=colors['bg'])
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame, bg=colors['bg'], highlightthickness=0)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    scroll.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas, bg=colors['bg'])
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    subNameLabel = Label(second_frame, text="Name: " + l[ind].name, background=colors['bg'], fg=colors['label_fg'], font=Font,
                         width=width['open_sub'])
    subNameLabel.grid(row=0, column=0)

    subTestLabel = Label(second_frame, text="Partial test date: " + format_date(l[ind].test), background=colors['bg'], fg=colors['label_fg'],
                         font=Font)
    subTestLabel.grid(row=1, column=0)

    subExamLabel = Label(second_frame, text="Exam date: " + format_date(
        l[ind].exam), background=colors['bg'], fg=colors['label_fg'], font=Font)
    subExamLabel.grid(row=2, column=0)

    row = 3
    if len(l[ind].hws) == 0:
        subHwLabel = Label(second_frame, text="No Homeworks ! :)",
                           background=colors['bg'], fg=colors['label_fg'], font=Font)
        subHwLabel.grid(row=row, column=0, pady=20)
    else:
        for j in range(len(l[ind].hws)):
            canvas_det = Canvas(
                second_frame, highlightthickness=0, bg=colors['bg'])
            canvas_det.grid(row=row, column=0, pady=20)

            sir1 = "HW NO " + str(j + 1) + " | Deadline: " + \
                format_date(l[ind].hws[j].deadline)
            sir2 = split(l[ind].hws[j].exerc)
            sir3 = split(l[ind].hws[j].submit)

            subHwLabel1 = Label(
                canvas_det, text=sir1, background=colors['bg'], fg=colors['label_fg'], font=Font)
            subHwLabel1.grid(row=0, column=0)

            label_inter1 = Label(canvas_det, text="Subjects:",
                                 background=colors['bg'], fg=colors['label_fg'], font=Font)
            label_inter1.grid(row=1, column=0)

            if verif_site(sir2):
                subHwLabel2 = Label(
                    canvas_det, text=sir2, background=colors['bg'], fg=colors['link'], font=Font)
                subHwLabel2.bind(
                    "<Button-1>", lambda e: access_site(l[ind].hws[j].exerc))
            else:
                subHwLabel2 = Label(
                    canvas_det, text=sir2, background=colors['bg'], fg=colors['label_fg'], font=Font)
            subHwLabel2.grid(row=2, column=0)

            label_inter1 = Label(canvas_det, text="Where to Submit:",
                                 background=colors['bg'], fg=colors['label_fg'], font=Font)
            label_inter1.grid(row=3, column=0)

            if verif_site(sir3):
                subHwLabel3 = Label(
                    canvas_det, text=sir3, background=colors['bg'], fg=colors['link'], font=Font)
                subHwLabel3.bind(
                    "<Button-1>", lambda e: access_site(l[ind].hws[j].submit))
            else:
                subHwLabel3 = Label(
                    canvas_det, text=sir3, background=colors['bg'], fg=colors['label_fg'], font=Font)
            subHwLabel3.grid(row=4, column=0)

            editHwButton = Button(second_frame, text="Edit This HW", width=width['open_sub_mid'], height=height['mid'], font=Font,
                                  bg=colors['edit'], command=lambda ind=ind: EditHwWnd(l[ind].hws[j], ind, j))
            editHwButton.grid(row=row, column=1, padx=10)

            remHwButton = Button(second_frame, text="Remove This HW", width=width['open_sub_mid'], height=height['mid'], font=Font,
                                 bg=colors['remove'], command=lambda ind=ind: RmvHwWnd(ind, j))
            remHwButton.grid(row=row, column=2, padx=10)

            row += 4

    canvas_down = Canvas(
        root, width=width['full'], height=height['canvas_down'], highlightthickness=0, bg=colors['bg'])
    canvas_down.pack()

    but_Edit = Button(canvas_down, text="Edit This Subject", bg=colors['edit'])
    but_Edit.configure(width=width['open_sub'], height=height['down'],
                       font=Font, command=lambda ind=ind: EditSubWnd(ind))
    but_Edit.grid(row=0, column=0)

    but_Rem = Button(canvas_down, text="Remove This Subject",
                     bg=colors['remove'])
    but_Rem.configure(width=width['open_sub'], height=height['down'],
                      font=Font, command=lambda ind=ind: RmvSubWnd(ind))
    but_Rem.grid(row=0, column=1)


def main():
    clear_window()

    canvas_main = Canvas(
        root, width=width['full'], height=height['canvas_half'], highlightthickness=0, bg=colors['bg'])
    canvas_main.pack()

    firstLabel = Label(canvas_main, text="Subjects:", background=colors['bg'], fg=colors['label_fg'],
                       width=width['main'], height=height['top'], font=Font)
    firstLabel.grid(row=0, column=0)

    AddSub = Button(canvas_main, text="Add A Subject", command=AddSubWnd, width=width['main'],
                    height=height['top'], bg=colors['add'], font=Font)
    AddSub.grid(row=0, column=1)

    if len(l) == 0:
        canvas_main.grid_propagate(False)
        firstLabel2 = Label(
            canvas_main, text="No Subjects added yet", background=colors['bg'])
        firstLabel2.configure(
            fg=colors['label_fg'], width=width['main'], height=height['mid'], font=Font)
        firstLabel2.grid(row=1, column=0)
    else:
        canvas_main.grid_propagate(True)

        main_frame = Frame(root, bg=colors['bg'])
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame, bg=colors['bg'], highlightthickness=0)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scroll = Scrollbar(main_frame, orient=VERTICAL,
                           command=my_canvas.yview)
        scroll.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
            scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas, bg=colors['bg'])
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        row = 1
        for i in range(len(l)):
            subLabel = Label(second_frame, text=l[i].name, width=width['main'])
            subLabel.configure(
                background=colors['bg'], fg=colors['label_fg'], font=Font)
            subLabel.grid(row=row, column=0)

            OpenSb = Button(second_frame, text="Open This Subject")
            OpenSb.configure(command=lambda i=i: OpenSub(
                i), bg=colors['open'], width=width['main'], height=height['mid'], font=Font)
            OpenSb.grid(row=row, column=1)

            row += 1

    canvas_cal = Canvas(
        root, width=width['full'], height=height['canvas_half'], highlightthickness=0)
    canvas_cal.pack_propagate(False)
    canvas_cal.pack()

    cal = Calendar(canvas_cal, selectmode="none", date_pattern=dp,
                   tooltipdelay=2, tooltipalpha=0.8,
                   weekendbackground="white", weekendforeground="black", selectbackground="white",
                   selectforeground="black",
                   othermonthbackground="#DCDCDC", othermonthwebackground="#DCDCDC")
    cal.pack(expand=True, fill='both')

    for ev in events:
        data = create_date(ev)
        txt = ""
        for x in events[ev][0]:
            txt += "Exam for " + x + '\n'
        for x in events[ev][1]:
            txt += "Test for " + x + '\n'
        for x in events[ev][2]:
            txt += "Homework for " + x + '\n'
        cal.calevent_create(data, txt, ev)
        if events[ev][0]:
            cal.tag_config(ev, background=colors['exam'], foreground='black', selectbackground=colors['exam'],
                           selectforeground="black")
        elif events[ev][1]:
            cal.tag_config(ev, background=colors['test'], foreground='black', selectbackground=colors['test'],
                           selectforeground="black")
        else:
            cal.tag_config(ev, background=colors['homework'], foreground='black', selectbackground=colors['homework'],
                           selectforeground="black")

    root.mainloop()


main()
