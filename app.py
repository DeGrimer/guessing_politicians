import json
import copy

lastquest = ""
lastans = ""
with open('db.json', 'r', encoding='utf-8') as f:
    js = json.load(f)
    database = list(js['политики'])
    questions = js['вопросы']
def append():
    notfound = False
    politic = input("Введите имя политика: ")
    print("Пожалуйста, ответьте на вопросы о политике")
    last = chance()
    if last == 0:
        notfound = True
        list = js["политики"]
        for p in list:
            if lastquest in p.keys():
                last = [p]
    else:
        print("Сформулируйте вопрос, ответ на который поможет отличить политика "+politic+" от политика "+last[0]["имя"] )
        question = input()
        answer = input("Подскажите вариант правильного ответа: да или нет: ")
        if(answer == "да"):
            questAns = True
        else:
            questAns = False
    with open('db.json', "r", encoding='utf-8') as f:
        PeopleList = json.load(f)
        before = copy.copy(last)
        man =  copy.copy(last[0])
        if notfound:
            man['имя'] = politic
            if lastans == 'f':
                man[lastquest] = False
            else:
                man[lastquest] = True
        else:
            man['имя'] = politic
            man[question] = questAns
            questAns = not questAns
            before[0][question] = questAns
            for p in PeopleList["политики"]:
                if p["имя"] == before[0]["имя"]:
                    PeopleList["политики"].remove(p)
                    PeopleList["вопросы"].append(question)
                    PeopleList["политики"].append(before[0])
        PeopleList["политики"].append(man)
    with open('db.json', 'w', encoding='utf-8') as f:
        json.dump(PeopleList, f, ensure_ascii=False)
def chance():
    for q in questions:
        ans = input("Ваш политик "+q+"(t,f) ")
        man = take_chance(ans,q)
        if man != 0:
            print('=====================')
            for key in man[0]:
                if key != 'имя':
                    print(f"Ваш политк {key} - {man[0][key]}")
            print("Ваш политик "+man[0]["имя"])
            break
        else:
            global lastquest
            global lastans
            lastquest = q
            lastans = ans
    return man
def view():
    for q in questions:
        print(q, end=' --> True ')
        for d in database:
            if d[q] == True:
                end = d
        print(end["имя"])
        database.remove(end)
        print('\n | False \n\\ /\n')
    if(len(database) != 0):
        print(database[0]['имя'])
def take_chance(answer, property):
    if answer == "t":
        ans = True
    else:
        ans = False
    to_remove=[]
    for d in database:
        if d[property] != ans:
            to_remove.append(d)

    for i in to_remove:
        database.remove(i)

    if len(database) == 1:
        return database
    else:
        return 0


mod = input("Выберите режим: chance - угадать, view - просмотреть базу знаний, добавить нового политика - append: ")
if mod == "chance":
    man = chance()
    if man == 0:
        print("Не удалось угадать политика, помогите добавить его в систему")    
        append()
elif mod == "view":
    view()
elif mod == "append":
    append()

input()