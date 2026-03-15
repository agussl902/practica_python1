#Escribe un programa que solicite al usuario una cantidad de segundos y muestre cuántas horas, minutos y segundos equivalen.
# Por ejemplo, 3661 segundos son 1 hora, 1 minuto y 1 segundo.

seg = int(input("escribe la cantidad de segundos: "))
min = seg//60
hora = min//60

seg_res = seg%60
min_res = min%60
print ("la cantidad de segundos: ",seg ," dando la cantidad de minutos que son: ", min_res , "y la cantidad de horas son: ", hora, "y la cantidad de seg restantes son: ",seg_res)