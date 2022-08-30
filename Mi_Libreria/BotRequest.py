import requests #importando libreria para solicitud de request
from bs4 import BeautifulSoup #iimportando libreria para 
import re #libreria de expresiones regulares

#Definiendo los colores del texto colores
azul = "\33[1;36m" 
gris="\33[0;37m"
blanco="\33[1;37m"

def datos_Game(url):
    #diccionario de salida que devualeve informacion de un producto 
    d={}
    # definiendo el user Agent en el encabezado del mensajero
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }
    #"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0"
    #realizando la peticion mediante el uso de libreria request
    
    print(f"{azul}realizando la petición a:\n {blanco} {url} {gris} fin de la petición\n")
    #aca se cibfigura el tiempo de espera con el servidor en caso de que no responda, se peude manejar la excepcion
    req=requests.get(url, headers=headers, timeout=2)
    print(req.status_code)

    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.title)
    #print(soup.prettify())
    print(req.text)
    """print(f"{azul}codigo de respuesta ...: {blanco}{request.status_code}{req.reason}{gris}")
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
        return d"""

if __name__=="__main__":
    #url="https://www.game.es/ACCESORIOS/AURICULARES/PC-GAMING/GAME-HX500-RGB-71-PRO-GAMING-HEADSET-PC-PS4-AURICULARES-AURICULARES-GAMING/169628"
    #url="https://www.game.es/19628"
    url="https://www.enel.com.co/es/reporte-de-fallas.html?utm_id=7908&utm_source=google%20search%20-%20nacional&utm_medium=cpc&utm_campaign=enel%20colombia_rerporte-de-fallas-b2b_cli&utm_term=arte%20entretenimiento_anuncio%20de%20texto_na"
    datos=datos_Game(url)
    
    """for clave, valor in datos.items():
        print(f"{azul}{clave.upper()}: {blanco}{valor}{gris}")
    exit(0)"""
    