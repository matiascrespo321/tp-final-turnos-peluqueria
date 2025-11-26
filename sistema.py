""" Consignas
Trabajo Práctico Final – Sistema de Turnos para 
Peluquería 
Materia: Programación Orientada a Objetos (Python) 
Duración estimada: 4 semanas 
Modalidad: Consola (línea de comandos) 
Entrega: Github 
Objetivo general 
Desarrollar un sistema simple de gestión de turnos para una peluquería utilizando 
Programación Orientada a Objetos (POO). 
El sistema debe permitir crear, consultar, modificar y eliminar turnos, así como guardar y 
recuperar la información de manera persistente usando archivos CSV y dict en lugar de una 
base de datos. 
Requisitos técnicos 
● El programa debe ejecutarse completamente desde la línea de comandos. 
● No se permite el uso de frameworks web ni bases de datos. 
● La persistencia de los datos debe realizarse: 
1. Guardando los turnos en un archivo CSV. 
2. Convirtiendo esos datos a un archivo dict que actúe como “base de datos”. 
● Se debe utilizar Programación Orientada a Objetos, con al menos las siguientes 
clases: 
1. Cliente 
2. Turno 
3. Peluquería o GestorTurnos (que administre los turnos y maneje las operaciones 
principales) 
● El sistema debe contar con un menú principal interactivo (por consola) con opciones 
como: 
1. Registrar nuevo cliente 
2. Solicitar turno 
3. Listar turnos existentes 
4. Modificar o cancelar turno 
5. Guardar datos en CSV / Cargar desde dict 
6. Salir 
Persistencia y archivos 
● Cada vez que se agregue o modifique un turno, se debe cargar la información en el dict 
y luego volcarlo al CSV 
● El programa debe poder convertir CSV a dict y dict A CSV, simulando una base de 
datos persistente. 
● Al iniciar el programa, si existe el archivo CSV, se deben cargar los turnos 
automáticamente desde allí. 
Sugerencias 
● Validar que no se dupliquen turnos en el mismo horario. 
● Permitir filtrar turnos por cliente o fecha. 
● Manejar excepciones para evitar que el programa se interrumpa. 
● Usar datetime para manejar fechas y horas. 
Evaluación 
Se evaluará: 
● Diseño y uso correcto de clases y objetos. 
● Organización del código (métodos, módulos, legibilidad). 
● Manejo adecuado de archivos (CSV). 
● Validación y control de errores. 
● Funcionalidad completa del sistema. 
● Creatividad en las funcionalidades adicionales. 
"""

def mostrar_menu():
    print("Sistema de Turnos - Peluquería")
    print("1. Registrar nuevo cliente")
    print("2. Solicitar turno")
    print("3. Listar turnos existentes")
    print("4. Modificar o cancelar turno")
    print("5. Guardar datos en CSV / Cargar desde dict")
    print("6. Filtros (por DNI / por fecha)")
    print("7. Salir")

if __name__ == "__main__":
    op = 1
    while op != 7:
        mostrar_menu()
        opcion = int(input("Seleccione una opción (1-7): "))
        
        if opcion == 1:
            print("Registrar nuevo cliente seleccionado.")
            # Función para registrar un nuevo cliente
        elif opcion == 2:
            print("Solicitar turno seleccionado.")
            # Función para solicitar un turno
        elif opcion == 3:
            print("Listar turnos existentes seleccionado.")
            # Función para listar turnos existentes
        elif opcion == 4:
            print("Modificar o cancelar turno seleccionado.")
            # Función para modificar o cancelar un turno
        elif opcion == 5:
            print("Guardar datos en CSV / Cargar desde dict seleccionado.")
            # Función para guardar/cargar datos
        elif opcion == 6:
            print("Filtros seleccionado.")
            # Función para filtrar por DNI o fecha
        elif opcion == 7:
            print("Saliendo del sistema. ¡Hasta luego!")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")