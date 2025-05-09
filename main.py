from manejador_clientes import Manejador_cliente
from manejador_reparacion import Manejador_Reparaciones

def menu():
    m_clientes = Manejador_cliente()
    m_reparacion = Manejador_Reparaciones()
    total = 0.0
    print("1.VER TODOS LOS DATOS Y REPARACIONES HECHAS AL VEHICULO DE CADA CLIENTE INGRESANDO EL DNI")
    print("2.VER SI TOTAS LAS REPARACIONES ENTAN TERMINADAS INGRESANDO NRO DE PATENTE")
    print("3.LISTADO DE TODOS LOS CLIENTE CON REPARACIONES PENDIENTES")
    print("4.VER LOS CLIENTES QUE LE USAN MAS EL SERVICIO DE REPARACION DE VEHICULO")
    print("5.TERMINAR")
    opcion = input("SELECCIONE UNA DE LAS OPCIONES DADAS-->")
    while(opcion != '5'):
        if opcion == '1':
           if m_clientes.cargar_cliente("clientes.csv") and m_reparacion.cargar_reparacion("reparaciones.csv"):
               print("Lectura exitosa!")
               m_clientes.ordenar_clientes()
               dni = input("DNI-->")
               m_clientes.encontra_cliente(dni)
               total = m_reparacion.calcular_total()
        elif opcion == '2':
            patente = input("Patente-->")
            m_clientes.leer_patente(patente)
            m_reparacion.encontrar_reparacion(patente,total)
        elif opcion == '3':
            m_clientes.listado_reparacion_no_terminado()
            m_reparacion.listar_cliente()
        elif opcion == '4':
            m_clientes.__it__()
        print("1.VER TODOS LOS DATOS Y REPARACIONES HECHAS AL VEHICULO DE CADA CLIENTE INGRESANDO EL DNI")
        print("2.VER SI TOTAS LAS REPARACIONES ENTAN TERMINADAS INGRESANDO NRO DE PATENTE")
        print("3.LISTADO DE TODOS LOS CLIENTE CON REPARACIONES PENDIENTES")
        print("4.VER LOS CLIENTES QUE LE USAN MAS EL SERVICIO DE REPARACION DE VEHICULO")
        print("5.TERMINAR")
        opcion = input("SELECCIONE UNA DE LAS OPCIONES DADAS-->")

if __name__ == '__main__':
    menu()