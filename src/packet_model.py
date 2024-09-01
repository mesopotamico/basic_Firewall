class Packet:
    def __init__(self, ip, port, protocol):
        self.ip = ip
        self.port = port 
        self.protocol = protocol
    
    def __repr__(self):
        return f"Packet(ip={self.ip}, port={self.port}, protocol={self.protocol})"

