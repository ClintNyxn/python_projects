l = int(input("length: "))
a = 1

while l>0:
    print("."*l, "#"*a, "."*l)
    a +=2
    l -=1
while a>=0:
    print("."*l, "#"*a, "."*l)
    l +=1
    a -=2
