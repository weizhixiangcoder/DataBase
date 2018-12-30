import shelve as shl
import os
p = os.getcwd()


def baseCreation():
    """
   Название: Создание бинарного файла, в котором содержится база данных
   Входные данные: -
   Возвращаемые данные: -
   Авторы: Кудрявцев Д.А., Приходько Д.С., Келлер В.А.
   """
    global p
    fields = ["Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
    d = dict()
    input_file = open(p + "\\Data\\input.txt", "r")
    for name in input_file:
        name = name.split("  ")
        name[2] = int(name[2])
        q = zip(fields, name)
        d[name[0].split()[0]] = dict(q)
    input_file.close()
    f = shl.open(p + "\\Data\\base.shl", "n")
    for x in d:
        f[x] = d[x]
    f.close()


def baseDecode():
    """
   Название: Загрузка файла базы данных в оперативную память
   Входные данные: -
   Возвращаемые данные: База данных в виде словаря словарей
   Автор: Приходько Д.С.
   """
    global p
    f = shl.open(p + "\\Data\\base.shl")
    b = dict()
    for x in f:
        b[x] = f[x]
    return b


def baseEncode(b):
    """
   Название: Зашифровка базы данных в бинарный файл
   Входные данные: База данных в виде словаря словарей
   Возвращаемые данные: -
   Автор: Приходько Д.С.
   """
    global p
    f = shl.open(p + "\\Data\\base.shl", "n")
    for x in b:
        f[x] = b[x]
    f.close()


def addPerson(b, value):
    """
   Название: Добавление пользователя в базу данных
   Входные данные: База данных в виде списка списков
   Возвращаемые данные: Изменённая база данных
   Авторы: Келлер В.А., Приходько Д.С.
   """
    fields = ["Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
    b[value["Имя"].split()[0]] = dict()
    b[value["Имя"].split()[0]]["Имя"] = value["Имя"]
    for x in fields[1:]:
        if x == 2:
            b[value["Имя"].split()[0]][x] = int(value[x])
        else:
            b[value["Имя"].split()[0]][x] = value[x]
    baseEncode(b)
    newBaseFile(b)


def newBaseFile(b):
    """
   Название: Запись в текстовые файлы (исходный и результат) изменённой базы данных
   Входные данные: База данных
   Возвращаемые данные: -
   Авторы: Приходько Д.С., Кудрявцев Д.А.
   """
    global p
    f = open(p + "\\Output\\base.txt", "w")
    s = ""
    for x in b:
        for y in b[x]:
            s += str(b[x][y]) + "  "
        s += '\n'
    f.write(s)
    f.close()
    f = open(p + "\\Data\\input.txt", "w")
    s = ""
    for x in b:
        for y in b[x]:
            s += str(b[x][y]) + "  "
        s += '\n'
    f.write(s)
    f.close()


def changePerson(b, value):
    """
   Название: Изменение полей пользователя
   Входные данные: База данных как список списков, Фамилия и имя пользователя как его ключ в базе
   Возвращаемые данные: -
   Автор: Кудрявцев Д.А.
   """
    fields = ["Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]
    for x in fields[1:]:
        if x == 2:
            b[value["Имя"].split()[0]][x] = int(value[x])
        else:
            b[value["Имя"].split()[0]][x] = value[x]
    baseEncode(b)
    newBaseFile(b)


def deletePerson(b, key):
    """
   Название: Удаление выбранного пользователя из базы данных
   Входные данные: База данных в виде словаря словарей
   Возвращаемые данные: Изменённый словарь
   Автор: Приходько Д.С.
   """
    del b[key]
    baseEncode(b)
    newBaseFile(b)


def isPersonOK(per, crit, mode):
    """
    Название: Проверка удовлетворения пользователем критерия
    Входные данные: База данных в виде словаря словарей
    Возвращаемые данные: Истина или ложь в зависимости от удовлетворения условий
    Автор: Келлер В.А.
    """
    fields = ["Имя", "Пол", "Возраст", "Почта", "Место учёбы", "Город"]

    for i in range(6):
        if i == 2:
            if len(crit[i]) != 0 and mode == 0 and (per[fields[i]] < int(crit[i][0]) or len(crit[i]) > 1):
                return False
            elif len(crit[i]) != 0 and mode == 1 and (per[fields[i]] > int(crit[i][0]) or len(crit[i]) > 1):
                return False
            elif len(crit[i]) != 0 and mode == 2 and (per[fields[i]] < int(crit[i][0]) or per[fields[i]] > int(crit[i][1]) or len(crit[i]) > 2):
                return False
            elif len(crit[i]) !=0 and mode == -1 and (per[fields[i]] != int(crit[i][0]) or len(crit[i]) > 1):
                return False
        else:
            if len(crit[i]) != 0 and ' '.join(crit[i]) != per[fields[i]]:
                return False
    return True


def siftedBase(fieldInput, mode):
    """
    Название: Поиск в базе данных по критериям введнным в поля ввода
    Входные данные: Список полей ввода данных из графического интерфейса
    Возвращаемые данные: словарь словарей
    Автор: Келлер В.А.
    """
    try:
        new_b = dict()
        crit = []
        for i in range(len(fieldInput)):
            crit.append(fieldInput[i].get().split())
        for per in base.values():
            if isPersonOK(per, crit, mode):
                new_b[per["Имя"].split()[0]] = per
        return new_b
    except:
        return dict()


def statsCount(b, new_b):
    """
    Название: Подсчёт итогов работы программы и занесение их в текстовый файл
    Входные данные: Исходная и полученная при поиске базы данных
    Возвращаемые данные: -
    Автор: Приходько Д.С.
    """
    s = 0
    avgAge = 0
    newsum = 0
    newfem = 0
    newmen = 0
    newAvgAge = 0
    newunis = dict()
    newcity = dict()
    for i in b:
        s += 1
        avgAge += int(b[i]["Возраст"])
    if s != 0:
        avgAge = round(avgAge / s)
    else:
        avgAge = 0
    for j in new_b:
        newsum += 1
        newAvgAge += int(new_b[j]["Возраст"])
        newunis[new_b[j]["Место учёбы"]] = newunis.get(new_b[j]["Место учёбы"], 0) + 1
        newcity[new_b[j]["Город"]] = newcity.get(new_b[j]["Город"], 0) + 1
        if new_b[j]["Пол"] == "жен":
            newfem += 1
        else:
            newmen += 1
    print(newunis)
    print(newcity)
    max1 = max2 = 0
    city = ""
    univer = ""
    for i in newunis:
        if newunis.get(i,0) > max1:
            max1 = newunis.get(i, 0)
            univer = i
    for i in newcity:
        if newcity.get(i,0) > max2:
            max2 = newcity.get(i, 0)
            city = i
    print(univer, city)
    if newsum != 0:
        newAvgAge = round(newAvgAge / newsum)
    else:
        newAvgAge = 0
    f = open(p + "\\Output\\result.txt", "w")
    st = ""
    st += "Общее количество записей в базе данных: " + str(s) + "\n"
    st += "Среднее значение возраста в базе данных: " + str(avgAge) + "\n"
    st += "Количество записей, найденных по заданным критериям: " + str(newsum) + "\n"
    st += "Среднее значение возраста найденных по заданным критериям: " + str(newAvgAge) + "\n"
    st += "Количество лиц мужского пола найденных по заданным критериям: " + str(newmen) + "\n"
    st += "Количество лиц женского пола найденных по заданным критериям: " + str(newfem) + "\n"
    st += "Большинство человек найденных по заданным критериям проживают в: " + city + "\n"
    st += "Большинство человек найденных по заданным критериям учаться в: " + univer + "\n"
    f.write(st)
    f.close()


baseCreation()
base = baseDecode()
