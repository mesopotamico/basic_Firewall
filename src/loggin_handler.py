from handler import Handler
from dotenv import load_dotenv
from scapy.all import *
import os
from datetime import datetime
import socket

class LoggingHandler(Handler):
    def __init__(self, log_file="log.txt"):
        self.next_handler = None
        self.log_file = log_file

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):
    
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        src_ip = packet[IP].src if packet.haslayer(IP) else "Unknown"
        dst_ip = packet[IP].dst if packet.haslayer(IP) else "Unknown"

        if packet.haslayer(TCP):
            protocol = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif packet.haslayer(UDP):
            protocol = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        else:
            protocol = "Other"
            sport = "N/A"
            dport = "N/A"

        log_entry = f"{timestamp} | Protocol: {protocol} | Source IP: {src_ip} | Source Port: {sport} | Dest IP: {dst_ip} | Dest Port: {dport}\n"
        
        with open(self.log_file, "a") as log:
            log.write(log_entry)

        if self.next_handler:
            return self.next_handler.handler_request(packet)
        return "Logged and processed"
