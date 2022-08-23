import time             #importa el paquete time format UTC
import datetime         #importando paquete datetima


#Mostrando algunas de las funcionalidades de el paquete time
print("MOSTRANDO ALGUNAS UTILIDADES DE LA HORA UNIX")
print(time.gmtime(0)) #imprime el tiempo unix
print(f"segundos transcurridos desde 1/January/1970 : {time.time()}") #imprime los segundos transcurridos hasta hoy
#que tipo de dato es este?
print(f"El tipo de dato para esta variable [time.gmtime(0)] es : {type(time.gmtime(0))}")
print(f"El tipo de dato parala clave tm_year es entero  : {type(time.gmtime(0).tm_year)}")
print(f"La hora  en el meridiano de Greenwitch: {time.gmtime(time.time())}")
print(f"La hora  local es : {time.localtime()}\n")

print("HORA STRING")
#metodos para convertir la hora en un string
print(f' la hora en formato STRING es : {time.strftime("%d/%m/%Y %H/:%M:%S",time.localtime())}\n') 

#declarando una variable que me mantega la hora de entrada
"""print("CONTANDO LOS SEGUNDOS EN RESPONDER")
inicio = time.time()
input("¿Amigo como te llamas? ")
fin = time.time()
#presento los segundos que se demoro en responder mediante la formula 
print(f"Has demorado : {int(fin-inicio)} segundos en responder\n")
"""

#Temporizador de inactividad
"""
print("TEMPORIZAR INACTIVIDAD")
print(" Preaparate para tres segundos de inactiviad")
time.sleep(3)
print(" Actividad Reanudada")
print(" ciclo for con time.sleep(0,25)")
for i in range(0,10):
    time.sleep(0.25)
    print(f"Ciclo for cada 0,25 sg {i}" )"""


print("DATETIME: Obtener la hora local mediante datetime")
print("Con este modulo puedes obtener mas precision")
print("Estableciendo la fecha de hoy")
fin=datetime.datetime.now()
print(fin)
print("predefiniendo una fecha 31/12/2022 como objeto datetime")
inicio=datetime.datetime(2022, 12,31)
print(inicio)
print("resultado de las restas de las fechas: DIAS, HORAS:MINUTOS:SEGUNDOS.MICROSEGUNDOS")
print(inicio-fin)
print((inicio-fin).total_seconds())
