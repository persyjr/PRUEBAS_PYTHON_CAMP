archivo = open("arhivo_ejemplo.txt", "a", encoding="utf-8")
archivo.write("has adicionado esta linea a tu archivo \n")
archivo.write("ingresando mas datos .write puedes escribir en tu archivo cuantas veces quieras \n")
lista=["nuevo dato",1, "persy" ]
lista=str(lista)
archivo.write(lista+"ingresando List String con .write puedes escribir siempre y cuando se transforme a string \n")
print("Archivo abierto y sobreescrito exitosamente")
