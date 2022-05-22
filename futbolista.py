from deportista import Deportista
from persona import Persona


class Futbolista(Persona,Deportista):

    listaFutbolista=[]
    
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        Futbolista.listaFutbolista.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas                  

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self,piernaHabil):
        self._PiernaHabils=piernaHabil


    def __str__(self) :
        return "Mi nombre es "+ Persona.getNombre(self) +" soy profesional en el deporte " + Deportista.getDeporte(self) + " Tengo "+ str(Persona.getEdad(self)) + " años de edad y llevo " + str(Deportista.getAñosPracticando(self))+ " años en el deporte" 


                