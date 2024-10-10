
import random
import os
import time
from colorama import Fore, Style

# Clear the screen for cleaner output
def clear_screen():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Art for visual appeal
rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Determine winner
win = {
    ("rock", "scissor"),
    ("scissor", "paper"),
    ("paper", "rock")
}

# Countdown animation
def countdown():
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(0.5)
    print("Shoot!")

# Visual representation of choices
def display_choice(choice):
    if choice == "rock":
        print(rock_art)
    elif choice == "paper":
        print(paper_art)
    elif choice == "scissor":
        print(scissor_art)

# Compare player and computer choices
def comp(player_choice, comp_choice):
    clear_screen()
    print(Fore.YELLOW + f"You picked {player_choice}!" + Style.RESET_ALL)
    display_choice(player_choice)

    print(Fore.YELLOW + f"I chose {comp_choice}!" + Style.RESET_ALL)
    display_choice(comp_choice)

    countdown()

    if player_choice == comp_choice:
        print(Fore.YELLOW + "IT'S A TIE ME LADDIE!" + Style.RESET_ALL)
    elif (player_choice, comp_choice) in win:
        print(Fore.BLUE + "YA HAVE WON ME LADDIE!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "YA HAVE LOST ME LADDIE!" + Style.RESET_ALL)

    play_again()

# Ask if the player wants to play again
def play_again():
    again = input(Fore.CYAN + "\nWanna play again? (y/n): " + Style.RESET_ALL).lower()
    if again == "y":
        clear_screen()
        main()
    else:
        print(Fore.GREEN + "TOO BAD WE STILL PLAYING LADDIE!" + Style.RESET_ALL)
        main()

def main():
    print(Fore.CYAN + "Welcome to Rock, Paper, Scissors!\n" + Style.RESET_ALL)
    player_choice = input("Pick (rock/paper/scissor): ").lower()
    if player_choice in ["rock", "paper", "scissor"]:
        comp_choice = random.choice(["rock", "paper", "scissor"])
        comp(player_choice, comp_choice)
    else:
        print(Fore.RED + "Invalid input, try again!" + Style.RESET_ALL)
        main()

clear_screen()
main()
