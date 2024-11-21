print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        """
        Constructor de la clase cuenta.
        :param titular: nombre del titular de la cuenta (obligatorio).
        :param cantidad: cantidad inicial en la cuenta (opcional, por defecto es 0.0).
        """
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        """
        getter para el titular de la cuenta.
        :return: el nombre del titular.
        """
        return self.__titular

    @titular.setter
    def titular(self, titular):
        """
        setter para el titular de la cuenta.
        :param titular: nuevo nombre del titular.
        """
        self.__titular = titular

    @property
    def cantidad(self):
        """
        getter para la cantidad en la cuenta.
        :return: el saldo actual de la cuenta.
        """
        return self.__cantidad

    def mostrar(self):
        """
        muestra los datos de la cuenta.
        :return: informacion de la cuenta como cadena de texto.
        """
        return f"titular: {self.__titular}, cantidad: {self.__cantidad:.2f}"

    def ingresar(self, cantidad):
        """
        ingresa una cantidad a la cuenta.
        :param cantidad: cantidad a ingresar (debe ser positiva).
        """
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        """
        retira una cantidad de la cuenta.
        :param cantidad: cantidad a retirar (puede dejar la cuenta en numeros rojos).
        """
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        """
        Constructor de la clase cuenta joven.
        :param titular: nombre del titular de la cuenta.
        :param cantidad: cantidad inicial en la cuenta.
        :param bonificacion: bonificacion de la cuenta en porcentaje.
        """
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        """
        getter para la bonificacion de la cuenta.
        :return: bonificacion de la cuenta en porcentaje.
        """
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        """
        setter para la bonificacion de la cuenta.
        :param bonificacion: nueva bonificacion en porcentaje.
        """
        self.__bonificacion = bonificacion

    def es_titular_valido(self, edad):
        """
        verifica si el titular es valido.
        :param edad: edad del titular.
        :return: true si el titular es mayor de edad y menor de 25 años, false en caso contrario.
        """
        return 18 <= edad < 25

    def retirar(self, cantidad, edad):
        """
        retira dinero de la cuenta si el titular es valido.
        :param cantidad: cantidad a retirar.
        :param edad: edad del titular.
        """
        if self.es_titular_valido(edad):
            super().retirar(cantidad)
        else:
            print("retirada no permitida: titular no valido.")

    def mostrar(self):
        """
        muestra los datos de la cuenta joven.
        :return: informacion de la cuenta joven como cadena de texto.
        """
        return f"cuenta joven\n" \
               f"titular: {self.titular}, cantidad: {self.cantidad:.2f}, bonificacion: {self.bonificacion}%"

# crear una cuenta joven con titular, cantidad inicial y bonificacion
cuenta_joven = CuentaJoven("Alan Reyes", 1000.0, 10)

# mostrar los datos de la cuenta joven
print(cuenta_joven.mostrar())  
# salida: cuenta joven
#         titular: Alan Reyes, cantidad: 1000.00, bonificacion: 10%

# intentar retirar dinero con un titular no valido
cuenta_joven.retirar(200, 17)  # salida: retirada no permitida: titular no valido.

# retirar dinero con un titular valido
cuenta_joven.retirar(200, 20)
print(cuenta_joven.mostrar())  
# salida: cuenta joven
#         titular: Alan Reyes, cantidad: 800.00, bonificacion: 10%

# cambiar la bonificacion
cuenta_joven.bonificacion = 15
print(cuenta_joven.mostrar())  
# salida: cuenta joven
#         titular: Alan Reyes, cantidad: 800.00, bonificacion: 15%
