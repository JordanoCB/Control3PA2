def posneg(lista):
    for x in range(0, cantidad):
        if lista[x] >= 0:
            pos.append(lista[x])
        else:
            neg.append(lista[x])

lista=[]
cantidad=int(input("Ingrese la cantidad de numeros del arreglo: "))
pos=[]
neg=[]

for x in range(0, cantidad):
    num=int(input("Ingrese un número: "))
    lista.append(num)

posneg(lista)

print("Los valores positivos son: ", pos)
print("Los valores negativos son: ", neg)