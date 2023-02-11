a = [10,1,6,3,9,4,8,5,7,2]
print("Sin ordenar: ", a)
for i in range(0, len(a)+1 -2):
    for j in range(0,len(a)+1 - i-2):
        x = a[j]
        y = a[j+1]
        if x > y:
            a[j] = y
            a[j+1] = x
print("Ordenada: ", a)