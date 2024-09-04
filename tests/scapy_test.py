from scapy.all import *
# Definir una función de callback para procesar los paquetes
def procesar_paquete(paquete):
    print("Paquete capturado:")
    paquete.show()
    ip = paquete.getlayer(IP)
    tcp = paquete.getlayer(TCP)
    port = paquete.sport 
    print(f"The port is showed like this: {port}")
    print(f"The ip is showed like this: {ip.src}")
#    print(f"La ip paquete es: {ip.src} y la destino es: {ip.dst}")
    #print(f"La tcp paquete es: {tcp}")
    # También puedes acceder a atributos específicos, por ejemplo:
    # print(paquete[IP].src)  # Dirección IP de origen

# Capturar paquetes en tiempo real
sniff(prn=procesar_paquete, count=1)  # Captura 10 paquetes

ip = IP(dst="www.google.com")

tcp = TCP(dport=80)

packet = ip/tcp

#`packet.show()
#packets = sniff(count = 5)

#packets.summary()

#send(packet)
