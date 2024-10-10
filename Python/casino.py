import random
from colorama import Fore, Style

points = 100

def main():
    global points
    while points > 0:
        t = [1,2,3,4,5]
        n = random.choice(t)

        # Input with color formatting
        x = int(input(Fore.YELLOW + f"You have {points} points, guess a number 1-5 to win: " + Style.RESET_ALL))
        
        if x == n:
            print(Fore.BLUE + "Nice, it was", n, Style.RESET_ALL)
            points += 50
            print("Your score is", points)
        else:
            print("Bad, it was", n)
            points -= 10
            print(Fore.RED + "Your score is", points, Style.RESET_ALL)

    print("YA RAN OUT O' MONEY LAD!")

main()
