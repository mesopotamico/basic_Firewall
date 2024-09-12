import time
from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os
    
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

    def handler_request(self, packet):
        #Where we can get the IP

        if packet.haslayer(TCP):
            port = packet.getlayer(TCP)
            protocol = 'TCP'
        elif packet.haslayer(UDP):
            port = packet.getlayer(UDP)
            protocol = 'UDP'

            #Other protocols but you can handle with the other handlers

        if packet.haslayer(IP): 
            ip = packet.getlayer(IP)
            source_ip = ip.src
        else:
            source_ip = 'NA'
        #protocol.
        current_time = time.time()
        connection_id = ( source_ip, port.sport, protocol )
        
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
            self.connection_table[connection_id] = Connection( source_ip , port.sport, protocol)
            #(packet.ip, packet.port, packet.protocol)
        
        if self.next_handler:
            return self.next_handler.handler_request(packet)
