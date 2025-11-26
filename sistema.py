""" Consignas

1. Guardando los turnos en un archivo CSV. 
2. Convirtiendo esos datos a un archivo dict que actúe como “base de datos”.

● Se debe utilizar Programación Orientada a Objetos, con al menos las siguientes 
clases: 
1. Cliente 
2. Turno 
3. Peluquería o GestorTurnos (que administre los turnos y maneje las operaciones 
principales)

● menu listo

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
class Transforma(object):
    def __init__(self, atributos, tipo_registro=None):
        self.keys = atributos
        self.tipo_registro = tipo_registro or Registro  # Por defecto usa Registro genérico

class Registro(object):
    """Clase base que representa un registro genérico de la base de datos"""
    def __init__(self, **kwargs):
        # **kwargs nos permite recibir cualquier cantidad de argumentos con nombre
        # Los asignamos como atributos del objeto
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

class Cliente(Registro):
    """Clase específica para registros de clientes"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llama al constructor de la clase padre

class DB(object):
    def __init__(self, filename, tipo_registro=None):
        self.filename = filename
        self.tipo_registro = tipo_registro or Registro
    
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