from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

class ProtocolFilterHandler(Handler):
    
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):

        protocols = self.mostrar_protocolos(packet)

        if self.is_allowed_protocol(protocols): 
            if self.next_handler:
                print(f"Allowed protocols") 
                return self.next_handler.handler_request(packet) 
        else:
            print(f"Blocked {packet.name} this is not allowed protocol")
            return "Blocked by port filter."

    def is_allowed_protocol(self, protocols):
        allowed_protocols = ['TCP','UDP','Ethernet','IP','Raw']
        return self.contains_sublist(allowed_protocols, protocols) 

    def mostrar_protocolos(self, packet):
        protocolos = set()
        # Recorrer la pila de protocolos del paquete
        while packet:
            protocolos.add(packet.name)
            if packet.payload:
                packet = packet.payload
            else:
                break
        print(protocolos)
        return list(protocolos)

    def contains_sublist(self, lst, sublst):
        len_sub = len(sublst)
        for i in range(len(lst) - len_sub + 1):
            if lst[i:i + len_sub] == sublst:
                return True
        return False

