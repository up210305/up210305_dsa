boleto = 0
dinero = int(input("Ingresa tu dinero: "))

while dinero > boleto:
    boleto+=1
    dinero-=boleto
print("Con tu dinero te alcanza para ", boleto, "boletos")

