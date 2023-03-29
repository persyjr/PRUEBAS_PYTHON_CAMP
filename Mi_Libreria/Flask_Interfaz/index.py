#pip install Flask #instalo flask
#importo flask para isntanciar la magia de crear el servidor de mi aplicacion
#render_template  para poder renderirar dentro de mi carpeta templates
from flask import Flask , render_template 

#inicializando la aplicación
#forma de inicializarla para referenciar el main
app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/inicio')
def Inicio():
    return('<h2> Bienvendio a mi sitio Web con Python 3.0</h2> </br> <p> Esta es tu pagina de inicio</p>')

@app.route('/hola')
def Saludo():
    saludo="<i>hola mundo</i>"    
    def saludar():
        return "<strong>TITULO</strong>"
    return(f'<h2> Bienvendio a mi sitio Web con Python 3.0</h2> </br> <p>{saludar()} este es un primer saludo desde la consola de python {saludo}</p> </br> <button onclick="">click </button>')

if __name__=="__main__":
    app.run(debug=True, port=3001) #app.run(debug=True)  me permite trabajar en modo desarrollo reiniciando el servidor
                        #app.run() Modo definitivo una vez se finalice el programa
                        #port=3001 puerto en el que quiero que corra el puerto por defecto es 5000