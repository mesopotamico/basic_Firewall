
from scapy.all import sniff, TCP

def packet_callback(packet):
    if packet.haslayer(TCP):
        tcp_layer = packet.getlayer(TCP)
        flags = tcp_layer.flags
        flag_str = ""

        # Abreviaturas de banderas TCP
        if flags & 0x02:
            flag_str += "SYN "
        if flags & 0x10:
            flag_str += "ACK "
        if flags & 0x01:
            flag_str += "FIN "
        if flags & 0x08:
            flag_str += "PSH "
        if flags & 0x04:
            flag_str += "RST "
        if flags & 0x20:
            flag_str += "URG "

        print(f"Packet Summary: {packet.summary()}")
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")
        print(f"Sequence Number: {tcp_layer.seq}")
        print(f"Acknowledgment Number: {tcp_layer.ack}")
        print(f"Flags: {flag_str.strip()}")
        print(f"Window Size: {tcp_layer.window}")
        print(f"Payload: {packet[TCP].payload}")
        print("-" * 50)

# Captura paquetes en la interfaz de red especificada
sniff(prn=packet_callback, count = 10 ,filter="tcp", store=0, iface="en0")  # Reemplaza 'en0' con tu interfaz de red
