
import os
import time
import random
import pyfiglet


def run():
    ficookie = pyfiglet.figlet_format("FORTUNE-COOKIE")
    print(ficookie)
    menu = """ 特殊絵文字さんツふぁぼ字  HELLO, WELCOME TO CHINA  特殊絵文字さん レッツふぁぼ字さんレ

                     .="=.
                /\_ /|- -|\ _/\             ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
                \_//O\_+_/O\\_/              ㉼ I INFORM YOU THAT YOU HAVE 3 OPTIONS:
                 \\\/`°°°`\///                 1) OPEN A FORTUNE COOKIE
                  \   ($)   /                 2) ADD YOUR FAVORITE SENTENCE TO A COOKIE
                 ./---/_\---\.                3) GET OUT OF HERE, WITHOUT KNOWING YOUR FORTUNE
                 / °-------° \              ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
                / /    |   \  \                 ｱ ｲ ｳ ｴ ｵ ｶ ｷ ｸ ｹ ｺ ｻ ｼ ｽ ｾ ｿ ﾀ ﾁ ﾂ ﾃ ﾄ ﾅ ﾆ 
               /   /    |  \   \                ﾉ ﾊ ﾋ ﾌ ﾍ ﾎ ﾏ ﾐ ﾑ ﾒ ﾓ ﾔ ﾕ ﾖ ﾗ ﾘ ﾙ ﾚ ﾛ ﾜ ｦ ﾝ
               `._._.-'-._.-'-.'            ㉼ WRITE THE OPTION NUMBER HERE ⟹ """
    option = int(input(menu))
    if option == 1:
        with open("./phrases.txt","r",encoding="utf-8") as pr:
            phraserandom = random.choice(pr.readlines())
            print("\n")
            name = str(input("NAME: ")).capitalize()
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1 ...")
            print(str(name) +" "+ str(phraserandom))
    if option == 2:
        with open ("./phrases.txt","a",encoding="utf-8") as ap:
            newphrase = str(input("WRITE HERE NEW FORTUNE PHRASE: ")).lower().strip()
            ap.write("\n")
            ap.write(newphrase)
    if option == 3:
        fiexit = pyfiglet.figlet_format("EXIT")
        print(fiexit)
        time.sleep(3)
        os.system("cls")
        exit() 


if __name__=="__main__":
    run()
