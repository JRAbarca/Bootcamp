# Básico: imprime todos los números enteros del 0 al 100.
for x in range(101):
    print(x)

# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for x in range(2,501,2):
    print(x)

# Contando Vanilla Ice
for x in range(1,101):
    if (x % 10  == 0):
        print('baby')
    elif  (x % 5 == 0):
        print('ice ice')
    else:
        print(x)

# Wow. Número gigante a la vista
suma=0
for x in range(0,500001,2):
    suma = suma + x
print(suma)

# Regrésame al 3
for x in range(2024,0,-3):
    print(x)

# Contador dinámico
def dinamico(numInicial, numFinal, multiplo):
    for x in range(numInicial,numFinal+1):
        if x % multiplo == 0:
            print(x)

dinamico(3,10,2)