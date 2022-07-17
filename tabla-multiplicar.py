# 2*1=2
# 2*2=4
# 2*3=6
#  .....
def multiplicar(numero):
    
    archivo = open(f"./tabla-{numero}.txt", "w")
    
    for i in range(11):

        # Cadena a guardar 
        cadena = f"{numero}*{i}={numero * i}\n"

        archivo.write(cadena)
    
    archivo.close()

multiplicar(5)
