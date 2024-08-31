from scapy.all import *

ip = IP(dst="www.google.com")

tcp = TCP(dport=80)

packet = ip/tcp

#`packet.show()
packets = sniff(count = 5)

packets.summary()

send(packet)
