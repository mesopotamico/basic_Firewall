from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os

class LoggingHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):

        print(f"Logging packet: {packet}")
        if self.next_handler:
            return self.next_handler.handle_request(packet)
        return "Logged and processed"

