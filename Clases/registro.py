class Registro(object):
    """Clase base que representa un registro genérico de la base de datos"""
    def __init__(self, **kwargs):
        # **kwargs nos permite recibir cualquier cantidad de argumentos con nombre
        # Los asignamos como atributos del objeto
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)
    
    def __str__(self):
        """Representación en string del objeto"""
        atributos = []
        for clave, valor in self.__dict__.items():
            atributos.append(f"{clave}: {valor}")
        clase = self.__class__.__name__  # Obtiene el nombre de la clase actual
        return f"{clase}({', '.join(atributos)})"


class Cliente(Registro):
    """Clase específica para registros de clientes"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Llama al constructor de la clase padre
    
    def validar(self):
        """Validación específica para clientes"""
        if not hasattr(self, 'nombre') or self.nombre == "":
            return False
        if hasattr(self, 'dni') and len(self.dni.strip()) != 8:
            return False
        return True
    
    def nombre_completo(self):
        """Método específico para clientes"""
        if hasattr(self, 'apellido'):
            return f"{self.nombre} {self.apellido}"
        return self.nombre