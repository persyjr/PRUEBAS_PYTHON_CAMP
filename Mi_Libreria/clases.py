import datetime
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

class Sla:
    def __init__(self,hora_input):
        self.hora_input=hora_input
        self.hora_actual=datetime.datetime.now()
        print(self.hora_actual)
        self.dispatch=self.hora_actual-self.hora_input
    
    
        
   

hora='2023-10-25 12:59:34'
hora=datetime.datetime.strptime(hora, "%Y-%m-%d %H:%M:%S")
print(hora)
sla= Sla(hora)

print(f"este es sla.hora_actual: {sla.hora_actual}")
print(f"este es sla.dispatch: {sla.dispatch.seconds}")
print(f"este es sla.dispatch: {type(sla.dispatch)}")