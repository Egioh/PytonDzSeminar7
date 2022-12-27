def OpenText():
    with open ("spisok.txt","r") as S:
        list = [i for i in S.read().split("_")]
        print(*list)
    input("enter для возврата в меню")

def OpenText2():
    with open ("spisok2.txt","r") as S2:

        lines = S2.readlines()
        for line in lines:
            print(line.strip())
    input("enter для возврата в меню")