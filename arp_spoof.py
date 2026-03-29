#/usr/bin/env python

from scapy.layers.l2 import ARP

# Create ARP Packet Response.  Unlike network_scanner where we created an ARP Request.
# To do this we set op (operation) to 2. Value 1 is an ARP Request, who has X. 2 is an ARP
# Reply where the target responds with its MAC Address.
# The next value we set is pdst, the ip address of the target computer.
packet = ARP(op=2, pdst="" )