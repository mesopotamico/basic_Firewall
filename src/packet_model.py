class Packet:
    def __init__(self, ip_src, ip_dst, port, protocol):
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.port = port 
        self.protocol = protocol
    
    def __repr__(self):
        return f"Packet(ip={self.ip}, port={self.port}, protocol={self.protocol})"

