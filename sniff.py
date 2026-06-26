from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
        else:
            print("Protocol       : Other")

        if packet.haslayer("Raw"):
            try:
                payload = packet["Raw"].load.decode(errors="ignore")
                print("Payload        :", payload[:100])
            except:
                print("Payload        : Unable to decode")

print("Starting Basic Network Sniffer...")
print("Capturing 20 packets...\n")

sniff(prn=packet_callback, count=20)

print("\nPacket capture completed.")
