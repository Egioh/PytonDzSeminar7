def Read ():
    with open ("spisok.txt","a") as S:
        S.write("_"+ input("введите телефон:"))
        S.write("_"+ input("введите имя:"))
        S.write("_"+ input("введите описание:"))
        input("enter для возврата в меню")

def Read2():
    with open ("spisok2.txt","a") as S2:
        S2.write("\n"+input("\nвведите телефон:"))
        S2.write("\n"+input("\nвведите имя:"))
        S2.write("\n"+input("\nвведите описание:"))
        input("enter для возврата в меню")
