def estaBalanceado(expresion):
    pila = []
    for i in expresion:
        if i == "(":
            pila.append(i)
        elif i == ")":
            if not pila:
                return False
            pila.pop()
    return not pila

#expresion = ["(())()"]
#expresion= ["(()"]
#expresion = [")()("]
#expresion = ["( a * + ()) b ()"]
expresion = ["(())()", "(()", ")()(", "( a * + ()) b ()"]
n = len(expresion)
for i in range(0, n):
    resultado = estaBalanceado(expresion[i])
    print(resultado)


