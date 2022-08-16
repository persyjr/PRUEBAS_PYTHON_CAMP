from Mi_Libreria import suma #si importo un archivo el cual ejecuta una funcion e imprime un resultado
#entonces cuando abra este aarchivo ejecutare lo que contenga dicho archivo

from Mi_Libreria.suma import  funcion_suma as sumando #de esta forma le cambio el nombre a mi funcion_suma ahora se llamara sumando
#* asi importo todas las funciones
#funcion_suma asi importo unicamente la funcion suma de mi archivo suma.py

print("RECORDANDO LOS MODULOS")
print("imprimiendo el valor de la variable principal de este documento o modulo (principal) llamada __name__")
print(f"__name__: {__name__}")
print("imprimiendo el valor de la variable del modulo importado suma suma.__name__")
print(f"suma.name : {suma.__name__}\n")

print("PROCEDIENDO A LLAMAR FUNCIONES CONTENIDAS EN EL ARCHIVO 'suma.py'")
resultado=sumando(10,59)
#De no importar la funcion suma pero su el archivo suma.py llamo a esta funcion solamente asi suma.funcion_suma(num2)
print(f"el resultado de la suma es : {resultado}\n")