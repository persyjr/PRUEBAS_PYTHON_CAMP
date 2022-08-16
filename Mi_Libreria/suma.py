#primero hago una funcion para limpiar la consola
def limpiar_pantalla():
    print("\33[2J\33[H") #esta secuenncia de comandos limpia la pantalla y luego me ubica el cursor arriba a la izquierda

def funcion_suma (num2,num1=5): #asigno valores por defecto, estos valores se usaran en caso de yo no definir algun parametro durante el llamado de la funcion
    return num1+num2


#lo que hago aca es condicionar la ejecucion de este codigo solo si este archivo es llamado desde la consola siendo principal
if __name__=="__main__":
    limpiar_pantalla()
    resultado =suma(10,15)
    print("EL RESULTADO DE LA SUMA ES")
    print(resultado)
    print("el origen de este codigo se escribio en el archivo suma.py")