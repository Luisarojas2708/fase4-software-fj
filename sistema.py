from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    filename='logs_sistema.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ErrorSistema(Exception):
    pass


class EntidadSistema(ABC):

    @abstractmethod
    def mostrar(self):
        pass


class Cliente(EntidadSistema):

    def __init__(self, nombre, cedula):
        if not nombre:
            raise ErrorSistema("El nombre no puede estar vacío")

        if not cedula.isdigit():
            raise ErrorSistema("La cédula debe contener números")

        self.__nombre = nombre
        self.__cedula = cedula

    def mostrar(self):
        return f"Cliente: {self.__nombre} - {self.__cedula}"


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self):
        return self.precio * 2

    def descripcion(self):
        return f"Reserva de sala: {self.nombre}"


class AlquilerEquipo(Servicio):

    def calcular_costo(self):
        return self.precio * 3

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre}"


class AsesoriaEspecializada(Servicio):

    def calcular_costo(self):
        return self.precio * 4

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre}"


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            if self.duracion <= 0:
                raise ErrorSistema("Duración inválida")

            total = self.servicio.calcular_costo() * self.duracion

            logging.info(
                f"Reserva procesada: "
                f"{self.cliente.mostrar()} - "
                f"{self.servicio.descripcion()}"
            )

            return total

        except Exception as e:
            logging.error(str(e))
            raise
        