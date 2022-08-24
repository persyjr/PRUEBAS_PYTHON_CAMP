import sys

#devuelve la suma de dos numeros
def funcion_suma (num2,num1): #asigno valores por defecto, estos valores se usaran en caso de yo no definir algun parametro durante el llamado de la funcion
    return num1+num2

#MAIN
if __name__=='__main__':
    #si no hay 3 paràmetros (0: archivo del programa, 1: num1 y 2: num2)
    if len(sys.argv)!= 3:
        print("ERROR PARÀMETROS INCORRECTOS")
        print("modo de uso: ")
        print(f"{sys.executable}{sys.argv[0]} numero1 numero2")
        print("ejemplo")
        print(f'{sys.executable}{sys.argv[0]} 4 8')
        sys.exit(1)
        #se ingresa numero (1) porque se ha generado un error
    #si hay 3 parametros
    else:
        #guardar n1 el primer numero que sea un entero
        try:
            n1=int(sys.argv[1])
        except ValueError:
            print("ERROR: El primer parámetro no es un numero")
            sys.exit(1)
        try:
            n2=int(sys.argv[2])
        except ValueError:
            print("ERROR: El primer parámetro no es un numero")
            sys.exit(1)
        #mostramos el resultado
        print(f"la suma de {n1} y {n2} es {funcion_suma(n1,n2)}")
        sys.exit(0)

