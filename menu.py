from Open import OpenText
from Open import OpenText2
from read import Read
from read import Read2


def menu():
    num= int(input("Выберите пункт:\n1. Вывод контаков\n2. Добавить контакт\n5. Завершить программу\n "))
    if num==1:
        num=(int(input("в каком формате вывести контакты?\n1. Записи в строку\n2. записи с новой строки")))
        if num==1:
            OpenText()
            menu()
        elif num==2:
            OpenText2()
            menu()
    elif num==2:
        num=(int(input("в каком формате внести контакты?\n1. Записи в строку\n2. записи с новой строки")))
        if num==1:
            Read()
            menu()
        elif num==2:
            Read2()
            menu()

menu()
