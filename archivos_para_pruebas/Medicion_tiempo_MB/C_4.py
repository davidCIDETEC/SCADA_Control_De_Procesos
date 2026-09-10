import time
from pymodbus.client.sync import ModbusTcpClient

#INICIA CONEXION CON PLC
client  = ModbusTcpClient('192.168.1.5', port=502)
estado_conexion = client.connect()

diferencia = 0
diferencia_mayor = 0
for i in range(1000):
    tiempo_1 = time.time()
    mensaje_1 = client.write_registers(0x1001,5, unit=1)
    if not mensaje_1.isError():
        tiempo_2 = time.time()
        diferencia = tiempo_2 - tiempo_1
        diferencia_mayor = max(diferencia_mayor, diferencia)
        

print(diferencia_mayor)
client.close()