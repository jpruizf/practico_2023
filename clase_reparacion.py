class Reparacion:
    __patente: str
    __reparacion:str
    __repuesto:str
    __precio_repuesto:float
    __mano_de_obra:float
    __estado:bool
    def __init__(self,patente,reparacion,repuesto,precio_repuesto,mano_de_obra,estado):
        self.__patente = patente
        self.__reparacion = reparacion
        self.__repuesto = repuesto
        self.__precio_repuesto = precio_repuesto
        self.__mano_de_obra = mano_de_obra
    
    def get_patente(self):
        return self.__patente
    
    def get_reparacion(self):
        return self.__reparacion
    
    def get_repuesto(self):
        return self.__repuesto
    
    def get_precio_repuesto(self):
        return self.__precio_repuesto
    
    def get_mano_de_obra(self):
        return self.__mano_de_obra