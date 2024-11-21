print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO


class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        """Constructor de la clase Persona. Los datos pueden estar vacíos por defecto."""
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    # Setter y getter para el nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("nombre invalido. debe ser una cadena no vacia.")
    
    def get_nombre(self):
        return self.nombre
    
    # Setter y getter para la edad
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("edad invalida. debe ser un numero entero positivo.")
    
    def get_edad(self):
        return self.edad
    
    # Setter y getter para el dni
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) > 0:
            self.dni = dni
        else:
            print("dni invalido. debe ser una cadena no vacia.")
    
    def get_dni(self):
        return self.dni
    
    # Metodo para mostrar los datos de la persona
    def mostrar(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"dni: {self.dni}")
    
    # Metodo para verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad is not None:
            return self.edad >= 18
        return False

# Ejemplo de uso
persona1 = Persona("Alan Reyes", 16, "0708")
persona1.mostrar()
print("es mayor de edad:", persona1.es_mayor_de_edad())

persona2 = Persona()
persona2.set_nombre("Alexa")
persona2.set_edad(16)
persona2.set_dni("1234")
persona2.mostrar()
print("es mayor de edad:", persona2.es_mayor_de_edad())

