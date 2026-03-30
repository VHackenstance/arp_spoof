#/usr/bin/env python
from scapy.layers.l2 import ARP

packet = ARP(op=2, pdst="192.168.63.174", hwdst=" 00-50-56-e8-00-20", psrc="192.168.63.2" )