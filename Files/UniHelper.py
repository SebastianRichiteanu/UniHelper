from functions import *


def AddSubFct(name, test, exam, v1, v2):
    if len(name) > 40:
        prompt_error("The name is too long (Max. 40 characters)")
    else:
        if v1.get():
            test = "not set yet"
        if v2.get():
            exam = "not set yet"
        if name != "":
            newSub = Subject(name=name, test=test, exam=exam)
            l.append(newSub)
            main()
        else:
            prompt_error()


def AddSubWnd():
    clear_window()

    submit = Button(root, text="Submit", width=39, height=1, font=Font, bg="#379c1a",
                    command=lambda: AddSubFct(nameText.get(), testCal.get_date(), examCal.get_date(), v1, v2))
    submit.grid(row=0, column=0)
    back = Button(root, text="Back", width=39, height=1, font=Font, bg="#ff5555", command=main)
    back.grid(row=0, column=1)

    nameLabel = Label(root, text="Name of the Subject:", background="#282a36", fg="white", font=Font)
    nameLabel.grid(row=1, column=0, pady=10)
    nameText = Entry(root, width=39, font=Font)
    nameText.grid(row=1, column=1)
    testLabel = Label(root, text="Date of the partial test:", background="#282a36", fg="white", font=Font)
    testLabel.grid(row=2, column=0, pady=10)
    testCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    testCal.grid(row=2, column=1, pady=10, sticky="nsew")
    examLabel = Label(root, text="Date of the exam:", background="#282a36", fg="white", font=Font)
    examLabel.grid(row=3, column=0)
    examCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    examCal.grid(row=3, column=1, pady=10, sticky="nsew")
    v1 = IntVar()
    testChk = Checkbutton(root, text="Partial not set yet", variable=v1, bg="#282a36", fg="#ffffff",
                          selectcolor="#000000", font=Font)
    testChk.grid(row=4, column=0, pady=10)
    v2 = IntVar()
    testChk = Checkbutton(root, text="Exam not set yet", variable=v2, bg="#282a36", fg="#ffffff",
                          selectcolor="#000000", font=Font)
    testChk.grid(row=4, column=1, pady=10)


def EditSubFct(name, test, exam, ind, v1, v2):
    if name == "":
        prompt_error("Name can't be null")
    else:
        if v1.get() == 1:
            test = l[ind].test
        if v2.get() == 1:
            exam = l[ind].exam
        if name == l[ind].name and test == l[ind].test and exam == l[ind].exam:
            prompt_error()
        else:
            l[ind].name = name
            l[ind].test = test
            l[ind].exam = exam
            OpenSub(ind)


def EditSubWnd(ind):
    clear_window()

    submit = Button(root, text="Submit", width=39, height=1, font=Font, bg="#379c1a",
                    command=lambda: EditSubFct(nameText.get(), testCal.get_date(), examCal.get_date(), ind, v1, v2))
    submit.grid(row=0, column=0)
    back = Button(root, text="Back", width=39, height=1, font=Font, bg="#ff5555", command=lambda: OpenSub(ind))
    back.grid(row=0, column=1)

    curNameLabel = Label(root, text="Current name of the Subject:",
                         background="#282a36", fg="white", font=Font)
    curNameLabel.grid(row=1, column=0, pady=5)
    curNameLabel2 = Label(root, text=l[ind].name, background="#282a36", fg="white", font=Font)
    curNameLabel2.grid(row=1, column=1)
    nameLabel = Label(root, text="New name for the Subject:", background="#282a36", fg="white", font=Font)
    nameLabel.grid(row=2, column=0)
    nameText = Entry(root, width=39, font=Font)
    nameText.insert(END, l[ind].name)
    nameText.grid(row=2, column=1)
    curTestLabel = Label(root, text="Current date of the Partial Test:",
                         background="#282a36", fg="white", font=Font)
    curTestLabel.grid(row=3, column=0, pady=7)
    curTestLabel = Label(root, text=l[ind].test, background="#282a36", fg="white", font=Font)
    curTestLabel.grid(row=3, column=1)
    testLabel = Label(root, text="New date for the partial test:", background="#282a36", fg="white", font=Font)
    testLabel.grid(row=4, column=0)
    c = return_date(l[ind].test)
    if c != -1:
        testCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy', day=c[0], month=c[1], year=c[2])
    else:
        testCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    testCal.grid(row=4, column=1, pady=10, sticky="nsew")

    curExamLabel = Label(root, text="Current date of the Exam:", background="#282a36",
                         fg="white", font=Font)
    curExamLabel.grid(row=5, column=0)
    curExamLabel2 = Label(root, text=l[ind].exam, background="#282a36", fg="white", font=Font)
    curExamLabel2.grid(row=5, column=1)
    examLabel = Label(root, text="New date for the exam:", background="#282a36", fg="white", font=Font)
    examLabel.grid(row=6, column=0)
    c = return_date(l[ind].exam)
    if c != -1:
        examCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy', day=c[0], month=c[1], year=c[2])
    else:
        examCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    examCal.grid(row=6, column=1, pady=10, sticky="nsew")
    v1 = IntVar()
    testChk = Checkbutton(root, text="Keep the old date for Partial Test", variable=v1, bg="#282a36", fg="#ffffff",
                          selectcolor="#000000", font=Font)
    testChk.grid(row=7, column=0, pady=20)
    v2 = IntVar()
    testChk = Checkbutton(root, text="Keep the old date for Exam", variable=v2, bg="#282a36", fg="#ffffff",
                          selectcolor="#000000", font=Font)
    testChk.grid(row=7, column=1, pady=20)


def RmvSubFct(ind):
    del l[ind]
    main()


def RmvSubWnd(ind):
    clear_window()
    nameLabel = Label(root, text="Are you sure you want to delete subject '" + l[ind].name + "' ?",
                      background="#282a36", fg="white", font=Font)
    nameLabel.grid(row=0, column=0, pady=10)
    canvas_ans = Canvas(root, width=800, height=50, highlightthickness=0, bg="#282a36")
    canvas_ans.grid_propagate(False)
    canvas_ans.grid(row=1, column=0, pady=30)
    yes = Button(canvas_ans, text="Yes", width=16, height=1, font=Font, bg="#379c1a",
                 command=lambda ind=ind: RmvSubFct(ind))
    yes.grid(row=0, column=0, padx=120)
    no = Button(canvas_ans, text="No", width=16, height=1, font=Font, bg="#ff5555",
                command=lambda ind=ind: OpenSub(ind))
    no.grid(row=0, column=1, padx=100)


def AddHwFct(ind, deadline, exerc, submit, v1):
    if v1.get() == 1 and exerc == "" and submit == "":
        prompt_error()
    else:
        if v1.get() == 1:
            deadline = "not set yet"
        if submit == "":
            submit = "not set yet"
        if exerc == "":
            exerc = "not set yet"
        newHw = Homework(deadline, exerc, submit)
        l[ind].hws.append(newHw)
        sort_hws(l[ind].hws)
        OpenSub(ind)


def AddHwWnd(ind):
    clear_window()
    submit = Button(root, text="Submit", width=39, height=1, font=Font, bg="#379c1a",
                    command=lambda ind=ind: AddHwFct(ind, deadlineCal.get_date(), exercText.get(), submitText.get(),
                                                     v1))
    submit.grid(row=0, column=0)
    back = Button(root, text="Back", width=39, height=1, font=Font, bg="#ff5555", command=lambda ind=ind: OpenSub(ind))
    back.grid(row=0, column=1)

    deadlineLabel = Label(root, text="Deadline: ", background="#282a36", fg="white", font=Font)
    deadlineLabel.grid(row=1, column=0)
    deadlineCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    deadlineCal.grid(row=1, column=1, sticky="nsew", pady=20)
    exercLabel = Label(root, text="Subjects (web link or plain text): ", background="#282a36", fg="white", font=Font)
    exercLabel.grid(row=2, column=0, pady=20)
    exercText = Entry(root, width=39, font=Font)
    exercText.grid(row=2, column=1, pady=20)
    submitLabel = Label(root, text="Where to Submit (web link or plain text): ", background="#282a36", fg="white",
                        font=Font)
    submitLabel.grid(row=3, column=0, pady=20)
    submitText = Entry(root, width=39, font=Font)
    submitText.grid(row=3, column=1, pady=20)

    v1 = IntVar()
    testChk = Checkbutton(root, text="Date not set yet", variable=v1, bg="#282a36", fg="#ffffff",
                          selectcolor="#000000", font=Font)
    testChk.grid(row=4, column=0, pady=20)


def EditHwFct(i, j, dl, ex, sub, v1):
    if (v1.get() == 1 or dl == l[i].hws[j].deadline) and ex == "" and sub == "":
        prompt_error()
    else:
        if v1.get() == 1:
            dl = l[i].hws[j].deadline
        if ex == "":
            ex = l[i].hws[j].exerc
        if sub == "":
            sub = l[i].hws[j].submit
        l[i].hws[j].deadline = dl
        l[i].hws[j].exerc = ex
        l[i].hws[j].submit = sub
        sort_hws(l[i].hws)
        OpenSub(i)


def EditHwWnd(hw, i, j):
    clear_window()
    submit = Button(root, text="Submit", width=39, height=1, font=Font, bg="#379c1a",
                    command=lambda i=i: EditHwFct(i, j, deadlineCal.get_date(), exercText.get(), submitText.get(), v1))
    submit.grid(row=0, column=0)
    back = Button(root, text="Back", width=39, height=1, font=Font, bg="#ff5555", command=lambda i=i: OpenSub(i))
    back.grid(row=0, column=1)
    deadlineLabel = Label(root, text="Current deadline: " + hw.deadline, background="#282a36",
                          fg="white", font=Font)
    deadlineLabel.grid(row=1, column=0)
    c = return_date(l[i].hws[j].deadline)
    if c != -1:
        deadlineCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy', day=c[0], month=c[1], year=c[2])
    else:
        deadlineCal = Calendar(root, selectmode="day", date_pattern='dd/mm/yy')
    deadlineCal.grid(row=1, column=1, sticky="nsew", pady=20)

    label_inter1 = Label(root, text="Subjects:", background="#282a36", fg="white", font=Font)
    label_inter1.grid(row=2, column=0)

    if hw.exerc[:4] == "http" or hw.exerc[:3] == "www":
        exercLabel = Label(root, text=split(hw.exerc), background="#282a36", fg="#6272a4", font=Font)
        exercLabel.bind("<Button-1>", lambda e: access_site(hw.exerc))
    else:
        exercLabel = Label(root, text=hw.exerc, background="#282a36", fg="white", font=Font)
    exercLabel.grid(row=3, column=0, pady=20)
    exercText = Entry(root, width=39, font=Font)
    exercText.insert(END, l[i].hws[j].exerc)
    exercText.grid(row=3, column=1, pady=20)

    label_inter1 = Label(root, text="Where to Submit:", background="#282a36", fg="white", font=Font)
    label_inter1.grid(row=4, column=0)

    if hw.submit[:4] == "http" or hw.submit[:3] == "www":
        submitLabel = Label(root, text=split(hw.submit), background="#282a36", fg="#6272a4", font=Font)
        submitLabel.bind("<Button-1>", lambda e: access_site(hw.submit))
    else:
        submitLabel = Label(root, text=hw.submit, background="#282a36", fg="white", font=Font)
    submitLabel.grid(row=5, column=0, pady=20)
    submitText = Entry(root, width=39, font=Font)
    submitText.insert(END, l[i].hws[j].submit)
    submitText.grid(row=5, column=1, pady=20)
    v1 = IntVar()
    testChk = Checkbutton(root, text="Keep the old deadline", variable=v1, bg="#282a36",
                          fg="#ffffff", selectcolor="#000000", font=Font)
    testChk.grid(row=6, column=0, pady=20)


def RmvHwFct(ind, j):
    del l[ind].hws[j]
    OpenSub(ind)


def RmvHwWnd(ind, j):
    clear_window()
    nameLabel = Label(root,
                      text="Are you sure you want to delete homework no." + str(j + 1) + " from subject '"
                           + l[ind].name + "'?", background="#282a36", fg="white", font=Font)
    nameLabel.grid(row=0, column=0, pady=10)
    canvas_ans = Canvas(root, width=800, height=50, highlightthickness=0, bg="#282a36")
    canvas_ans.grid_propagate(False)
    canvas_ans.grid(row=1, column=0, pady=30)
    yes = Button(canvas_ans, text="Yes", height=1, width=16, font=Font, bg="#379c1a", command=lambda: RmvHwFct(ind, j))
    yes.grid(row=1, column=0, padx=120)
    no = Button(canvas_ans, text="No", height=1, width=16, font=Font, bg="#ff5555", command=lambda: OpenSub(ind))
    no.grid(row=1, column=1, padx=100)


def OpenSub(ind):
    pickle.dump(l, open("save.p", "wb"))
    clear_window()
    canvas_top = Canvas(root, width=800, height=50, highlightthickness=0, bg="#282a36")
    canvas_top.pack()
    but_AddHw = Button(canvas_top, text="Add A Homework", width=40, height=1, font=Font, bg='#626AA4')
    but_AddHw.configure(command=lambda ind=ind: AddHwWnd(ind))
    but_AddHw.grid(row=0, column=0)
    but_Back = Button(canvas_top, text="Back", width=40, height=1, font=Font, bg='#AE8ABE', command=main)
    but_Back.grid(row=0, column=1)
    main_frame = Frame(root, bg="#282a36")
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(main_frame, bg="#282a36", highlightthickness=0)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    scroll.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=scroll.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = Frame(my_canvas, bg="#282a36")
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    subNameLabel = Label(second_frame, text="Name: " + l[ind].name, background="#282a36", fg="white", font=Font,
                         width=40)
    subNameLabel.grid(row=0, column=0)
    subTestLabel = Label(second_frame, text="Partial test date: " + l[ind].test, background="#282a36", fg="white",
                         font=Font)
    subTestLabel.grid(row=1, column=0)
    subExamLabel = Label(second_frame, text="Exam date: " + l[ind].exam, background="#282a36", fg="white", font=Font)
    subExamLabel.grid(row=2, column=0)
    row = 3
    if len(l[ind].hws) == 0:
        subHwLabel = Label(second_frame, text="No Homeworks ! :)", background="#282a36", fg="white", font=Font)
        subHwLabel.grid(row=row, column=0, pady=20)
    else:
        for j in range(len(l[ind].hws)):
            canvas_det = Canvas(second_frame, highlightthickness=0, bg="#282a36")
            canvas_det.grid(row=row, column=0, pady=20)
            sir1 = "HW NO " + str(j + 1) + " | Deadline: " + l[ind].hws[j].deadline
            sir2 = split(l[ind].hws[j].exerc)
            sir3 = split(l[ind].hws[j].submit)
            subHwLabel1 = Label(canvas_det, text=sir1, background="#282a36", fg="white", font=Font)
            subHwLabel1.grid(row=0, column=0)
            label_inter1 = Label(canvas_det, text="Subjects:", background="#282a36", fg="white", font=Font)
            label_inter1.grid(row=1, column=0)
            if sir2[:4] == "http" or sir2[:3] == "www":
                subHwLabel2 = Label(canvas_det, text=sir2, background="#282a36", fg="#626AA4", font=Font)
                subHwLabel2.bind("<Button-1>", lambda e: access_site(l[ind].hws[j].exerc))
            else:
                subHwLabel2 = Label(canvas_det, text=sir2, background="#282a36", fg="white", font=Font)
            subHwLabel2.grid(row=2, column=0)

            label_inter1 = Label(canvas_det, text="Where to Submit:", background="#282a36", fg="white", font=Font)
            label_inter1.grid(row=3, column=0)

            if sir3[:4] == "http" or sir3[:3] == "www":
                subHwLabel3 = Label(canvas_det, text=sir3, background="#282a36", fg="#626AA4", font=Font)
                subHwLabel3.bind("<Button-1>", lambda e: access_site(l[ind].hws[j].submit))
            else:
                subHwLabel3 = Label(canvas_det, text=sir3, background="#282a36", fg="white", font=Font)
            subHwLabel3.grid(row=4, column=0)

            editHwButton = Button(second_frame, text="Edit This HW", width=16, height=1, font=Font,
                                  bg="#379c1a", command=lambda ind=ind: EditHwWnd(l[ind].hws[j], ind, j))
            editHwButton.grid(row=row, column=1, padx=10)
            remHwButton = Button(second_frame, text="Remove This HW", width=16, height=1, font=Font,
                                 bg="#ff5555", command=lambda ind=ind: RmvHwWnd(ind, j))
            remHwButton.grid(row=row, column=2, padx=10)
            row += 4
    row += 1

    canvas_down = Canvas(root, width=800, height=50, highlightthickness=0, bg="#282a36")
    canvas_down.pack()

    but_Edit = Button(canvas_down, text="Edit This Subject", bg='#379c1a')
    but_Edit.configure(width=40, height=1, font=Font, command=lambda ind=ind: EditSubWnd(ind))
    but_Edit.grid(row=0, column=0)

    but_Rem = Button(canvas_down, text="Remove This Subject", bg='#ff5555')
    but_Rem.configure(width=40, height=1, font=Font, command=lambda ind=ind: RmvSubWnd(ind))
    but_Rem.grid(row=0, column=1)


def main():
    clear_window()
    pickle.dump(l, open("save.p", "wb"))
    ev_color = {}
    ev_color.clear()
    ev_text = {}
    ev_text.clear()
    load_events_color(ev_color)
    load_events_text(ev_text)
    canvas_main = Canvas(root, width=800, height=400, highlightthickness=0, bg="#282a36")
    canvas_main.pack()
    firstLabel = Label(canvas_main, text="Subjects:", background="#282a36", fg="white",
                       width=40, height=1, font=Font)
    firstLabel.grid(row=0, column=0)
    AddSub = Button(canvas_main, text="Add A Subject", command=AddSubWnd, width=40,
                    height=1, bg='#626AA4', font=Font)
    AddSub.grid(row=0, column=1)

    if len(l) == 0:
        canvas_main.grid_propagate(False)
        firstLabel2 = Label(canvas_main, text="No Subjects added yet", background="#282a36")
        firstLabel2.configure(fg="white", width=40, height=1, font=Font)
        firstLabel2.grid(row=1, column=0)
    else:
        canvas_main.grid_propagate(True)
        main_frame = Frame(root, bg="#282a36")
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame, bg="#282a36", highlightthickness=0)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        scroll = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        scroll.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas, bg="#282a36")
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
        row = 1
        for i in range(len(l)):
            subLabel = Label(second_frame, text=l[i].name, width=40)
            subLabel.configure(background="#282a36", fg="white", font=Font)
            subLabel.grid(row=row, column=0)
            OpenSb = Button(second_frame, text="Open This Subject")
            OpenSb.configure(command=lambda i=i: OpenSub(i), bg='#AE8ABE', width=37, height=1, font=Font)
            OpenSb.grid(row=row, column=1)
            row += 1

    canvas_cal = Canvas(root, width=800, height=400, highlightthickness=0)
    canvas_cal.pack_propagate(False)
    canvas_cal.pack()

    cal = Calendar(canvas_cal, selectmode="day", date_pattern='dd/mm/yy'
                   , tooltipdelay=2, tooltipalpha=0.8, selectbackground="white",
                   selectforeground="black", weekendbackground="white", weekendforeground="black",
                   othermonthbackground="#DCDCDC", othermonthwebackground="#DCDCDC")
    cal.pack(expand=True, fill='both')
    for ev in ev_color:
        data = create_date(ev)
        txt = ev_text[ev]
        cal.calevent_create(data, txt, ev)
        if ev_color[ev] == 1:
            cal.tag_config(ev, background='yellow', foreground='black')
        elif ev_color[ev] == 2:
            cal.tag_config(ev, background='orange', foreground='black')
        else:
            cal.tag_config(ev, background='red', foreground='black')
    root.mainloop()


main()
