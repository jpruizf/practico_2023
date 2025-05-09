from clase_reparacion import Reparacion
import csv

class Manejador_Reparaciones:
    reparaciones:list

    def __init__(self):
        self.reparaciones = []

    def cargar_reparacion(self,archivo):
        aux = []
        with open(archivo,"r",encoding='utf-8') as file:
            lector = csv.reader(file,delimiter=",")
            for i in lector:
              patente = i
              reparacion_x = i
              repuesto = i
              precio_repuesto = i
              mano_de_obra = i
              estado = i
              aux = Reparacion(patente,reparacion_x,repuesto,precio_repuesto,mano_de_obra,estado)
              self.reparaciones.append(aux)
        return self.reparaciones
    
    def calcular_total(self):
        for i in self.reparaciones:
            reparacion_x = i[1]
            precio_repuesto = i[3]
            mano_de_obra = i[4]
            sub_total = sum(precio_repuesto + mano_de_obra)
            total = sum(sub_total)
        print(f"Reparacion:{reparacion_x}/Precio repuesto:{precio_repuesto}/Mano de obra:{mano_de_obra}/Subtotal: {sub_total}\nTotal:{total}")
        return total
    def ordenar(self):
        self.reparaciones.sort()
    
    def encontrar_reparacion(self,aux_patente,total):
        encontrado = False
        i = 0
        while i < range(self.reparaciones) and not encontrado:
            if i[0] == aux_patente:
                encontrado = True
                print(f"{total}")
            i += 1

    def listar_cliente(self):
        for i in self.reparaciones:
            print(f"Reparacion:{i._Repracion__get_reparacion()}")