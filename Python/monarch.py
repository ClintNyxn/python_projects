import random
n = int(input("no. of kids = ")) 
dict = {}
while n>=1:
    i = random.randint(1,10)
    name = input("enter name:")

    while i in dict.values():
        i = random.randint(1,11)
    
    dict[name] = i 
    n = n-1
    
boys = []
girls = []
liist = []

for i in dict:
    if dict[i] % 2 == 0: 
        boys.append((dict[i]))
    else:
        girls.append((dict[i]))

boys.sort(reverse=True)
girls.sort(reverse=True)

liist = boys + girls
print(liist)

