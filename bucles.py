#primer ejercicio
print("EJERCICIO 1 'hola mundo' ")
# segundo ejercicio
a="hola"
b="adios"
print(a)
print(b)

#ejemplo de la sentencia if
a=1
b=2
if a > b:
    print(f"{a}  es mayor que {b}\n")
else:
    print(f"{a}  es menor que {b}\n\n")

#como manejar excepciones en python
#ejemplo con bucle while
print("EJERCICIO 2 OPCIONES")
print("[1] Suscribirme")
print("[2] Like")
print("[3] Comentario")
print()
#inicializacion de variables
opcion=0
intentos =0
#bucle hasta que se introduzca la opcion correcta
while opcion<1 or opcion>3:
    #mensaje a consola con input y asignacion de variable opcion
    opcion= input("Seleccione una opcion : ")
    try:
        #aseguro que el valor sea transformado a entero
        opcion =int(opcion)
    except:
        #except ValueError: PARA SOLO exceptuar ese error se utiliza para personalizar los mensajes en el print para comunicarle al usuario 
        #ejemplo : ingrese un numero diferente de cero , no se puede dividir por cero o
        #ingrese valores numericos no string
        #cuando por alguna razon la variable entero no contiene un numero me aseguro que opcion sea cero para continuar el bucle
        opcion =0
    intentos +=1
    if intentos>=5:
        print("has agotado el numero de intentos")
        break
        #me salgo del ciclo
    else:
        print(f"Has escogido la opcion {opcion}\n\n")