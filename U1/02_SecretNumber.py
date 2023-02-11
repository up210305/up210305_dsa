import random as random

secret = random.randint(1, 20)

number = int(input("Adivina el numero secreto: "))

while number != secret:
    print("Lo siento, intentalo devuelta")
    number = int(input("Ingresa un numero diferente: "))
else:
    print("Correcto, haz acertado el numero secreto!!!")

