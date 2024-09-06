from scapy.all import *

# Captura de paquetes en tiempo real (o puedes cargar un archivo de captura con rdpcap())
packets = sniff(count=1)  # Captura 10 paquetes, ajusta según necesites

def mostrar_protocolos(packet):
    protocolos = set()
    # Recorrer la pila de protocolos del paquete
    while packet:
        protocolos.add(packet.name)
        if packet.payload:
            packet = packet.payload
        else:
            break
    return list(protocolos)

# Analiza cada paquete y muestra los protocolos
for pkt in packets:
    protocolos = mostrar_protocolos(pkt)
    print(f"Paquete: {pkt.summary()}")
    print("Protocolos:", protocolos)
    print("-" * 40)
