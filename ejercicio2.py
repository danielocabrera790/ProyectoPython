from datetime import date 
import time
#Variables
fecha=date.today()
hora=time.strftime("%X")
#Cadenas
codigo = int(input("Introduce el codigo del paciente:"))
cad = input("Introduce la cadena a examinar:")
#Genera un informe que te indica la fecha, la hora, 
# el codigo del paciente y el resultado COVID
print("Se esta analizando el codigo...")
print("=====================================")
print("INFORME COVID")
print("=====================================")
print("Fecha:",fecha)
print("Hora:",hora)
print("Codigo:",codigo)
if cad == "ccucggcgggca":
    print("COVID: Positivo")
    resultado="Positivo"
else:
    print("COVID: Negativo")
    resultado="Negativo"
#Creo el archivo "covid.txt" si no esta creado, y si lo está el programa introduce la fecha, la hora y los resultados del test.
#El archivo se guarda y cada vez que ejecutemos un nuevo informe, relizara un salto de linea
archivo=(fecha,hora,resultado)
lista=list(archivo)
file=open("covid.txt", "a")
file.write('%s' % lista +'\n')
