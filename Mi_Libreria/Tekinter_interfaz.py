import tkinter
#Este codigo funciona en visual estudio
__autor__="AD"
def imprime():
    print("acabas de presionar el boton imprimir")

ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta=tkinter.Label(ventana, text="hola mundo")
etiqueta.pack()
ventana.title("segunda ventana")
boton_salir= tkinter.Button(ventana, text="salir", fg="red", command=ventana.quit)
boton_salir.pack()
boton_Imprimir=tkinter.Button(text="imprimir", fg="blue", command=imprime())
boton_Imprimir.pack()
ventana.mainloop()