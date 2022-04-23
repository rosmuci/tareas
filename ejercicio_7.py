#entradas
nivel_agua=float(input("Nivel de agua:  "))

#proceso
if(nivel_agua> 6):
    print("Desbordamiento bomba")
elif(nivel_agua==6):
    print("Apagar bomba")    
elif(4<nivel_agua<6):
    print("Desacelarar bomba")
elif (2<nivel_agua<4):
    print("Bomba trabajando")
elif(0<nivel_agua<2):
    print("Acelerar bomba de agua")    
elif(nivel_agua ==0):
    print("Enceder bomba de agua")
elif(nivel_agua<0):
    print("Fuga en cisterna")      
    
    
        
