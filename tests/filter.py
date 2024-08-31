from scapy.all import sniff, get_if_list, IP, TCP 
from scapy.layers.inet6 import IPv6 
from scapy.layers.inet import UDP

print(get_if_list())

#prn osea la funcion que va a procesar el paquete

def packet_callback(packet):
    if packet.haslayer('TCP'):
        print(f"TCP packet: {packet['TCP'].summary()}")

    if packet.haslayer('UDP'):
        print(f"UDP packet: {packet['UDP'].summary()}")

    if packet.haslayer('ICMP'):
        print(f"ICMP packet: {packet['ICMP'].summary()}")

def analyze_udp(packet):
    if packet.haslayer(IPv6):
        src_ip = packet[IPv6].src
    print(f"Packet IP src: {src_ip}")

def packet_info(packet):
    print(packet.show())

#lfilter es la funcion que permite hacer el filtrado de paquetes

def filter_IPv6(packet):
    if packet.haslayer(IPv6):
        return True
    return False 


def filter_flags_IP(packet):
    if filter_flags_TCP(packet):
        if packet.haslayer(IP):
            if packet[IP].dst == "192.168.1.8" :
                return True
        return False 


def filter_flags_TCP(packet):
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        flags = tcp_layer.flags

        if flags & 0x02:
            return True
    return False 


sniff(iface = "en0",filter = "icmp or tcp",count = 5 ,lfilter = filter_flags_IP,prn = packet_info, store = 0)

