class Cliente:
    __dni: int
    __apellido: str
    __nombre: str
    __telefono: int
    __patente: str
    __vehiculo: str
    __estado: bool

    def __init__(self,dni,apellido,nombre,telefono,patente,vehiculo,estado):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__patente = patente
        self.__vehiculo = vehiculo
        self.__estado = estado
    def get_dni(self):
        return self.__dni
    
    def get_cliente(self):
        return f"{self.__nombre}-{self.__apellido}"
    
    def get_telefono(self):
        return self.__telefono
    
    def get_patente(self):
        return self.__patente
    
    def get_vehiculo(self):
        return self.__vehiculo
    
    def get_estado(self):
        return self.__estado
    
    def __str__(self):
        return f"{self.get_dni()}/{self.get_cliente()}/{self.get_patente()}/{self.get_vehiculo()}/{self.get_estado()}"