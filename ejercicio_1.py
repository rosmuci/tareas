#PROMEDIO
#ENTRADAS



NUM_1=float(input("escribe el 1er número: "))
NUM_2=float(input("escribe el 2do número: "))
NUM_3=float(input("escribe el 3er número: "))
#PROCESOS
PROMEDIO=((NUM_1+NUM_2+NUM_3)/3);
if(PROMEDIO<6):
    print("REPROBADO")
elif(PROMEDIO>6):
    print("APROBADO")    

#SALIDA DE DATOS
print("el promedio es igual a",round(PROMEDIO,2))
