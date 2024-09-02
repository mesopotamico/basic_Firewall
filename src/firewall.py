from IP_Handler import IPFilterHandler
from scapy.all import  *
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

    #packet = Packet('192.168.1.10', '192.168.1.10' ,80, 'TCP')
    #result = firewall.process(packet)

    def packet_callback(packet):

        ip = packet.getlayer(IP)
        tcp = packet.getlayer(TCP) 

        standar_packet = Packet(ip.src, ip.dst, int(tcp.sport) , 'TCP' )

        firewall.process(standar_packet)

    sniff(prn = packet_callback, count = 1)



    
    print(result)

if __name__ == "__main__":
    main()
