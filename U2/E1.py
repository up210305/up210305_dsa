def moverLista(lista, n):
    for i in range(0, n):
        ultimo = lista.pop()
        lista.insert(0, ultimo)
    return lista

lista = [5, 2, 1, 6, 3, 4, 7, 9]

n = int(input("Numero de corrimientos a la derecha: "))

print("Lista sin modificar: " , lista)
moverLista(lista, n)
print("Lista modificada: " , lista) 
