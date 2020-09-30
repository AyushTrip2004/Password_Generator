import random

userinp = int(input("Enter Your Password Length\n"))

characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*0123456789")

length = int(userinp)

password = ""

for x in range(length):
    password = password + random.choice(characters)
print(password)