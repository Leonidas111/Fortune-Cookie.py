
import os
import time
import random

def run():
    menu = """ 特殊絵文字さんツふぁぼ字  HELLO, WELCOME TO CHINA  特殊絵文字さん レッツふぁぼ字さんレ
                     .="=.
                /\_ /|- -|\ _/\             ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
                \_//O\_+_/O\\_/             * I INFORM YOU THAT YOU HAVE 3 OPTIONS:
                 \\\/`°°°`\///                1) OPEN A FORTUNE COOKIE
                  \   ($)   /                 2) ADD YOUR FAVORITE SENTENCE TO A COOKIE
                 ./---/_\---\.                3) GET OUT OF HERE, WITHOUT KNOWING YOUR FORTUNE
                 / °-------° \              ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼
                / /    |   \  \
               /   /    |  \   \
               `._._.-'-._.-'-.'            ㉼ WRITE THE OPTION NUMBER HERE ⟹           """
    option = int(input(menu))
    if option == 1:
        with open("./phrases.txt","r",encoding="utf-8") as pr:
            phraserandom = random.choice(pr.readlines())
            print("\n")
            name = str(input("NAME: "))
            print("THREE")
            time.sleep(1)
            print("TWO")
            time.sleep(1)
            print("ONE...")
            print(str(name) +" "+ str(phraserandom))
    if option == 2:
        with open ("./phrases.txt","a",encoding="utf-8") as ap:
            newphrase = str(input("WRITE HERE NEW FORTUNE PHRASE: "))

        
    if option == 3:
        os.system("cls")
        exit() 

if __name__:"__main__":
    run()