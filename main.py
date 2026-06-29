from sistema import *

print("===== SISTEMA SOFTWARE FJ =====")

# Operación 1
try:
    cliente1 = Cliente("Luis Rojas", "123456")
    print(cliente1.mostrar())
except Exception as e:
    print(e)

# Operación 2
try:
    cliente2 = Cliente("", "abc")
except Exception as e:
    print("Error:", e)

# Operación 3
sala = ReservaSala("Sala Premium", 50)
print(sala.descripcion())

# Operación 4
equipo = AlquilerEquipo("Computador", 30)
print(equipo.descripcion())

# Operación 5
asesoria = AsesoriaEspecializada("Python", 100)
print(asesoria.descripcion())

# Operación 6
try:
    reserva1 = Reserva(cliente1, sala, 2)
    print("Costo:", reserva1.procesar())
except Exception as e:
    print(e)

# Operación 7
try:
    reserva2 = Reserva(cliente1, equipo, -1)
    print(reserva2.procesar())
except Exception as e:
    print("Error:", e)

# Operación 8
reserva1.confirmar()
print("Estado:", reserva1.estado)

# Operación 9
reserva1.cancelar()
print("Estado:", reserva1.estado)

# Operación 10
try:
    reserva3 = Reserva(cliente1, asesoria, 3)
    print("Costo:", reserva3.procesar())
except Exception as e:
    print(e)

print("Programa ejecutado correctamente")
import logging

logging.info("Prueba de escritura en logs_sistema.txt")
logging.error("Prueba de error registrada en logs_sistema.txt")
