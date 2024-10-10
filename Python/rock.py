import random 
from colorama import Fore, Style

win = {
    ("rock", "scissor"),  
    ("scissor", "paper"),  
    ("paper", "rock")
    }

def comp(x, choice):
    if x == choice:
        print(Fore.YELLOW + "IT'S A TIE ME LADDIE!" + Style.RESET_ALL)
        main()
    elif (x, choice) in win:
        print(Fore.BLUE+ "YA HAVE WON ME LADDIE!" + Style.RESET_ALL)
        again = str(input("wanna play again?(y/n)"))
        if again == "y":
            print("okay")
            main()
        else:
            print("WELL WE WILL")
            main()
    else:
        print(Fore.RED + "YA HAVE LOST ME LADDIE!" + Style.RESET_ALL)
        main()

def main():
    x = str(input("pick (rock/paper/scissor): "))
    choice = random.choice(["rock", "paper", "scissor"])
    if x in ["rock", "paper", "scissor"]:
        print("i pick", choice)
        comp(x, choice)
    else:
        print("try again: ")
        main()

main()
