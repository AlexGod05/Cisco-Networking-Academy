print("Ingresa un numero positivo")
c0 = int(input())
if c0 < 0:
    print("Has ingresado un numero negativo")
elif c0 <= 1:
    print("el numero debe ser mayor a 1")

pasos = 0

while c0 > 1:
    if c0 % 2 == 0:
        print("Numero par: ", c0)
        c0 //= 2
        print("Numero divido: ", c0)
    else:
        print("Numero impar: ", c0)
        c0 *= 3
        c0 += 1
        print("Numero multiplicado y sumado 1: ", c0)
    pasos += 1

print(pasos)
