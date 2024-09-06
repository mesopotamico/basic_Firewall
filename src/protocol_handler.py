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
        ip = packet.getlayer(IP)

    def is_allowed_protocol(self, protocol):
        allowed_protocols = ['TCP','UDP']
        return protocol in allowed_protocols
