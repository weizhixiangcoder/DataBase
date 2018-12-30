from tkinter import *
import sys, os
os.chdir("..")
s = os.getcwd()
sys.path.append(s + "\\Library")
import database as db


def delete():
    """
    Название: Удаление выбранного пользователя из базы данных
    Входные данные: -
    Возвращаемые данные: -
    Автор: Приходько Д.С., Кудрявцев Д.А.
    """
    listSelection.delete(0, END)
    selection = listBox.curselection()
    if selection:
        value = listBox.get(selection)
        listBox.delete(selection[0])
        db.deletePerson(db.base, value)
    else:
        listSelection.insert(END, "Выберите пользователя")


def add():
    """
    Название: Добавление пользователя в базу данных и в таблицу визуализации
    Входные данные: -
    Возвращаемые данные: -
    Автор: Келлер В.А., Приходько Д.С., Кудрявцев Д.А.
    """
    listSelection.delete(0, END)
    root = Tk()
    root.geometry("320x250")
    root.title("Добавить пользователя")
    root.configure(bg='lightgrey')

    field = ["Фамилия Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
    x1 = 20
    y1 = 20
    for i in field:
        lbl = Label(root, text=i, font=("Helvetica", 12))
        lbl.configure(bg='lightgrey')
        lbl.place(x=x1, y=y1)
        y1 += 30
    x1 = 140
    y1 = 20
    nameInput = Entry(root, width=20)
    nameInput.place(x=x1, y=y1)
    y1 += 30
    genderInput = Entry(root, width=20)
    genderInput.place(x=x1, y=y1)
    y1 += 30
    ageInput = Entry(root, width=20)
    ageInput.place(x=x1, y=y1)
    y1 += 30
    mailInput = Entry(root, width=20)
    mailInput.place(x=x1, y=y1)
    y1 += 30
    univerInput = Entry(root, width=20)
    univerInput.place(x=x1, y=y1)
    y1 += 30
    cityInput = Entry(root, width=20)
    cityInput.place(x=x1, y=y1)
    y1 += 30

    def save():
        """
        Название: Сохранение данных после внесений информации в поля ввода по нажатию кнопки "Сохранить"
        Входные данные:
        Возвращаемые данные: -
        Автор: Кудрявцев Д.А., Приходько Д.С.
        """
        try:
            value = dict()
            value["Имя"] = nameInput.get()
            value["Пол"] = genderInput.get()
            value["Возраст"] = int(ageInput.get())
            value["Почта"] = mailInput.get()
            value["Место учёбы"] = univerInput.get()
            value["Город"] = cityInput.get()
            listBox.insert(END, value["Имя"].split()[0])

            db.addPerson(db.base, value)

            root.destroy()
        except ValueError:
            pass

    saveButton = Button(root, text="Сохранить", command=save)
    saveButton.place(x=10, y=210)

    cancelButton = Button(root, text="Отмена", command=root.destroy)
    cancelButton.place(x=85, y=210)

    root.mainloop()


def change():
    """
    Название: Изменение полей данных пользователя по нажатию кнопки "Изменить" под его информацией
    Входные данные: -
    Возвращаемые данные: -
    Автор: Кудрявцев Д.А., Приходько Д.С.
    """
    selection = listBox.curselection()
    if selection:
        value = listBox.get(selection)
        root = Tk()
        root.geometry("400x300")
        root.title("Изменить данные пользователя")
        root.configure(bg='lightgrey')

        field = ["Фамилия Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
        x1 = 20
        y1 = 20
        for i in field:
            lbl = Label(root, text=i, font=("Helvetica", 12))
            lbl.configure(bg='lightgrey')
            lbl.place(x=x1, y=y1)
            y1 += 30

        x1 = 140
        y1 = 20

        def set_text(text, e):
            """
            Название: Изначальная запись в поля ввода информации о пользователе
            Входные данные: Начальный текст поля для ввода, поле для ввода
            Возвращаемые данные: -
            Автор: Кудрявцев Д.А.
            """
            e.delete(0, END)
            e.insert(0, text)

        nameInput = Entry(root, width=20)
        nameInput.place(x=x1, y=y1)
        y1 += 30
        genderInput = Entry(root, width=20)
        genderInput.place(x=x1, y=y1)
        y1 += 30
        ageInput = Entry(root, width=20)
        ageInput.place(x=x1, y=y1)
        y1 += 30
        mailInput = Entry(root, width=20)
        mailInput.place(x=x1, y=y1)
        y1 += 30
        univerInput = Entry(root, width=20)
        univerInput.place(x=x1, y=y1)
        y1 += 30
        cityInput = Entry(root, width=20)
        cityInput.place(x=x1, y=y1)
        y1 += 30

        set_text(db.base[value]["Имя"], nameInput)
        set_text(db.base[value]["Пол"], genderInput)
        set_text(db.base[value]["Возраст"], ageInput)
        set_text(db.base[value]["Почта"], mailInput)
        set_text(db.base[value]["Место учёбы"], univerInput)
        set_text(db.base[value]["Город"], cityInput)

        def save():
            """
            Название: Сохранение данных после изменений по нажатию кнопки "Сохранить"
            Входные данные: -
            Возвращаемые данные: -
            Автор: Кудрявцев Д.А., Приходько Д.С.
            """
            try:
                info = dict()
                info["Имя"] = nameInput.get()
                info["Пол"] = genderInput.get()
                info["Возраст"] = int(ageInput.get())
                info["Почта"] = mailInput.get()
                info["Место учёбы"] = univerInput.get()
                info["Город"] = cityInput.get()

                db.changePerson(db.base, info)

                listSelection.delete(0, END)
                listSelection.insert(END, "Фамилия Имя: " + info["Имя"])
                listSelection.insert(END, "Пол: " + info["Пол"])
                listSelection.insert(END, "Возраст: " + str(info["Возраст"]))
                listSelection.insert(END, "Почта: " + info["Почта"])
                listSelection.insert(END, "Место учёбы: " + info["Место учёбы"])
                listSelection.insert(END, "Город: " + info["Город"])
                root.destroy()
            except ValueError:
                pass

        saveButton = Button(root, text="Сохранить", command=save)
        saveButton.place(x=10, y=270)

        cancelButton = Button(root, text="Отмена", command=root.destroy)
        cancelButton.place(x=85, y=270)

        root.mainloop()
    else:
        listSelection.delete(0, END)
        listSelection.insert(END, "Выберите пользователя")


def search():
    """
    Название: Поиск и вывод информации по нажатию кнопки "Поиск"
    Входные данные: -
    Возвращаемые данные: -
    Автор: Кудрявцев Д.А., Келлер В.А., Приходько Д.С.
    """
    root = Tk()
    root.geometry("630x500")
    root.title("Окно поиска")
    root.configure(bg='lightgrey')

    lbl = Label(root, text="Введите критерий поиска:")
    lbl.place(x=0, y=0)
    lbl.configure(bg='lightgrey')
    lbl1 = Label(root, text="Поле данных")
    lbl1.place(x=230, y=10)
    lbl1.configure(bg='lightgrey')

    def mode_min():
        global mode
        ds = Label(root, text="Текущий мод - min                ")
        ds.configure(bg='lightgrey')
        ds.place(x=380, y=120)
        mode = 0

    def mode_max():
        global mode
        ds = Label(root, text="Текущий мод - max                ")
        ds.configure(bg='lightgrey')
        ds.place(x=380, y=120)
        mode = 1

    def mode_combo():
        global mode
        ds = Label(root, text="Текущий мод - combobox")
        ds.configure(bg='lightgrey')
        ds.place(x=380, y=120)
        mode= 2

    def mode_normal():
        global mode
        ds = Label(root, text="Текущий мод - normal         ")
        ds.configure(bg='lightgrey')
        ds.place(x=380, y=120)
        mode = -1
    
    def process():
        """
        Название: Поиск и вывод информации по нажатию кнопки "Поиск"
        Входные данные: -
        Возвращаемые данные: -
        Автор: Кудрявцев Д.А., Келлер В.А.
        """
        def on_select2(event):
            """
            Название: Действие программы, когда пользователь выделяет поле в списке найденных пользователей
            Входные данные: Действие
            Возвращаемые данные: -
            Автор: Кудрявцев Д.А., Приходько Д.С.
            """
            w = event.widget
            try:
                index = int(w.curselection()[0])
                value = w.get(index)
                listInfo.delete(0, END)
                listInfo.insert(END, "Фамилия Имя: " + db.base[value]["Имя"])
                listInfo.insert(END, "Пол: " + db.base[value]["Пол"])
                listInfo.insert(END, "Возраст: " + str(db.base[value]["Возраст"]))
                listInfo.insert(END, "Почта: " + db.base[value]["Почта"])
                listInfo.insert(END, "Место учёбы: " + db.base[value]["Место учёбы"])
                listInfo.insert(END, "Город: " + db.base[value]["Город"])
            except IndexError:
                pass

        new_base = db.siftedBase(fieldInput, mode)
        db.statsCount(db.base, new_base)
        lblres = Label(root, text="Результаты были занесены в текстовый файл result.txt", fg='black',
                       font=("Helvetica", 12, "bold"))
        lblres.place(x=0, y=250)
        lblres.configure(bg='lightgrey')
        lblw = Label(root, text="Результат поиска:", fg='black', font=("Helvetica", 12, "bold"))
        lblw.place(x=0, y=270)
        lblw.configure(bg='lightgrey')
        lblq = Label(root, text="Информация о пользователе:", fg='black', font=("Helvetica", 12, "bold"))
        lblq.place(x=200, y=270)
        lblq.configure(bg='lightgrey')
        scrollbar = Scrollbar(root, orient="vertical")
        listResult = Listbox(root, width=15, height=10, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
        scrollbar.config(command=listResult.yview)
        scrollbar.pack(side="right", fill="y")
        for names in new_base:
            listResult.insert(END, names)
        listResult.bind("<<ListboxSelect>>", on_select2)
        listResult.place(x=0, y=300)

        listInfo = Listbox(root, width=40, height=6, font=("Helvetica", 12))
        listInfo.place(x=200, y=300)

    field = ["Фамилия Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
    fieldInput = []
    y1 = 30
    labels = []
    btns = []
    for i in field:
        labels.append(Label(root, text=i))
        labels[-1].place(x=150, y=y1)
        labels[-1].configure(bg='lightgrey') 
        fieldInput.append(Entry(root, width=20))
        fieldInput[-1].place(x=250, y=y1)
        y1 += 30
    minBtn = Button(root, text="min", command=mode_min)
    minBtn.place(x=380, y=90)
    maxBtn = Button(root, text="max", command=mode_max)
    maxBtn.place(x=415, y=90)
    comboBtn = Button(root, text="combobox", command=mode_combo)
    comboBtn.place(x=450, y=90)
    normalBtn = Button(root, text="normal", command=mode_normal)
    normalBtn.place(x=520, y=90)
    global mode
    mode = -1

    btn = Button(root, text="Поиск", width=10, command=process)
    btn.place(x=225, y=210)


    root.mainloop()


def on_select(event):
    """
    Название: Действие программы, когда пользователь выделяет поле в списке пользователей
    Входные данные: Действие
    Возвращаемые данные: -
    Автор: Кудрявцев Д.А., Приходько Д.С.
    """
    w = event.widget
    try:
        index = int(w.curselection()[0])
        value = w.get(index)
        listSelection.delete(0, END)
        listSelection.insert(END, "Фамилия Имя: " + db.base[value]["Имя"])
        listSelection.insert(END, "Пол: " + db.base[value]["Пол"])
        listSelection.insert(END, "Возраст: " + str(db.base[value]["Возраст"]))
        listSelection.insert(END, "Почта: " + db.base[value]["Почта"])
        listSelection.insert(END, "Место учёбы: " + db.base[value]["Место учёбы"])
        listSelection.insert(END, "Город: " + db.base[value]["Город"])
    except IndexError:
        pass
    changeButton = Button(root, text="Изменить", command=change)
    changeButton.place(x=200, y=160)

    deleteButton = Button(text="Удалить", command=delete)
    deleteButton.place(x=270, y=160)


if __name__ == "__main__":
    root = Tk()
    root.geometry("680x460")
    root.title("База данных")
    root.configure(bg='lightgrey')

    lbl1 = Label(root, text="Спискок людей:", fg='black', font=("Helvetica", 16, "bold"))
    lbl2 = Label(root, text="Информация:", fg='black', font=("Helvetica", 16, "bold"))
    lbl1.configure(bg='lightgrey')
    lbl2.configure(bg='lightgrey')
    lbl1.place(x=5, y=5)
    lbl2.place(x=200, y=5)

    scrollbar = Scrollbar(root, orient="vertical")
    listBox = Listbox(root, width=20, height=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
    scrollbar.config(command=listBox.yview)
    scrollbar.pack(side="right", fill="y")
    for names in db.base:
        listBox.insert(END, names)
    listBox.bind("<<ListboxSelect>>", on_select)
    listBox.place(x=0, y=21)

    listSelection = Listbox(root, width=50, height=6, font=("Helvetica", 12))

    listBox.place(x=5, y=40)
    listSelection.place(x=200, y=40)

    addButton = Button(root, text="Добавить", command=add)
    addButton.place(x=20, y=430)
    
    mode = 0
    searchButton = Button(root, text="Поиск", width=8, command=search)
    searchButton.place(x=90, y=430)

    exitButton = Button(root, text="Выход", command=quit)
    exitButton.pack(side="bottom", anchor="se")
    root.mainloop()
