palabra=input("Dame una palabra: ")
palabraDos = "".join(palabra.split())
lista=list(palabraDos)

for j in range(int(len(lista))):
    if j == len(lista)-1:
        break
    if (lista[j]==' '):
        del(lista[j])

print (lista)

if lista == lista[::-1] :
    print("Palindromo")
else:
    print("No es Palindromo")