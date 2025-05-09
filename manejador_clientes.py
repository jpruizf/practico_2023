from clase_cliente import Cliente
import csv
class Manejador_cliente:
    clientes:list

    def __init__(self):
        self.clientes = []

    def cargar_cliente(self,archivo):
        with open(archivo,"r",encoding='utf-8') as file:
            lector = csv.reader(file,delimiter=",")
            for i in lector:
                dni = i
                apellido = i
                nombre = i
                telefono = i
                patente = i
                vehiculo = i
                estado = i
                aux = Cliente(dni,apellido,nombre,telefono,patente,vehiculo,estado)
                self.clientes.append(aux)
            return self.clientes
    
    def ordenar_clientes(self):
        self.clientes.sort()
    
    def encontra_cliente(self,dni):
        encontrado = False
        i = 0
        while(i < len(self.clientes) and not encontrado):
            if i[0] == dni:
                encontrado = True
                print(f"Cliente encontrado! {i._Cliente__get_dni()}/{i._Cliente__get_patente()}/{i._Cliente__get_cliente()}/{i._Cliente__get_telefono()}/{i._Cliente__get_vehiculo()}/{i._Cliente__get_estado()}")
            i += 1
        return self.clientes
    
    def leer_patente(self,aux_patente):
        encontrado = False
        i = 0
        while (i < len(self.clientes) and not encontrado):
            if i[4] == aux_patente and i[6] == 'P':
                encontrado = True
                i[6] = 'T'
                print(f"{i._Cliente__get_cliente()}/{i._Cliente__get_telefono()}/{i._Cliente__get_vehiculo()}")
            i += 1
        return f"patente no encontrada"
    
    def listado_reparacion_no_terminado(self):
        for i in self.clientes:
            if i[6] == 'P':
                print(f"{i._Cliente__get_cliente()}/{i._Cliente__get_telefono()}/{i._Cliente__get_patente()}/{i._Cliente__get_vehiculo()}")
        return self.clientes

    def __eq__(self,otro):
        encontrado = False
        i = 0
        while i < len(self.clientes) and not encontrado:
            if otro._Cliente_get_cliente() == i._Cliente__get_cliente() and otro._Cliente_get__dni() == i._Cliente__get_dni() and otro._Cliente__get_telefono() == i._Cliente__get_telefono():
                print(f"El cliente {i._Cliente__get_cliente()}/ con patente {i._Cliente__patente()}/ fue el que mas uso el servicio de repraciones")