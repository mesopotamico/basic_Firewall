from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

load_dotenv()
allowed_ips_str = os.getenv('ALLOWED_IPS')
allowed_ips = allowed_ips_str.split(',')

class IPFilterHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):
        if packet.haslayer(IP):
            ip = packet.getlayer(IP)
            if self.is_allowed_ip(ip.src):
                print(f"Packet from {ip.src} allowed by IP filter. ")
                if self.next_handler:
                    return self.next_handler.handler_request(packet) 
            else:
                print(f"Packet from {ip.src} blocked by IP filter.")
                return "Blocked by IP filter."
        else:
            print("Packet does not have IP")

    def is_allowed_ip(self, ip):
        #allowed_ips = ['192.168.1.10', '10.0.0.5'] 
        return ip in allowed_ips
        return True


