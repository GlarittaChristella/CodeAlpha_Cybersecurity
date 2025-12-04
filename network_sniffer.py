from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        dst_ip = packet['IP'].dst
        protocol = packet['IP'].proto
        
        protocol_name = {6: "TCP", 17: "UDP"}.get(protocol, "Other")
        
        print(f"\nSource IP: {src_ip} -> Destination IP: {dst_ip} | Protocol: {protocol}")
        print(f"Protocol Type: {protocol_name}")
        print("-" * 60)

sniff(prn=process_packet, store=False)
