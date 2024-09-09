from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

load_dotenv()
allowed_protocols_str = os.getenv('ALLOWED_PROTOCOLS')
allowed_protocols = allowed_protocols_str.split(',')

class ProtocolFilterHandler(Handler):
    
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):

        protocols = self.show_protocols(packet)

        if self.is_allowed_protocol(protocols): 
            print(f"Allowed by filter protocols") 
            if self.next_handler:
                return self.next_handler.handler_request(packet) 
        else:
            print(f"Blocked {packet.name} this is not allowed protocol")
            return "Blocked by protocol filter."

    def is_allowed_protocol(self, protocols):
#        allowed_protocols = ['TCP','UDP','Ethernet','IP','Raw', 'DNS']
        return self.contains_sublist(allowed_protocols, protocols) 

    def show_protocols(self, packet):
        protocolos = set()
        # Recorrer la pila de protocolos del paquete
        while packet:
            protocolos.add(packet.name)
            if packet.payload:
                packet = packet.payload
            else:
                break
        return list(protocolos)

    def contains_sublist(self, lst, sublst):
        conjunto_principal = set(lst)
        conjunto_sublista = set(sublst)
        return len(conjunto_sublista - conjunto_principal) == 0
