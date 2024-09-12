import time
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle_request(self, packet):
        pass
class Connection:
    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.state = 'ESTABLISHED'
        self.first_seen = time.time()
        self.last_seen = time.time()
        self.packet_count = 0

    def update(self):
        self.last_seen = time.time()
        self.packet_count += 1

    def expire(self, timeout):
        return time.time() - self.last_seen > timeout

class StatefulHandler(Handler):
    def __init__(self, timeout=60):
        self.next_handler = None
        self.connection_table = {}
        self.timeout = timeout

    def set_next(self, handler):
        self.next_handler = handler

    def handle_request(self, packet):
        current_time = time.time()
        connection_id = (packet.ip, packet.port, packet.protocol)
        
        # Clean up expired connections
        expired_connections = [cid for cid, conn in self.connection_table.items()
                               if conn.expire(self.timeout)]
        print(f"Las conexiones expiradas son {expired_connections}")
        for cid in expired_connections:
            del self.connection_table[cid]
        
        if connection_id in self.connection_table:
            connection = self.connection_table[connection_id]
            print(f"Packet allowed for existing connection: {connection_id}, Info: {connection.__dict__}")
            connection.update()
        else:
            print(f"New connection attempt: {connection_id}")
            self.connection_table[connection_id] = Connection(packet.ip, packet.port, packet.protocol)
        
        if self.next_handler:
            return self.next_handler.handle_request(packet)

class Packet:

    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port
        self.protocol = protocol


# Creamos el manejador con un timeout de 5 segundos
handler = StatefulHandler(timeout=5)

# Enviamos algunos paquetes para simular conexiones
packets = [
    Packet(ip='192.168.1.1', port=1234, protocol='TCP'),
    Packet(ip='192.168.1.1', port=1234, protocol='TCP'),
    Packet(ip='192.168.1.2', port=5678, protocol='UDP'),
    Packet(ip='192.168.1.1', port=1234, protocol='TCP'),
]

# Procesamos los paquetes a través del manejador
for packet in packets:
    handler.handle_request(packet)
    time.sleep(1)  # Esperamos 1 segundo entre paquetes

# Simulamos la expiración de conexiones
time.sleep(6)  # Esperamos más tiempo que el timeout

# Enviamos un nuevo paquete para ver si se ha limpiado la conexión anterior
new_packet = Packet(ip='192.168.1.1', port=1234, protocol='TCP')
handler.handle_request(new_packet)
