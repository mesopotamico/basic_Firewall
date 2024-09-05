from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

class PortFilterHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):
        ip = packet.getlayer(IP)
        if packet.haslayer(TCP):
            tcp = packet.getlayer(TCP)
            if self.is_allowed_port(tcp.sport):
                print(f"The scanned port {tcp.sport} is avaliable")
                if self.next_handler:
                    return self.next_handler.handler_request(packet) 
            else:
                print(f"Packet from {ip.src} with the port {tcp.sport} blocked by filter.")
                return "Blocked by TCP filter."

    def is_allowed_port(self, port):
        allowed_ports = [80, 443]
        return port in allowed_ports
