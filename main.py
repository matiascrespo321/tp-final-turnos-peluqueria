def mostrar_menu():
    print("Sistema de Turnos - Peluquería")
    print("(1) Registrar nuevo cliente")
    print("(2) Solicitar turno")
    print("(3) Listar turnos existentes")
    print("(4) Modificar o cancelar turno")
    print("(5) Filtros (por DNI / por fecha)")
    print("(6) Guardar datos en CSV / Cargar desde dict")
    print("(7) Salir")



def main():
    menu = True
    while menu:
        op = 1
        while op != 7:
            mostrar_menu()
            op = int(input("Seleccione una opción (1-7): "))
            
            if op == 1:
                print("Registrar nuevo cliente seleccionado.")
                # Función para registrar un nuevo cliente
            elif op == 2:
                print("Solicitar turno seleccionado.")
                # Función para solicitar un turno
            elif op == 3:
                print("Listar turnos existentes seleccionado.")
                # Función para listar turnos existentes
            elif op == 4:
                print("Modificar o cancelar turno seleccionado.")
                # Función para modificar o cancelar un turno
            elif op == 5:
                print("Guardar datos en CSV / Cargar desde dict seleccionado.")
                # Función para guardar/cargar datos
            elif op == 6:
                print("Filtros seleccionado.")
                # Función para filtrar por DNI o fecha
            elif op == 7:
                print("Saliendo del sistema.")
                menu = False
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()


