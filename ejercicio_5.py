#Escribe un programa que simule una caja registradora: el usuario ingresa precios de
#productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
#acumulado. Nota: utilizá la sentencia break cuando haga falta.

suma = 0
while True: 
    precio = float(input("ingresa un precio o ingresa 0 para terminar el programa: "))
    if (precio == 0):
        break 
    suma += precio
print("el total acumalado es: ", suma)