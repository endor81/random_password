import random
element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = int(input("какая длинна пароля?"))

password_1 = ""
for i in range (password):
    password_1+=random.choice(element)
print(password_1)