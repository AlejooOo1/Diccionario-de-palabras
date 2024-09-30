import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Introduce la longitud de la contraseña: "))
password = ""

for i in range(password_length):
    password += random.choice(characters)

print("Tu contraseña generada es:", password)

