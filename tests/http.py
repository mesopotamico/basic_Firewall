from scapy.all import IP, TCP, sniff, Raw

def packet_filter_http(packet):
    # Verifico si es IP y TCP
    if packet.haslayer(IP) and packet.haslayer(TCP):
        layer_IP = packet.getlayer(IP)
        layer_TCP = packet.getlayer(TCP)


        if layer_TCP.dport == 80 or layer_TCP.sport == 80:
            print(f"Source {layer_IP.src} : layer_TCP.sport")
            print(f"Destination {layer_IP.dst} : layer_TCP.dport")

            if packet.haslayer(Raw):
                raw_layer = packet.getlayer(Raw)
                http_payload = raw_layer.load
                try:
                    print(f"Payload: {http_payload.decode(errors='ignore')}")
                except UnicodeDecodeError:
                    print("Payload: Non-text data")
            print("\n")


sniff(prn = packet_filter_http, filter = "tcp port 80", store = 0)

