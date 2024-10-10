import random

x = random.choice([1,2,3,4,5,6,7,8,9,10])
lives = 3
print("WELCOME TO THE BEST GAME EVER!")
def main():
    global lives
    while lives > 0: 
        print(f"you have {lives} lives")
        y = int(input("guess a no. "))
        if y == x:
            print("ya have won")
            break
        elif y>x:
            print("think less")
        else:
            print("think more")
        lives -= 1
main()
print('ya dead')
