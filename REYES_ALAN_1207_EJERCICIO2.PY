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

# crear una cuenta con titular y saldo inicial
mi_cuenta = Cuenta("Alan Reyes", 10000)

# mostrar datos de la cuenta
print(mi_cuenta.mostrar())  # salida: titular: cantidad: 100000

# ingresar dinero
mi_cuenta.ingresar(50)
print(mi_cuenta.mostrar())  # salida: titular cantidad: 150.00

# retirar dinero
mi_cuenta.retirar(200)
print(mi_cuenta.mostrar())  # salida: titular: cantidad: -50.00

# cambiar el titular
mi_cuenta.titular = "Alan Reyes"
print(mi_cuenta.mostrar())  # salida: titular: cantidad: -50.00
