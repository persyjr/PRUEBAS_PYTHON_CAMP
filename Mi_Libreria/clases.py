#instrucciones para crear el objeto soldado
class Soldado:
    #ATRIBUTOS valores por defecto para los nuevos objetos
    vuela=False
    velocidad=3

    #definiendo mi constructor donde defino mis atributos de instancia
    #los cuales se definen por defecto segun lo que indique aca cuando cree el objeto
    def __init__(self,nivel):
        #definiendo los atributos de instancia
        self.nivel=nivel
        self.vida=nivel*1000
        self.fuerza=nivel*10000
    
    #metodo que habilita el atributo vuela o capacidad de volar
    def coger_alas(self):
        self.vuela=True
    
    #metodo que resta daño a la vida del objeto
    def recibe_golpe(self,dano):
        self.vida-=dano
        #con el signo menos resto el valor original de vida y asigno nuevo valor

#instanciando el soldado !
tropa1=Soldado(13)
print(f"este es el nivel del soldado: {tropa1.nivel}")
print(f"esta es la capacidad de volar: {tropa1.vuela}\n")
print("VOY A COGER ALAS")
tropa1.coger_alas()
print(f"esta es la capacidad de volar ahora: {tropa1.vuela}\n")
print("CON EL METODO DAÑO")
print(f"esta es la vida inicial: {tropa1.vida}\n")
print("Recibe 200 de daño")
tropa1.recibe_golpe(200)
print(f"esta es la vida despues del golpe: {tropa1.vida}\n")
