# src/firewall.py
class Firewall:
    def __init__(self):
        self.first_handler = None
    
    def set_first_handler(self, handler):
        self.first_handler = handler

    def process(self, packet):
        if self.first_handler:
            return self.first_handler.handle_request(packet)
        else:
            print("No handlers.")
            return "No processing"






def main():
    print("Starting the firewall...")
    # Firewall code goes here

