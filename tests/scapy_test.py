from scapy.all import *
# Definir una función de callback para procesar los paquetes
def procesar_paquete(paquete):
    print("Paquete capturado:")
    ip = paquete.getlayer(IP)
    print(f"La ip del paquete es: {ip.src}")
    # También puedes acceder a atributos específicos, por ejemplo:
    # print(paquete[IP].src)  # Dirección IP de origen

# Capturar paquetes en tiempo real
sniff(prn=procesar_paquete, count=2)  # Captura 10 paquetes

ip = IP(dst="www.google.com")

tcp = TCP(dport=80)

packet = ip/tcp

#`packet.show()
#packets = sniff(count = 5)

#packets.summary()

#send(packet)
