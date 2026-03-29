#/usr/bin/env python

from scapy.layers.l2 import ARP

# Create ARP Packet Response.  network_scanner created an ARP Request.
# op (operation) value 1 (who has X). op value 2 is an ARP Reply
# where the target responds with its MAC Address.
# The next value set is pdst, ip address of target computer.
# I got this value by doing a network_scanner.py on interface eth0 IP
# The next value is the target MAC Address hwdst, which in my case is our default gateway (??).
packet = ARP(op=2, pdst="192.168.1.123", hwdst="60:45:e8:31:e5:23" )