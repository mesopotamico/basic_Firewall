from scapy.all import sniff

def list_protocols(packet):
    protocols = []
    
    if packet.haslayer('Ether'):
        protocols.append('Ethernet')
    if packet.haslayer('IP'):
        protocols.append('IP')
    if packet.haslayer('TCP'):
        protocols.append('TCP')
    if packet.haslayer('UDP'):
        protocols.append('UDP')
    if packet.haslayer('ICMP'):
        protocols.append('ICMP')
    if packet.haslayer('ARP'):
        protocols.append('ARP')
    if packet.haslayer('DNS'):
        protocols.append('DNS')
    if packet.haslayer('DHCP'):
        protocols.append('DHCP')
    if packet.haslayer('TLS') or packet.haslayer('SSL'):
        protocols.append('TLS/SSL')
    
    # Agregar más protocolos según sea necesario
    # Aquí se asume que TLS y SSL se manejan como capas 'TLS' y 'SSL' respectivamente

    if protocols:
        print(f"Protocols: {', '.join(protocols)}")

# Captura paquetes y muestra solo los protocolos presentes
sniff(prn=list_protocols)
