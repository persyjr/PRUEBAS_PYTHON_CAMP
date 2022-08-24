import requests
from bs4 import BeautifulSoup
import re #libreria de expresiones regulares

#Definiendo los colores del texto colores
azul = "\33[1;36m" 
gris="33[0:37m"
blanco="33[1:37m"

def datos_Game(url):
    #diccionario de salida que devualeve informacion de un producto 
    d={}
    # definiendo el user Agent en el encabezado del mensajero
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"
    }
    #realizando la peticion mediante el uso de libreria request
    print(f"{azul}realizando la petición: {blanco}{url}{gris}")
    #aca se cibfigura el tiempo de espera con el servidor en caso de que no responda, se peude manejar la excepcion
    req=request.get(url, headers=headers, timeout=10)
    print(f"{azul}codigo de respuesta ...: {blanco}{request.status_code}{req.reason}{gris}")
    #en caso de que la peticion no se realice de forma correcta devuelvo el error
    if req.status_code !=200:
        return {"Error": f"{req.reason}", "status_code": f"{req.status_code}" }
        #proceso de captura de datos 
        #url del producto
        d["url"]=req.url
        #ide del producto
        d["id"]=d["url"].split("/")[-1]
        #creamos el objeto bs4 a partir del codigo html
        soup.BeautifulSoup(req.text,"html.parser")  
        #nombre del producto
        d["url_imagen"] = soup.find("img", id="producto-cover").attrs.get("src")
        #plataformas
        objs_plat = soup.find("dd").find_all("a")
        d["plataformas"]=[]
        for item in objs_plat:
            #estoy aagregando lo que necesito a la clave plataforas es decir el contenido en limpio
            d["plataformas"].append(item.text.strip())
        #valoración
        try:
            #string del atributo que contiene la valoracion entre 0 y 5
            c_point=soup.find("a", class_="reviews-points-m").attrs.get("class")[-1]
            # extraemos el numero que representa la puntiación del string del atributo
            puntos=re.search(r'points=(/d)', c_point).group(1)
            #convertimos el string  o expresion regular en un entero                   
        except:
            d["valoracion"]=None

        #Precios
        obj_precio =soup.find("div",class_="buy--price")#objeto que contiene el precio anterior y el actual 
        try:
            d["precio_antes"]=float(obj_precio.find("small").text.replace("€","").replace(",","."))
        except:
            d["precio_antes"]=None
        
        #PRECION ACTUAL
        try:
            #obtenemos el string con el valor entero del precio actual
            p_int =obj_precio.find("spam").text.strip().split("\n")[0].strip()
            #obtenemos el string con el valor decimal del precio actual
            p_dec=obj_precio.find("span",class_="decimal").text.replace("'",".")
            #concatenamos el string con el valor entero y el decimal y lo convertimos a float
            d["precio_ahora"]=float(p_int+p_dec)
        except:
            d["precio_ahora"]=None
        #devolvemos el diccionario con los datos obtenidos
        #brakpoint()
        return d

if __name__=="__main__":
    url=
    url="https://www.game.es/19628"
    #url
    datos=datos_Game(url)
    for clave, valor in datos.items():
        print(f"{azul}{clave.upper()}: {blanco}{valor}{gris}")
    exit(0)