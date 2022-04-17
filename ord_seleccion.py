def ord_seleccion(lista):
    n=len(lista)-1

    while n>0:
        lista2=sorted(lista)
        return lista2[n]

lista=[]
lista2=[]

for x in range(0, 3):
    num=int(input("Ingrese un número entero: "))
    lista.append(num)

maximo=ord_seleccion(lista)

print("El arreglo ingresado es: ", lista)
print("El valor maximo del arreglo es: ", maximo)