#/usr/bin/env python
from scapy.layers.l2 import ARP

packet = ARP(op=2, pdst="192.168.1.123", hwdst="60:45:e8:31:e5:23", psrc="192.168.1.254" )