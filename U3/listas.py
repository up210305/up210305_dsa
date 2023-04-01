class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato=dato)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo

    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato=dato)
        if self.esta_vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

    def eliminar_por_valor(self, dato):
        actual = self.primero
        while actual is not None:
            if actual.dato == dato:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def imprimir_hacia_adelante(self):
        actual = self.primero
        while actual is not None:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()

    def imprimir_hacia_atras(self):
        actual = self.ultimo
        while actual is not None:
            print(actual.dato, end=' ')
            actual = actual.anterior
        print()

    def search(self, dato):
        actual = self.primero
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def peak(self):
        if self.primero is None:
            return None
        maximo = self.primero.dato
        actual = self.primero
        while actual is not None:
            if actual.dato > maximo:
                maximo = actual.dato
            actual = actual.siguiente
        return maximo
    
    def getSize(self):
        actual = self.primero
        contador = 0
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

mi_lista = ListaDobleEnlazada()

print(mi_lista.esta_vacia())

mi_lista.agregar_al_final(1)
mi_lista.agregar_al_final(2)
mi_lista.agregar_al_final(3)
mi_lista.agregar_al_inicio(4)
mi_lista.agregar_al_inicio(5)
mi_lista.agregar_al_inicio(6)

print(mi_lista.esta_vacia())

mi_lista.imprimir_hacia_adelante()  # Output: 6 5 4 1 2 3
mi_lista.imprimir_hacia_atras()     # Output: 3 2 1 4 5 6

print(mi_lista.search(3))  # Output: True
print(mi_lista.search(7))  # Output: False

print(mi_lista.peak())  # Output: 6

print(mi_lista.getSize())  # Output: 6
