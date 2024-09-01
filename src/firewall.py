from IP_Handler import IPFilterHandler
from packet_model import Packet 


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


    #Make the firewall and assign the first handler
    firewall = Firewall()
    firewall.set_first_handler(ip_handler)
    # Firewall code goes here

    #Process a packet 

    packet1 = Packet('192.168.1.10', 80, 'TCP')
    result = firewall.process(packet1)
    
    print(result)

if __name__ == "__main__":
    main()
