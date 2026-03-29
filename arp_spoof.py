#/usr/bin/env python

from scapy.layers.l2 import ARP

# Create ARP Packet Response.  network_scanner created an ARP Request.
# op (operation) value 1 (who has X). op value 2 is an ARP Reply
# where the target responds with its MAC Address.
# The next value set is pdst, ip address of target computer.
packet = ARP(op=2, pdst="" )