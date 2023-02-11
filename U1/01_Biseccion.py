
import numpy as np

def fnEcuacion(valor):
    return pow(valor, 2) - 2

x1 = 1
x2 = 2
xm = 0
Es = 0.001        
Er = abs(x2-x1)
i = 1
it = round((np.log(x2 - x1) - np.log(Es)) / np.log(2))

print("Iterations: ", it)
print("i\t|x1\t|x2\t|er\t|xm\t|f(x1)\t|f(xm)\t|f(x1)*f(xm)")

while (Er >= Es):

    xm = (x1 + x2) / 2
    print(i,round(x1, 3), round(x2, 3), round(Er, 3), round(xm, 3), round(fnEcuacion(x1), 3), round(fnEcuacion(xm), 3), round((fnEcuacion(x1) * fnEcuacion(xm)),3), sep="\t|")
    
    if (fnEcuacion(x1) * fnEcuacion(xm) < 0):
        x2 = xm
    else :
        x1 = xm
    
    Er = abs(x2 - x1)
    i += 1        

print("\nRoot: ", xm, "\n")