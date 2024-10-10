import random
leng = input("I will make password, how long? ")
leng = int(leng)
print("here your password")

chars = "1234567890qwertyuioplkjhgfdsazxcvbnm!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM"
passwd = ""
for c in range(leng):
    passwd += random.choice(chars)

print(passwd)
