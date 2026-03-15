#Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
#una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al finalizar

num = int (input("escribe un numero: "))
l1 = []
l2= []
for i in range(1,num+1):
    if (i%5 == 0):
        l1.append(i) 
        continue
    l2.append(i)
print("voy a imprimir la lista multiplo de 5", l1)
print("voy a imprimir la lista sin los multiplos de 5", l2)