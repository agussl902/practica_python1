# Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
#oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
#espacios. Las palabras cortas deben ser excluidas del resultado final.

lista = []
oracion = ""
while True:
    palabra = input("escribe una palabra o pone 0 para salir: ")
    if (palabra == "0"):
        break
    lista.append(palabra)
for palabra in lista:
    if len(palabra)>3:
        oracion+= palabra + " "
print (oracion)

