def recorre(lista):
    for y in range(0, cantidad):
        valor=lista[y]
        rep=replicar
        replica(lista2, rep, valor)

def replica(lista2, rep, valor):
    for w in range(0, rep):
        lista2.append(valor)

lista=[]
lista2=[]

cantidad=int(input("Ingrese la cantidad de numeros del arreglo: "))
replicar=int(input("Ingrese la cantidad de replicas: "))

for x in range(0, cantidad):
    num=int(input("Ingrese un número: "))
    lista.append(num)

recorre(lista)

print("La lista ingresa es:", lista)
print("Cada valor de la lista se replicara:", replicar, "veces")
print ("La lista con los valores replicados es:", lista2)