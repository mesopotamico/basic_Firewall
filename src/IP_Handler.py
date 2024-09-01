from handler import Handler

class IPFilterHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handler_request(self, packet):
        if self.is_allowed_ip(packet.ip):
            print(f"Packet from {packet.ip} allowed by IP filter. ")
            if self.next_handler:
                return self.next_handler.handler_request(packet) 
        else:
            print("Packet from {packet.ip} blocked by IP filter.")
            return "Blocked by IP filter."

    def is_allowed_ip(self, ip):
        allowed_ips = ['192.168.1.10', '10.0.0.5'] 
        return ip in allowed_ips

