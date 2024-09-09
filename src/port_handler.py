from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

load_dotenv()
allowed_ports_str = os.getenv('ALLOWED_PORTS')
allowed_ports = allowed_ports_str.split(',')


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
                print(f"The scanned TCP port {tcp.sport} is avaliable")
                if self.next_handler:
                    return self.next_handler.handler_request(packet) 
            else:
                print(f"TCP Packet from {ip.src} with the port {tcp.sport} blocked by filter.")
                return "Blocked by TCP filter."

        elif packet.haslayer(UDP):
            udp = packet.getlayer(UDP)
            if self.is_allowed_port(udp.sport):
                print(f"The scanned UDP port {udp.sport} is avaliable")
                if self.next_handler:
                    return self.next_handler.handler_request(packet)
            else:
                print(f"UDP Packet from {ip.src} with the port {udp.sport} blocked by filter.")
                return "Blocked by UDP filter."

    def is_allowed_port(self, port):
        #allowed_ports = [80, 443, 3478]
        return port in allowed_ports
