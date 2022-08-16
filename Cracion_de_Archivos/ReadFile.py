archivo = open("arhivo_ejemplo.txt", "r", encoding="utf-8")
#para abrir el archivo y leerlo

#leyendo por parrafos
print("LEYENDO PARRAFOS")
contenido=archivo.read()
    #para guardar los datos en un archivo contenido
print(contenido+"\n")
    #para imprimir los datos de forma continua 

#leyendo por lineas
print("LEYENDO LINEA POR LINEA")
archivo = open("arhivo_ejemplo.txt", "r", encoding="utf-8")
for linea in archivo:
    #si imprimo las lineas de contenido me las imprime como colimnas 
    print(linea)
    #para imprimir los datos linea por linea
print()


#buscando coincidencias de texto en el archivo
print("BUSCANDO COINCIDENCIAS")
archivo = open("arhivo_ejemplo.txt", "r", encoding="utf-8")
for linea in archivo:
    if "Persy" in linea:
    #si encuntro la coincidencia del texto en mayusculas o minusculas
        print(linea, end ="" )
        #para imprimir los datos linea por linea  me imprime la linea, sin salto de linea

print("Archivo leido exitosamente")    
archivo.close()
