from IP_Handler import IPFilterHandler
from port_handler import PortFilterHandler 
from scapy.all import  *
from dotenv import load_dotenv
import os
load_dotenv()

class Firewall:
    def __init__(self):
        self.first_handler = None
    
    def set_first_handler(self, handler):
        self.first_handler = handler

    def process(self, packet):
        if self.first_handler:
            return self.first_handler.handler_request(packet)
        else:
            print("No handlers.")
            return "No processing"





def main():
    print("Starting the firewall...")
    
    ip_handler = IPFilterHandler()
    port_handler = PortFilterHandler() 


    #Make the firewall and assign the first handler
    firewall = Firewall()
    firewall.set_first_handler(ip_handler)
    #Assign pattern
    ip_handler.set_next(port_handler)
   
    #Process a packet 


    def packet_callback(packet):
        #packet.show()
        firewall.process(packet)

    sniff(prn = packet_callback, count = 1000)

if __name__ == "__main__":
    main()
