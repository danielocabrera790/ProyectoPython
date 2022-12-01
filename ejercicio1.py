from datetime import date
import time
#Variables y listas
fecha= date.today()
hora= time.strftime("%X")
temperaturas = []
count=0
# Hago que el script te pregunte temperaturas hasta que introduzcas un "100" 
while True:	
	temperatura = int and float(input("¿Que temperatura hace hoy? (Cº): ")) 
	if temperatura < 100:
		temperaturas.append(temperatura)
		count=count+1
	if temperatura >= 100: break;	
#Titulo del informe
print("==============================================================")
print("Informes de temperaturas del Parque Natural de Doñana:")
print("==============================================================")
#Fecha y hora
print("Fecha:",fecha)
print("Hora:", hora)
# Te indica la temperatura maxima, minima y la media de todas las introducidas.
# Ademas te indica el numero de valores introducidos y todas las temperaturas que has indicado
print("Numero de valores introducidos:",count)
print("Temperaturas tomadas:",temperaturas,"Cº")
print("Temperatura media:",sum(temperaturas)/len(temperaturas),"Cº")
print("Temperatura max:",max(temperaturas),"Cº")
print("Temperatura min:",min(temperaturas),"Cº")
#Creo el archivo "temp.txt" si no esta creado, y si lo está el programa introduce la fecha, la hora y las temperaturas del informe.
#El archivo se guarda y cada vez que ejecutemos un nuevo informe, relizara un salto de linea
archivo=(fecha,hora,temperaturas)
lista=list(archivo)
file=open("temp.txt", "a")
file.write('temperaturas = %s' % lista +'\n')
